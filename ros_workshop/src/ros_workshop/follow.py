#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import numpy as np

class LookAtMe(object):
  
  def __init__(self):
    rospy.loginfo('Init LookAtMe')
    # Sub datos laser
    self.laser_sub = rospy.Subscriber('/bender/sensors/laser_front/scan', LaserScan, self.process_laser)
    # Pub comando base
    self.base_pub = rospy.Publisher('/bender/nav/base/cmd_vel', Twist, queue_size=1)
    self.command = Twist()
    
  def process_laser(self, msg):
    data = [(msg.angle_min+msg.angle_increment*i,msg.ranges[i]) for i,dist in enumerate(msg.ranges)]
    self.print_data(data)

  def print_data(self, data):
    for d in data:
      rospy.loginfo(d)

if __name__ == '__main__':
  rospy.init_node('t1')
  t1 = LookAtMe()
  rospy.spin()

