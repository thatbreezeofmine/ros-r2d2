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
    global pub, arduino, conf
    if conf['use_arduino']:
        arduino.write(data.data)
    # TODO Publish the data to the Messages Node
    if conf['log_actions']:
        pub.publish("Action taken : (Vx, Vy, Omega) = %s." % data.data)

def verbose(status):
    if conf['verbose']:
        print(status)

def controller():
    global pub, arduino, conf
    rospy.init_node('r2d2/controller', anonymous=True)
    verbose('Intialized node "r2d2/controller" successfully.')

    if conf['use_arduino']:
        arduino = serial.Serial('/dev/ttyACM0', 9600)
        time.sleep(2)

    rospy.Subscriber('r2d2/logic', String, handler)
    verbose('Subscribed to node "r2d2/logic" successfully.')

    pub = rospy.Publisher('r2d2/controller', String, queue_size=int(conf['queue_size']))
    verbose('Intialized "r2d2/controller"\'s publisher successfully.')

    # we print that we're ready
    time.sleep(2)

    verbose('r2d2/controller ready.')

if __name__ == '__main__':

    conf = yaml.load(open("../config/conf.yaml", 'r'))
    verbose('Loaded config successfully.')

    try:
        controller()
    except rospy.ROSInterruptException:
        pass