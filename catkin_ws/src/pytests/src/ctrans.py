#!/usr/bin/env python
#hybridization of jumptest.py and offb_node.cpp


import rospy
import math
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State
from mavros_msgs.srv import CommandBool
from mavros_msgs.srv import CommandTOL
from mavros_msgs.srv import SetMode

rospy.init_node('offb_python')
state_sub = rospy.Publisher("mavros/state", State, queue_size = 10)
local_pos_pub = rospy.Publisher("mavros/setpoint_position/local", PoseStamped, queue_size = 10)
arming_client = rospy.ServiceProxy("mavros/cmd/arming", CommandBool)
set_mode_client = rospy.ServiceProxy("mavros/set_mode", SetMode)
takeoff_cl = rospy.ServiceProxy('/mavros/cmd/land', CommandTOL)
rate = rospy.Rate(20)

pose = PoseStamped()
pose.pose.position.x = 0
pose.pose.position.y = 0
pose.pose.position.z = 2

for i in range(0,200):
    local_pos_pub.publish(pose)
    rate.sleep()

print("\nSetting Mode")
rospy.wait_for_service('/mavros/set_mode')
try:
    response = set_mode_client(custom_mode="OFFBOARD")
    rospy.loginfo(response)
except rospy.ServiceException as e:
    print("Set mode failed: %s" %e)

print("\nArming")
rospy.wait_for_service('/mavros/cmd/arming')
try:
    response = arming_client(value = True)
    rospy.loginfo(response)
except rospy.ServiceException as e:
    print("Arming failed: %s" %e)
    
try:
    starttime = rospy.get_rostime()
    t = 0
    while t < 5:
        print(t)
        t = (float) ((rospy.get_rostime() - starttime)/(rospy.Time(20)-rospy.Time(0)))
        pose.pose.position.x = 10 * math.sin(t*2*math.pi) 
        pose.pose.position.y = 10 * math.cos(t*2*math.pi)
        local_pos_pub.publish(pose)
        rate.sleep()
            
except rospy.ServiceException as e:
    print("Circling failed: %s" %e)

print ("\nLanding")
rospy.wait_for_service('/mavros/cmd/land')
try:
    response = takeoff_cl(altitude=10, latitude=0, longitude=0, min_pitch=0, yaw=0)
    rospy.loginfo(response)
except rospy.ServiceException as e:
    print("Landing failed: %s" %e)

print ("\nDisarming")
rospy.wait_for_service('/mavros/cmd/arming')
try:
    response = arming_client(value = False)
    rospy.loginfo(response)
except rospy.ServiceException as e:
    print("Disarming failed: %s" %e)