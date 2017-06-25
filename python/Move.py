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

        self.speed = 0
        self.angle = 0

    def move(self, speed=255):
        self.speed = speed
	self.update()
	
    def update(self):
	speed_left = abs(self.speed) + self.angle
	speed_right = abs(self.speed) - self.angle
        self.api.analogWrite(self.PINS["LEFT_SPEED"], max(0, speed_left))
        self.api.analogWrite(self.PINS["RIGHT_SPEED"], max(0, speed_right))
        self.api.digitalWrite(self.PINS["IN1"], self.api.LOW if self.speed > 0 else self.api.HIGH) # right wheels, backwards
        self.api.digitalWrite(self.PINS["IN2"], self.api.HIGH if self.speed > 0 else self.api.LOW)  # right wheels, forward
        self.api.digitalWrite(self.PINS["IN3"], self.api.LOW if self.speed > 0 else self.api.HIGH) # left wheel, backwards
        self.api.digitalWrite(self.PINS["IN4"], self.api.HIGH if self.speed > 0 else self.api.LOW)  # left wheel, forward

    def turn(self, angle=5):
        self.angle = angle
	self.update()

    def backwards(self, speed=255):
        pass

    def left(self):
        pass

    def right(self):
        pass    

import sys
if __name__ == "__main__":
    car = Car()
    car.move(100)
    time.sleep(2)
    car.turn(20)
    time.sleep(2)
    car.move(-100)
    car.turn(20)
    time.sleep(2)
    car.turn(0)
    time.sleep(1.8)
    car.move(0)
