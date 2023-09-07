#!/usr/bin/env python
import pyttsx3
import rospy
from std_msgs.msg import String
'''
pub = rospy.Publisher('/servo', UInt16, queue_size=10)



def onStart(name, location, length):
    pub = rospy.Publisher('/servo', UInt16, queue_size=10)
    pub.publish(0)
    
    
def onEnd():
  pub = rospy.Publisher('/servo', UInt16, queue_size=10)
  pub.publish(90)

'''


def callback(data):
    engine = pyttsx3.init()
    #engine.connect('started-utterance', onStart)
    #engine.connect('finished-utterance', onEnd)
    rospy.loginfo(data.data)
    engine.say(data.data)
    engine.runAndWait()

def listener():
    rospy.init_node('text_to_speech', anonymous=True)
    rospy.Subscriber("/text_to_speech", String, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()
