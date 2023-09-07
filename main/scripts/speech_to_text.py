#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
import speech_recognition as sr

def listen_and_pub():
    pub = rospy.Publisher('/speech_to_text', String, queue_size=10)
    rospy.init_node('speech_to_text', anonymous=True)
    while not rospy.is_shutdown():
        rate = rospy.Rate(10)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak:")
            audio = r.listen(source)
            print("Stop talking")
        try:
            text = r.recognize_google(audio)
            pub.publish(text)
        except:
            text=""
        rate.sleep()
if __name__ == '__main__':
    listen_and_pub()
