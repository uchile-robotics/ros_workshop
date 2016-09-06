#include <ros.h>
#include <geometry_msgs/Twist.h>
#include "hbridge.h"

ros::NodeHandle nh;
HBridge driver(1,2,3);

void messageCb( const geometry_msgs::Twist& cmd){
  driver.set(-200);
  delay(500);
  driver.set(200);
}

ros::Subscriber<geometry_msgs::Twist> sub("cmd_vel", &messageCb );

void setup(){
  driver.init();
  nh.initNode();
  nh.subscribe(sub);
}

void loop(){
  nh.spinOnce();
  delay(1);
}
