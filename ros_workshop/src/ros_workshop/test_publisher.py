#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def main():
  rospy.init_node('test_publisher')
  rospy.loginfo('test_publisher')
  # Base cmd
  base_pub = rospy.Publisher('/bender/nav/base/cmd_vel', Twist, queue_size=1)
  # Publish each sec
  rate = rospy.Rate(1)
  msg = Twist()
  while not rospy.is_shutdown():
    msg.angular.z = 0.1
    msg.linear.x = 0.1
    base_pub.publish(msg)
    rate.sleep()

if __name__ == '__main__':
  main()
