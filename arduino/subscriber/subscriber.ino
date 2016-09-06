#include <ros.h>
#include <std_msgs/UInt8.h>

ros::NodeHandle nh;

void messageCb( const std_msgs::UInt8& led_msg){
  analogWrite(13, led_msgs.data);
}

ros::Subscriber<std_msgs::UInt8> sub("toggle_led", &messageCb );

void setup()
{
  pinMode(13, OUTPUT);
  nh.initNode();
  nh.subscribe(sub);
}

void loop()
{
  nh.spinOnce();
  delay(1);
}
