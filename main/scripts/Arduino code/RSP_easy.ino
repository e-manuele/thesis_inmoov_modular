#if (ARDUINO >= 100) 
 #include "Arduino.h"
#else
  #include <wprogram.h>  
#endif

#include <Servo.h> 
#include <ros.h>

#include <std_msgs/UInt16MultiArray.h>

ros::NodeHandle nh;

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
void servo_cb( const std_msgs::UInt16MultiArray& cmd_msg)
{
  servo1.write(cmd_msg.data[0]); //set servo angle, should be from 0-180  
  servo2.write(cmd_msg.data[1]);
  servo2.write(cmd_msg.data[2]);
  servo2.write(cmd_msg.data[3]);
  servo2.write(cmd_msg.data[4]); // thumb?
}

ros::Subscriber<std_msgs::UInt16MultiArray> sub("hand_pos", servo_cb);

void setup()
{

  nh.initNode();
  nh.subscribe(sub);

  servo1.attach(2); //attach it to pin 2
  servo2.attach(3); // attach it to pin 3
  servo3.attach(4);
  servo4.attach(5);
  servo5.attach(6);
}

void loop()
{
  nh.spinOnce();
  delay(1);
}

