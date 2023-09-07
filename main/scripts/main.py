#!/usr/bin/env python
import rospy
from std_msgs.msg import String
#import time
global pub_tts

def language_understand(data):
    if(str(data).__contains__("play")):      #RSP_GAME
        pub_rsp= rospy.Publisher('/rsp_game', String, queue_size=10)
        pub_rsp.publish("So let's play!")

    if(str(data).__contains__("read")):      #READER
        pub_read= rospy.Publisher('/reader', String, queue_size=10)
        pub_read.publish("Let me see!")
        
    if(str(data).__contains__("wikipedia")):  #WIKIPEDIA
        pub_wiki= rospy.Publisher('/wiki', String, queue_size=10)
        pub_wiki.publish(data)


def interaction_human(data):
    pub_tts("Hi human!")
    pub_human_interaction = rospy.Publisher('/human_interaction', String, queue_size=10)
    pub_human_interaction.publish("Initialization pose detector to find face")




def init():
    rospy.init_node('listener', anonymous=False)
    pub_tts = rospy.Publisher('/text_to_speech', String, queue_size=1)
    rospy.Subscriber("/speech_to_text", String, language_understand)
    rospy.Subscriber("/PIR_activated", String, interaction_human)
    pub_tts.publish("I'm awake!")
    rospy.spin()

if __name__ == '__main__':
    init()