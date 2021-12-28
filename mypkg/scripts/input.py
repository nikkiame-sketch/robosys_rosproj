#!/usr/bin/env python3
#SPDX-License-Identifier: GPL-3.0
#Copyright (c) Shunsuke Yoneyama & Ryuichi Ueda All rights reserved.

import rospy
from std_msgs.msg import Int32

rospy.init_node('input')
pub = rospy.Publisher('input', Int32, queue_size=1)  

n = int(input("amount ="))
pub.publish(n)
