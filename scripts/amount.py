#!/usr/bin/env python3
#SPDX-License-Identifier: BSD
#Copyright (c) Shunsuke Yoneyama & Ryuichi Ueda All rights reserved.

import rospy
from std_msgs.msg import Int32

def cb(massage):
    amount = int(massage.data)
    height = 0
    
    while myglass.calc_volume(0,height) < amount:
        height += 0.1

    pub.publish(int(height))


class glass:
	PI = 3.1415

	__bottom = 10
	__top = 10
	__height = 10
	__delta_s = 0

	def calc_height(self,size):
	#断面積がsizeになるときの高さを返す
	    value = ((size - self.bottom)/self.delta_s) * self.height

	    if value > self.height:
	        return 0
	    else:
                return value

	def calc_size(self,height):
	#高さheightの底面積
	    r = (self.bottom + (self.delta_s * (height / self.height)))/2

	    if height > self.height:
                return 0
	    else:
	        return r * r * self.PI

	def calc_volume(self,height1,height2):
	#height1とheight2の間の容積(ml)を返す
	    value = 0
        
	    #高さ0.1mmの円柱で近似
	    h = height1
	    while h < height2:
	        value += self.calc_size(h) * 0.1
	        h += 0.1

	    return value / 1000                

	def __init__(self,bottom,top,height):
	    self.bottom = bottom
	    self.top = top
	    self.height = height
	    self.delta_s = self.top-self.bottom
	    return None
    


if __name__ == '__main__':
    rospy.init_node('amount')
    sub = rospy.Subscriber('input',Int32,cb)
    pub = rospy.Publisher('amount', Int32 ,queue_size = 1)
    rate = rospy.Rate(1)
    myglass = glass(55,75,125)
    
    rospy.spin()

    #while not rospy.is_shutdown():
    #   rate.sleep()
