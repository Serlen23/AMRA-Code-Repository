#!/usr/bin/env python

import rospy

from geometry_msgs.msg import PoseStamped, TwistStamped;
from mavros_msgs.msg import State
from mavros_msgs.srv import CommandBool
from mavros_msgs.srv import CommandTOL
from mavros_msgs.srv import SetMode
from tf.transformations import quaternion_from_euler

rospy.init_node('hop_python') 
state_sub = rospy.Publisher("mavros/state", State, queue_size = 10) 
local_pos_pub = rospy.Publisher("mavros/setpoint_position/local", PoseStamped, queue_size = 10) 
arming_client = rospy.ServiceProxy("mavros/cmd/arming", CommandBool)
set_mode_client = rospy.ServiceProxy("mavros/set_mode", SetMode)
takeoff_cl = rospy.ServiceProxy('/mavros/cmd/land', CommandTOL)
rate = rospy.Rate(20)

pose = PoseStamped() #Position msg object
pose.pose.position.x = 0 
pose.pose.position.y = 0
pose.pose.position.z = 2
quat = quaternion_from_euler(0,0,0)
pose.pose.orientation.x = quat[0]
pose.pose.orientation.y = quat[1]
pose.pose.orientation.z = quat[2]
pose.pose.orientation.w = quat[3]

for i in range(0,200): #for 200 iterations
    local_pos_pub.publish(pose) #send the current position message object
    rate.sleep() #then wait for 1/rate seconds

print("\nSetting Mode")
rospy.wait_for_service('/mavros/set_mode') #Wait here until the mavros node has created the topic "set_mode"
try:
    response = set_mode_client(custom_mode="OFFBOARD") #The control method we're using requires the mode to be set to OFFBOARD or STABILIZED.
    rospy.loginfo(response) #Log the response from the service for debugging
except rospy.ServiceException as e:
    print("Set mode failed: %s" %e) #if an exception (error) is thrown at any point in the try loop, print an error message and move on.

print("\nArming")
rospy.wait_for_service('/mavros/cmd/arming') #Wait here until the mavros node has created the topic "cmd/arming"
try:
    response = arming_client(value = True) #Arm the autonomous vehicle.
    rospy.loginfo(response)
except rospy.ServiceException as e:
    print("Arming failed: %s" %e)
    
pose.pose.position.x = 0 
pose.pose.position.y = 0
pose.pose.position.z = 1

for i in range(0,100): #for 100 iterations
    quat = quaternion_from_euler(0,0,i)
    pose.pose.orientation.x = quat[0]
    pose.pose.orientation.y = quat[1]
    pose.pose.orientation.z = quat[2]
    pose.pose.orientation.w = quat[3]
    local_pos_pub.publish(pose) #send the current position message object
    rate.sleep()

print ("\nDisarming")
rospy.wait_for_service('/mavros/cmd/arming') #Wait here until the mavros node has created the topic "cmd/arming"
try:
    response = arming_client(value = False)
    rospy.loginfo(response)
except rospy.ServiceException as e:
    print("Disarming failed: %s" %e)