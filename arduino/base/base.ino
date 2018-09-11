#include <ros.h>
#include <geometry_msgs/Twist.h>
#include "hbridge.h"

ros::NodeHandle nh;
HBridge leftDriver(9,8,10);
HBridge rightDriver(6,7,5);


void messageCb(const geometry_msgs::Twist& cmd)
{
  int linear=((int)(cmd.linear.x*254));
  int angular=((int)(cmd.angular.z*254));
  int linear_vel= (abs(linear)*linear);
  int angular_vel= (abs(angular)*angular);
  //if (linear_vel+angular_vel<50){}
  rightDriver.set(linear + angular);
  leftDriver.set(linear + angular*(-1));
  
}

ros::Subscriber<geometry_msgs::Twist> sub("cmd_vel", &messageCb );

void setup()
{
  nh.initNode();
  nh.subscribe(sub);
}

void loop()
{
  nh.spinOnce();
  delay(100);
}

void basicTest()
{
  HBridge& driver = leftDriver;
  driver.setRawPwm(250);
  driver.brake();
  delay(1500);
  driver.activeBrake();
  delay(1500);
  driver.forward();
  delay(1500);
  driver.backward();
  delay(1500);
}

void setTest()
{
  HBridge& driver = leftDriver;
  driver.set(250);
  delay(1500);
  driver.set(-250);
  delay(1500);
}

