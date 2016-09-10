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
        # Filter
        ranges = []
        angles = []
        for i, distance in enumerate(msg.ranges):
            if distance < msg.range_max*0.9:
                ranges.append(distance)
                angles.append(msg.angle_min+msg.angle_increment*i)
        if not ranges or not angles:
            return # Avoid empty data
        # Process
        est_distance = np.mean(ranges)
        est_angle = np.mean(angles)
        # Calc command
        error_distance = est_distance - 0.5
        error_angle = est_angle - 0.0
        # Calc command using saturation limits
        linear_cmd = Follow.saturation(0.2*error_distance, -0.2, 0.2)
        angular_cmd = Follow.saturation(0.4*error_angle, -0.5, 0.5)
        # Set command
        self.command.linear.x = linear_cmd
        self.command.angular.z = angular_cmd
        self.base_pub.publish(self.command)
    
    @staticmethod
    def saturation(value, min_value, max_value):
        if value > max_value:
            return max_value
        if value < min_value:
            return min_value
        return value

if __name__ == '__main__':
    rospy.init_node('p2')
    rospy.loginfo('Init Follow')
    try:
        p2 = Follow()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
    rospy.loginfo('Closing Follow')
