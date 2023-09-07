#!/usr/bin/env python
import rospy
from std_msgs.msg import String
global sub


def get_data(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard 2 %s", data.data)
   

def manager(data):
    global sub
    if data.data == "True":
        sub =   rospy.Subscriber("chatter", String, get_data)# Image analizer and eventual publisher of data on topic
    if data.data == "False":
        sub.unregister()

 
def init():
    rospy.init_node('manager', anonymous=False)
    rospy.Subscriber("command", String, manager)
    rospy.spin()

if __name__ == '__main__':
    init()