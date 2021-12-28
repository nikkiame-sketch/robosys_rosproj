#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

rospy.init_node('input')
pub = rospy.Publisher('input', Int32, queue_size=1)  

n = int(input("amount ="))
pub.publish(n)
