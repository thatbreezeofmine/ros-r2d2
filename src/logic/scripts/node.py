#!/usr/bin/env python

import rospy
from std_msgs.msg import String

pub = None
verbose_pub = None

def teleop_handler(data):
    global pub, verbose_pub
    pass

def controller_pub(data):
    global pub, verbose_pub
    pass

def logic():
    global pub, verbose_pub
    pass

if __name__ == "__main__":

    
    try:
        logic()
    except rospy.ROSInterruptException:
        pass