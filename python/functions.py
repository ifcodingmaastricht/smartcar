from nanpy import ArduinoApi, SerialManager
import time

connection = SerialManager(device='/dev/ttyACM0')
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

def forward(speed,duration):				#forward
	a.analogWrite(ENA, speed)  
	a.analogWrite(ENB, speed)
	a.digitalWrite(IN1, a.LOW)
  	a.digitalWrite(IN2, a.HIGH)    
  	a.digitalWrite(IN3, a.LOW)
  	a.digitalWrite(IN4, a.HIGH)  
  	time.sleep(duration)


def backward(speed,duration):				#forward
	a.analogWrite(ENA, speed)  
	a.analogWrite(ENB, speed)
	a.digitalWrite(IN1, a.LOW)
  	a.digitalWrite(IN2, a.HIGH)    
  	a.digitalWrite(IN3, a.LOW)
  	a.digitalWrite(IN4, a.HIGH)  
  	time.sleep(duration)


def backward(speed,duration):
  	a.analogWrite(IN1, speed)
  	a.analogWrite(IN2, 0)    
  	a.analogWrite(IN3, speed)
  	a.analogWrite(IN4, 0)
  	time.sleep(duration)
def turn(angle,direction,duration):
	if direction == 1:	
	  	a.analogWrite(IN1, angle)
	  	a.analogWrite(IN2, 0)    
	  	a.analogWrite(IN3, 0)
	  	a.analogWrite(IN4, angle)
	  	time.sleep(duration)
  	else:
  		a.analogWrite(IN1, 0)
	  	a.analogWrite(IN2, angle)    
	  	a.analogWrite(IN3, angle)
	  	a.analogWrite(IN4, 0)
	  	time.sleep(duration)

while True:
	forward(0,3)
	#turn(100,1,2)
