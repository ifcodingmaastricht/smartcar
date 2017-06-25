from nanpy import ArduinoApi, SerialManager
import time

class Car():
    def __init__(self, arduinoApi=None, serialPort="/dev/ttyACM0"):
        self.PINS = {
            "LEFT_SPEED": 11, # ENA
            "RIGHT_SPEED": 5, # ENB
            "IN1": 9,
            "IN2": 8,
            "IN3": 7,
            "IN4": 6,
        }

        if arduinoApi:
            self.api = arduinoApi
        else:
            connection = SerialManager(device=serialPort)
            self.api = ArduinoApi(connection=connection)

        for pin in self.PINS.values():
            self.api.pinMode(pin, self.api.OUTPUT)

        self.left_speed_raw = 0
        self.left_direction = 0
        self.right_speed_raw = 0
        self.right_direction = 0

    def write(self):
        self.write_speed()
        self.write_left_direction()
        self.write_right_direction()

    def write_speed(self):
        self.api.analogWrite(self.PINS["LEFT_SPEED"], self.left_speed_raw)
        self.api.analogWrite(self.PINS["RIGHT_SPEED"], self.right_speed_raw)

    def write_left_direction(self):
        # both pins LOW if left_direction == 0 aka. full stop
        self.api.digitalWrite(self.PINS["IN3"], self.api.LOW if self.left_direction > 0 else self.api.HIGH)
        self.api.digitalWrite(self.PINS["IN4"], self.api.LOW if self.left_direction < 0 else self.api.HIGH)

    def write_right_direction(self):
        # both pins LOW if right_direction == 0 aka. full stop
        self.api.digitalWrite(self.PINS["IN1"], self.api.LOW if self.right_direction > 0 else self.api.HIGH)
        self.api.digitalWrite(self.PINS["IN2"], self.api.LOW if self.right_direction < 0 else self.api.HIGH)

    # -100 <= left_speed <= 100
    # -100 <= right_speed <= 100
    # a value of 0 means stop
    def move(self, left_speed, right_speed, turn=0):
        # cmp(-123, 0) == -1
        # cmp(0, 0)    == 0
        # cmp(88, 0)   == 1
        # aka it mimicks the "sign" function from other languages (and basic math)
        self.left_direction = cmp(left_speed, 0)
        self.right_direction = cmp(right_speed, 0)

        # Because the wheels only start moving when the analog port has
        # value 'threshold' or up. In our case it was somewhere between
        # 80 and 90.
        threshold = float(85)

        # Make sure we don't fuck up with values outside [-100...100]
        left_speed = min(100, max(-100, left_speed))
        right_speed = min(100, max(-100, right_speed))

        # Here we map a value [0...100] to [threshold...255]
        self.left_speed_raw = round((float(abs(left_speed)) / 100.0) * (255.0 - threshold) + threshold)
        self.right_speed_raw = round((float(abs(right_speed)) / 100.0) * (255.0 - threshold) + threshold)

        if turn > 0:
            self.right_speed_raw = 0
            # self.left_speed_raw = min(255, self.left_speed_raw + turn * 4)
        elif turn < 0:
            self.left_speed_raw = 0
            # self.right_speed_raw = min(255, self.right_speed_raw - turn * 4)

        # write debug info
        print "left_speed %d" % (left_speed)
        print "right_speed %d" % (right_speed)
        print "self.left_speed_raw %d" % (self.left_speed_raw)
        print "self.right_speed_raw %d" % (self.right_speed_raw)
        print "self.left_direction %d" % (self.left_direction)
        print "self.right_direction %d" % (self.right_direction)
        print ""

        # Write values to the Bruce car
        self.write()

    def fullStop(self):
        self.move(0,0,0)

import sys
if __name__ == "__main__":
    car = Car()

    while True:
        car.move(1,1,0)
        time.sleep(1)
        car.move(0,0,0)
        time.sleep(1)
        car.move(-1,-1,0)
        time.sleep(1)
        car.move(0,0,0)
        time.sleep(1)
