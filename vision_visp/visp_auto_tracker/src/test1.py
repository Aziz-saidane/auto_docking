#!/usr/bin/
env python
import rospy
import time
from geometry_msgs.msg import PoseStamped


def callback(data):
        c = PoseStamped()
	c.x = data.position.x
	c.y = data.position.y
 	c.z = data.position.z
	


if __name__ == '__main__':

      rospy.init_node("navig")
      rospy.Subscriber("/visp_auto_tracker/object_position", PoseStamped, callback)

