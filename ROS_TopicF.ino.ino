#include <ros.h>

#include <std_msgs/Float64.h>

// LEFT motor connection pins
int LMpin1 = 9;
int LMpin2 = 12;
// RIGHT motor connection pins
int RMpin1 = 10;
int RMpin2 = 11;
//Pins for ultrasonic sensor
int echoPin = A0;
int trigPin = A1;
// Ultrasonic sensor variables with float decimal point
float distance, duration, cm;
//Starting variables of motor speeds
int motRspeed = 0;
int motLspeed = 0;
//Creating value for motors
int motState = 0;

// LED pins connections
int ledPinG = 5;
int ledPinB = 6;

int x;
float pub;
int forward;
int halt;

ros::NodeHandle  nh;

void messageCb(std_msgs::Float64 & msg){

    
   x = msg.data;
   
   pub = x;
   Serial.print(x,pub);
     
}

void Stop () {// STOP function
    digitalWrite(LMpin1, LOW);
    digitalWrite(LMpin2, LOW);
    digitalWrite(RMpin1, LOW);
    digitalWrite(RMpin2, LOW);
    digitalWrite(ledPinB,HIGH);
    digitalWrite(ledPinG,HIGH);
    delay(2000);
    digitalWrite(ledPinB,LOW);
    digitalWrite(ledPinG,LOW);
  }
void Ahead () {// AHEAD only function
    digitalWrite(LMpin1, LOW);
    digitalWrite(LMpin2, HIGH);
    digitalWrite(RMpin1, LOW);
    digitalWrite(RMpin2, HIGH);
    digitalWrite(ledPinB,HIGH);
    digitalWrite(ledPinG,HIGH);
    delay(2000);
  }
void TurnL () { //Powering(Controling) Right motor
  
    digitalWrite(LMpin1, LOW);
    digitalWrite(LMpin2, HIGH);
    digitalWrite(RMpin1, LOW);
    digitalWrite(RMpin2, LOW);
    digitalWrite(ledPinB,HIGH);
    digitalWrite(ledPinG,LOW);
    delay(1000);
    digitalWrite(ledPinB,LOW);
  }

void TurnR () { // Powering(Controling) Left motor
  
    digitalWrite(LMpin1, LOW);
    digitalWrite(LMpin2, LOW);
    digitalWrite(RMpin1, LOW);
    digitalWrite(RMpin2, HIGH);
    digitalWrite(ledPinG,LOW);
    digitalWrite(ledPinB,LOW);
    delay(1000);
    digitalWrite(ledPinG,HIGH);   
  }

void Base(){
    digitalWrite(LMpin1, LOW);
    digitalWrite(LMpin2, LOW);
    digitalWrite(RMpin1, LOW);
    digitalWrite(RMpin2, LOW);
    digitalWrite(ledPinG,LOW);
    digitalWrite(ledPinB,LOW);
}

void Move() { // Function combining all functions responsible for robot movement
  if ((distance > 30)&&(pub==34)) {
    TurnL();
  }
  else if ((distance > 30) && (pub == 33)) {
    TurnR();
  }
  else if ((distance > 30) && (pub==35)) {
    Ahead();
  }
  else if (pub==14){
    Stop();
  }
  else if (pub!=34,33,35,14) {
    Base();
  }
}

// Declare a Subscribers object
 ros::Subscriber<std_msgs::Float64> sub("ROS_Topic", &messageCb);




void setup() {
   
  Serial.begin(9600);
   // Set all the motor control pins to outputs
  pinMode(LMpin1, OUTPUT);
  pinMode(LMpin2, OUTPUT);
  pinMode(RMpin1, OUTPUT);
  pinMode(RMpin2, OUTPUT);

  pinMode(ledPinG, OUTPUT);
  pinMode(ledPinB, OUTPUT);

  pinMode(trigPin, OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin, INPUT); // Sets the echoPin as an INPUT
  
  // Motors at start
  digitalWrite(LMpin1, LOW);
  digitalWrite(LMpin2, LOW);
  digitalWrite(RMpin1, LOW);
  digitalWrite(RMpin2, LOW);
  
  nh.getHardware()->setBaud(57600);
  nh.initNode();  
  nh.subscribe(sub); 
  

}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
  Serial.println(x);
  nh.spinOnce();

  Move();

}
