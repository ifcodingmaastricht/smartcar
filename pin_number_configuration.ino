#include <Servo.h> //servo library
Servo myservo; // create servo object to control servo
int Echo = A4;  
int Trig = A5; 
int in1 = 9;
int in2 = 8;
int in3 = 7;
int in4 = 6;
int ENA = 11;
int ENB = 5;
int ABS = 100; /*This has to be at least 100, or the left side of the car won't work*/
int rightDistance = 0,leftDistance = 0,middleDistance = 0 ;
void _mForward()
{
 analogWrite(ENA,ABS);
 analogWrite(ENB,ABS);
 digitalWrite(in1,LOW);
 digitalWrite(in2,HIGH);
 digitalWrite(in3,LOW);
 digitalWrite(in4,HIGH);
 Serial.println("go forward!");
}

void _mBack()
{
 analogWrite(ENA,ABS);
 analogWrite(ENB,ABS);
 digitalWrite(in1,HIGH);
 digitalWrite(in2,LOW);
 digitalWrite(in3,HIGH);
 digitalWrite(in4,LOW);
 Serial.println("go back!");
}

void _mleft()
{
 analogWrite(ENA,ABS);
 analogWrite(ENB,ABS);
 digitalWrite(in1,LOW);
 digitalWrite(in2,HIGH);
 digitalWrite(in3,HIGH);
 digitalWrite(in4,LOW);
 Serial.println("go left!");
}

void _mright()
{
 analogWrite(ENA,ABS);
 analogWrite(ENB,ABS);
 digitalWrite(in1,HIGH);
 digitalWrite(in2,LOW);
 digitalWrite(in3,LOW);
 digitalWrite(in4,HIGH);
 Serial.println("go right!");
} 
void _mStop()
{
  digitalWrite(ENA,LOW);
  digitalWrite(ENB,LOW);
  Serial.println("Stop!");
} 
 /*Ultrasonic distance measurement Sub function*/
int Distance_test()   
{
  digitalWrite(Trig, LOW);   
  delayMicroseconds(2);
  digitalWrite(Trig, HIGH);  
  delayMicroseconds(20);
  digitalWrite(Trig, LOW);   
  float Fdistance = pulseIn(Echo, HIGH);  
  Fdistance= Fdistance/58;       
  return (int)Fdistance;
}  

void setup() 
{ 
  myservo.attach(3);// attach servo on pin 3 to servo object
  Serial.begin(9600);     
  pinMode(Echo, INPUT);    
  pinMode(Trig, OUTPUT);  
  pinMode(in1,OUTPUT);
  pinMode(in2,OUTPUT);
  pinMode(in3,OUTPUT);
  pinMode(in4,OUTPUT);
  pinMode(ENA,OUTPUT);
  pinMode(ENB,OUTPUT);
  _mStop();
} 

void loop() 
{
        _mForward();                     
}
