#include <ros.h>
#include <geometry_msgs/Twist.h>
#include "hbridge.h"

ros::NodeHandle nh;
HBridge leftDriver(9,8,10);
HBridge rightDriver(6,7,5);

#define SAT(x) ( ((x) > 255) ? 255 : ( ((x) < -255) ? -255 : (x) ) )

void messageCb(const geometry_msgs::Twist& cmd)
{
  int32_t leftCmd = cmd.linear.x*255 + cmd.angular.z*255;
  int32_t rightCmd = cmd.linear.x*255 - cmd.angular.z*255;;
  
  leftDriver.set(SAT(leftCmd));
  rightDriver.set(SAT(rightCmd));
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
  delay(1);
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
