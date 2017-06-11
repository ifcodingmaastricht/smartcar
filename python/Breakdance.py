from nanpy import ArduinoApi, SerialManager
import time

connection = SerialManager(device='/dev/ttyACM0')
a = ArduinoApi(connection=connection)

class Car():
	def __init__(self):


ENA=10
IN1=9
IN2=8
ENB=5 
IN3=7
IN4=6

a.pinMode(IN1,a.OUTPUT)
a.pinMode(IN2,a.OUTPUT) 
a.pinMode(IN3,a.OUTPUT)
a.pinMode(IN4,a.OUTPUT)
a.pinMode(ENA,a.OUTPUT)
a.pinMode(ENB,a.OUTPUT)
a.digitalWrite(ENA,a.HIGH)  
a.digitalWrite(ENB,a.HIGH)

   
while True:
  a.digitalWrite(IN1,a.HIGH)  #Anticlockwise
  a.digitalWrite(IN2,a.LOW)        #left wheel back
  a.digitalWrite(IN3,a.LOW)      
  a.digitalWrite(IN4,a.HIGH)       #right wheel forward
  time.sleep(2.0)
  a.digitalWrite(IN1,a.LOW)   #Stop
  a.digitalWrite(IN2,a.LOW)        #left wheel stop
  a.digitalWrite(IN3,a.LOW)      
  a.digitalWrite(IN4,a.LOW)        #right wheel stop
  time.sleep(2.0)
  a.digitalWrite(IN1,a.LOW)   #Clockwise
  a.digitalWrite(IN2,a.HIGH)       #left wheel forward
  a.digitalWrite(IN3,a.HIGH)      
  a.digitalWrite(IN4,a.LOW)        #right wheel back
  time.sleep(2.0)
  a.digitalWrite(IN1,a.LOW)   #Stop
  a.digitalWrite(IN2,a.LOW)        #left wheel stop
  a.digitalWrite(IN3,a.LOW)      
  a.digitalWrite(IN4,a.LOW)        #right wheel stop
  time.sleep(2.0)
