#!/usr/bin/env python

import rospy
from rospy.exceptions import ROSException
from std_msgs.msg import String
import time
import yaml

pub = None
arduino = None
conf = None

def handler(data):
    global conf
    if conf['output']:
        rospy.loginfo(data.data)

def verbose(status):
    if conf['verbose']:
        print(status)

def logger():
    global pub, arduino, conf
    rospy.init_node('r2d2/msgs', anonymous=True)
    verbose('Intialized node "r2d2/msgs" successfully.')

    rospy.Subscriber('r2d2/msgs', String, handler)
    verbose('Subscribed to node "r2d2/msgs" successfully.')

    rospy.spin()

    time.sleep(2)
    verbose('r2d2/msgs ready.')
    

if __name__ == '__main__':

    conf = yaml.load(open("../config/conf.yaml", 'r'))
    verbose('Loaded config successfully.')

    try:
        logger()
    except rospy.ROSInterruptException:
        pass