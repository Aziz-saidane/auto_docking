#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Int8
from tracking_qr_code.msg import Cord
from geometry_msgs.msg import Twist 
from math import *


def callback(data):
	
	c.X = data.pose.position.x
	c.Y = data.pose.position.y
	c.Z = data.pose.position.z

def callback1(data):
	global valid_pose
	valid_pose = data.data
	




if __name__ == '__main__':
	global c
	global valid_pose
	valid_pose = Int8()
	i=0
	j =0
	r =0
	theta =0
	c = Cord()
	T = Twist()
	rospy.init_node("navig")
	rospy.Subscriber("/visp_auto_tracker/object_position", PoseStamped, callback)
	rospy.Subscriber("/visp_auto_tracker/status", Int8, callback1)
	p = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
	r1 = rospy.Rate(50)
	
        while not rospy.is_shutdown() :
		
		if ((valid_pose == 3) and (j==0) ) :
			while( abs(c.X) > 0.005 ):
				if (c.X < 0) :
					T.angular.z = 0.3 
					T.linear.x=0.1
					p.publish(T)
					r1.sleep()
				else:
					T.angular.z = -0.3 
					T.linear.x=0.1
					p.publish(T)
					r1.sleep()
			j = 1
		if ( j==1) :		
			T.angular.z =0
			T.linear.x=0
			p.publish(T)
			r1.sleep()
			
			j = 2
		if (j==2) :
			while ( c.Z > 0.14) :
				if ( valid_pose == 3) :
					T.linear.x=0.4
					T.angular.z= -0.1
					p.publish(T)
					r1.sleep()
				else :
					T.angular.z= 0.05
					T.linear.x=0
					p.publish(T)
					r1.sleep()
			j =3
		if (j ==3):
			while ( i < 100):
				T.linear.x=0.2
				T.angular.z= 0
				p.publish(T)
				r1.sleep()
				i = i+1
			j = 4


		if (j ==4):
			T.linear.x=0
			T.angular.z= 0
			p.publish(T)
			r1.sleep()
			j = 5










			
			#r = sqrt((c.X-X1)**2+(c.Z-Z1)**2)
			#theta = 2*atan((c.Z-Z1)/((c.X-X1)+sqrt((c.X-X1)**2+(c.Z-Z1)**2))) 
			#print (r)
			#T.angular.z = theta /10 
			#T.linear.x = r *5 
			#p.publish(T)
			
			#j = j+1 
			#r1.sleep()
	
