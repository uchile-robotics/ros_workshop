#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import numpy as np

class Follow(object):
    def __init__(self):
        # Sub datos laser
        self.laser_sub = rospy.Subscriber('/bender/sensors/laser_front/scan', LaserScan, self.process_laser)
        # Pub comando base
        self.base_pub = rospy.Publisher('/bender/nav/base/cmd_vel', Twist, queue_size=1)
        self.command = Twist()
        
    def process_laser(self, msg):
        for i, distance in enumerate(msg.ranges):
            print distance

if __name__ == '__main__':
    rospy.init_node('p2')
    rospy.loginfo('Init Follow')
    try:
        p2 = Follow()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
    rospy.loginfo('Closing Follow')
