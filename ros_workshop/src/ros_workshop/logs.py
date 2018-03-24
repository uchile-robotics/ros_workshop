#!/usr/bin/env python

import rospy

def main():

    rospy.init_node('Logger Test')

    while not rospy.is_shutdown():
        try:
            rospy.loginfo("I am a INFO")
            rospy.sleep(2)
            rospy.logwarn("I am a WARN")
            rospy.sleep(2)
            rospy.logerr("I am a ERROR")
            rospy.sleep(2)
            rospy.logfatal("I am a FATAL ERROR")
            rospy.sleep(2)

        except KeyboardInterrupt:
            exit() 

if __name__ == '__main__':
    main()
