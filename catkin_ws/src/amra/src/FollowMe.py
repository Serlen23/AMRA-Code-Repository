#!/usr/bin/env python

import rospy

from geometry_msgs.msg import TwistStamped
from mavros_msgs.msg import State
from mavros_msgs.srv import CommandBool
from mavros_msgs.srv import CommandTOL
from mavros_msgs.srv import SetMode
from std_msgs.msg import Float64MultiArray

rospy.init_node('hop_python') 
state_sub = rospy.Publisher("mavros/state", State, queue_size = 10) 
local_tst_pub = rospy.Publisher("mavros/setpoint_velocity/cmd_vel", TwistStamped, queue_size = 10) 
arming_client = rospy.ServiceProxy("mavros/cmd/arming", CommandBool)
set_mode_client = rospy.ServiceProxy("mavros/set_mode", SetMode)
takeoff_cl = rospy.ServiceProxy('/mavros/cmd/land', CommandTOL)
rate = rospy.Rate(20)

pose = TwistStamped() 
pose.twist.linear.x = 0 
pose.twist.linear.y = 0
pose.twist.linear.z = 0
pose.twist.angular.x = 0
pose.twist.angular.y = 0
pose.twist.angular.z = 0

def callback(data):
    xNormCenter = data[0] + ((data[2] - data[0])/2)
    yNormCenter = data[1] + ((data[3] - data[1])/2)
    pointX = xNormCenter - 0.5 
    pointY = yNormCenter - 0.5
    pose.twist.angular.y = -pointX
    pose.twist.angular.z = -pointY
    local_tst_pub.publish(pose)


for i in range(0,200): #for 200 iterations
    local_tst_pub.publish(pose) #send the current position message object
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
    
rospy.Subscriber('boundingboxes', Float64MultiArray, callback)
rospy.spin()

print ("\nDisarming")
rospy.wait_for_service('/mavros/cmd/arming') #Wait here until the mavros node has created the topic "cmd/arming"
try:
    response = arming_client(value = False)
    rospy.loginfo(response)
except rospy.ServiceException as e:
    print("Disarming failed: %s" %e)