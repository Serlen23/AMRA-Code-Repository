#!/usr/bin/env python
#This first line is REQUIRED in every python script you plan to make for ROS.

#This file is ahybridization of jumptest.py and offb_node.cpp
#These comments have been made with the best of my knowledge, but are still probably wrong. I will update them when I get the chance.


import rospy #you'll need this import statement for every ROS python script.
import math

from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State
#.msg files are large files that standardize how certain things are communicated through ROS.

from mavros_msgs.srv import CommandBool
from mavros_msgs.srv import CommandTOL
from mavros_msgs.srv import SetMode

rospy.init_node('offb_python') 
#the name of the mavros node that we make with this script

state_sub = rospy.Publisher("mavros/state", State, queue_size = 10) 
local_pos_pub = rospy.Publisher("mavros/setpoint_position/local", PoseStamped, queue_size = 10) 
#Two publishers that publish to certain parts of the "mavros" node

arming_client = rospy.ServiceProxy("mavros/cmd/arming", CommandBool)
set_mode_client = rospy.ServiceProxy("mavros/set_mode", SetMode)
takeoff_cl = rospy.ServiceProxy('/mavros/cmd/land', CommandTOL) #Three services that can both publish and receive data
rate = rospy.Rate(20) #Sets the rate to 20Hz

pose = PoseStamped() #Position msg object
pose.pose.position.x = 0 
pose.pose.position.y = 0
pose.pose.position.z = 2
#Set up the initial location points for the autonomous vehicle. These are cartesian coordinates relative to the origin (scale unknown)

for i in range(0,200): #for 200 iterations
    local_pos_pub.publish(pose) #send the current position message object
    rate.sleep() #then wait for 1/rate seconds


print("\nSetting Mode")
rospy.wait_for_service('/mavros/set_mode') #Wait here until the mavros node has created the topic "set_mode"
try:
    response = set_mode_client(custom_mode="OFFBOARD") #The control method we're using requires the mode to be set to OFFBOARD.
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
    
try:
    starttime = rospy.get_rostime() #Record the current system time that ROS is recording.
    t = 0
    while t < 5:
        print(t)
        t = (float) ((rospy.get_rostime() - starttime)/(rospy.Time(20)-rospy.Time(0))) 

        pose.pose.position.x = 10 * math.sin(t*2*math.pi) 
        pose.pose.position.y = 10 * math.cos(t*2*math.pi)
        #parametric equation of a circle

        local_pos_pub.publish(pose) #publish the manipulated coordinates for the listener node
        rate.sleep() #wait for 1/rate seconds
            
except rospy.ServiceException as e:
    print("Circling failed: %s" %e)

print ("\nLanding")
rospy.wait_for_service('/mavros/cmd/land') #Wait here until the mavros node has created the topic "cmd/land"
try:
    response = takeoff_cl(altitude=10, latitude=0, longitude=0, min_pitch=0, yaw=0)
    rospy.loginfo(response)
except rospy.ServiceException as e:
    print("Landing failed: %s" %e)

print ("\nDisarming")
rospy.wait_for_service('/mavros/cmd/arming') #Wait here until the mavros node has created the topic "cmd/arming"
try:
    response = arming_client(value = False)
    rospy.loginfo(response)
except rospy.ServiceException as e:
    print("Disarming failed: %s" %e)