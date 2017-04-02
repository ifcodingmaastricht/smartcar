from nanpy import ArduinoApi, SerialManager
import time

connection = SerialManager()

a = ArduinoApi(connection=connection)
a.pinMode(13, a.OUTPUT)
a.digitalWrite(13, a.HIGH)
while True:
   a.digitalWrite(13, a.HIGH)
   time.sleep(2)
   a.digitalWrite(13, a.LOW)
   time.sleep(2)
