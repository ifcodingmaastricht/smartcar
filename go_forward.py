# -*- coding: utf-8 -*-
from nanpy import ArduinoApi, SerialManager
import time

connection = SerialManager(device='/dev/tty.usbmodem1411')
a = ArduinoApi(connection=connection)

ENA=10
IN1=9
IN2=8
ENB=5 
IN3=7
IN4=6

#a.pinMode(13, a.OUTPUT)
#a.digitalWrite(13, a.HIGH)
#while True:≈
   #a.digitalWrite(13, a.HIGH)
   #time.sleep(0.01)
   #a.digitalWrite(13, a.LOW)
   #time.sleep(0.01)

a.pinMode(IN1,a.OUTPUT)
a.pinMode(IN2,a.OUTPUT)
a.pinMode(IN3,a.OUTPUT)
a.pinMode(IN4,a.OUTPUT)
a.pinMode(ENA,a.OUTPUT)
a.pinMode(ENB,a.OUTPUT)
a.digitalWrite(ENA,a.HIGH)  
a.digitalWrite(ENB,a.HIGH)

   
while True:
  #a.digitalWrite(13, a.HIGH)
  #time.sleep(1)
  #a.digitalWrite(13, a.LOW)
  #time.sleep(1)
  a.digitalWrite(IN1,a.LOW)      
  a.digitalWrite(IN2,a.HIGH)         # left wheel goes forward
  a.digitalWrite(IN3,a.LOW)      
  a.digitalWrite(IN4,a.HIGH)         # right wheel goes forward
  time.sleep(0.5)
  a.digitalWrite(IN1,a.LOW)      
  a.digitalWrite(IN2,a.LOW)         #left wheel holds still
  a.digitalWrite(IN3,a.LOW)      
  a.digitalWrite(IN4,a.LOW)         # right wheel holds still
  time.sleep(500)

