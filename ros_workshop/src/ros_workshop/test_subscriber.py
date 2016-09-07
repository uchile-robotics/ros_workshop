#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy

def main():
    rospy.init_node('test_subscriber')
    rospy.loginfo('test_subscriber')
    # Subscriber for joint states
    sub = rospy.Subscriber('/bender/joy', Joy, process_callback)
    rospy.spin()

def process_callback(msg):
    rospy.loginfo(msg)
    rospy.loginfo(msg.axes[0])

if __name__ == '__main__':
    main()
