#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import wikipedia

global pub_tts

def wiki_search(data):
    pub_tts = rospy.Publisher('/text_to_speech', String, queue_size=1)



    info = wikipedia.summary(data.data)
    pub_tts.Publish("I got this " +info)

    
def wiki_search():
    rospy.init_node('wiki_search', anonymous=True)
    rospy.Subscriber("/wiki", String, wiki_search)
    rospy.spin()

if __name__ == '__main__':
    wiki_search()


    '''
    
    '''