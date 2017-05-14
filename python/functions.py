from nanpy import ArduinoApi, SerialManager
import time

connection = SerialManager(device='/dev/tty.usbmodem1411')
a = ArduinoApi(connection=connection)

ENA=11
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
a.analogWrite(ENA,a.HIGH)  
a.analogWrite(ENB,a.HIGH)

def forward(speed,duration):				#forward
	a.analogWrite(IN1,a.0)
  	a.analogWrite(IN2,a.speed)    
  	a.analogWrite(IN3,a.0)
  	a.analogWrite(IN4,a.speed)  
  	time.sleep(duration)
def backward(speed,duration)
  	a.analogWrite(IN1,a.speed)
  	a.analogWrite(IN2,a.0)    
  	a.analogWrite(IN3,a.speed)
  	a.analogWrite(IN4,a.0)
  	time.sleep(duration)
def turn(angle,direction,duration)
	if direction = 1:	
	  	a.analogWrite(IN1,a.angle)
	  	a.analogWrite(IN2,a.0)    
	  	a.analogWrite(IN3,a.0)
	  	a.analogWrite(IN4,a.angle)
	  	time.sleep(duration)
  	else:
  		a.analogWrite(IN1,a.0)
	  	a.analogWrite(IN2,a.angle)    
	  	a.analogWrite(IN3,a.angle)
	  	a.analogWrite(IN4,a.0)
	  	time.sleep(duration)

while True:
	forward(250,3)
	turn(100,1,2)









