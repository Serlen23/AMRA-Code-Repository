#!/usr/bin/env python

import rospy

from geometry_msgs.msg import PoseStamped, TwistStamped;
from mavros_msgs.msg import State
from mavros_msgs.srv import CommandBool
from mavros_msgs.srv import CommandTOL
from mavros_msgs.srv import SetMode

rospy.init_node('deadreckon')
state_sub = rospy.Publisher("mavros/state", State, queue_size = 10)
local_pos_pub = rospy.Publisher("mavros/setpoint_position/local", PoseStamped, queue_size = 10)
local_tst_pub = rospy.Publisher("mavros/setpoint_velocity/cmd_vel", TwistStamped, queue_size = 10)
arming_client = rospy.ServiceProxy("mavros/cmd/arming", CommandBool)
set_mode_client = rospy.ServiceProxy("mavros/set_mode", SetMode)
takeoff_cl = rospy.ServiceProxy("mavros/cmd/land", CommandTOL)
rate = rospy.Rate(20)

pose = PoseStamped()
pose.pose.position.x = 0
pose.pose.position.y = 0
pose.pose.position.z = 1.5

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

twist = TwistStamped()
twist.twist.linear.x = 1
twist.twist.linear.y = .1
for i in range (0,1000):
    local_tst_pub.publish(twist)
    rate.sleep()

print ("\nDisarming")
rospy.wait_for_service('/mavros/cmd/arming')
try:
    response = arming_client(value = False)
    rospy.loginfo(response)
except rospy.ServiceException as e:
    print("Disarming failed: %s" %e)