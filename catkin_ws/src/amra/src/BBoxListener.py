#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64MultiArray

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def listener():
    rospy.init_node('jetsonListener', anonymous=False)
    rospy.Subscriber('boundingboxes', Float64MultiArray, callback)
    rospy.spin()

if __name__ ==  '__main__':
    listener()
