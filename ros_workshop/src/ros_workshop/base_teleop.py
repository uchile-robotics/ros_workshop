#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class BaseController(object):
    def __init__(self):
        self.sub = rospy.Subscriber('joy', Joy, self.joy_callback)
        self.pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
        self.cmd = Twist()

    def joy_callback(self, msg):
        rospy.loginfo(msg)

def main():
    rospy.init_node('base_controller')
    rospy.loginfo('Init base controller')
    base = BaseController()   
    rospy.spin()

if __name__ == '__main__':
    main()
