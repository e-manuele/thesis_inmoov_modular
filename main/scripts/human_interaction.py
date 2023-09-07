#!/usr/bin/env python
'''
-Get the face box coords and save once the image
-Then check if is on databases (opening a file and iterating over the json.loads)
-If unknowned save the photo and ask for the name and compile the rest





files: .npy,.json

while person.detected() 
      1.start tracking face
      say hi


      2.recognise person:
      
      2.a look in his db
      2.b if not in db ask the name and other data



USA FACE COORD TRACKER for trtacke face 
USA FACE RECOGNITION PER CAPIRE IL NOME DELLA PERSONA CON CUI PARLA
QUINDI QUESTO é IL MANAGER DELLA HI

FACE RECOGNITION SU PYCHARM
'''

import rospy
from std_msgs.msg import String
#from std_msgs.msg import Image
from std_msgs.msg import UInt16
from std_msgs.msg import UInt16MultiArray

global known_human,found_human,pub_face_detector,pub_neck

found_human =False

def get_face_coord(data):
    global found_human,known_human
    if data.data.all()!=None: 
       found_human = True
    while found_human:   
       track_human(data.data)
       if not known_human:
          recognize_human() 

def recognize_human():
    pub_recognize_human = rospy.Publisher("/recognize_human_ctrl", String)
    pub_recognize_human.publish("True")

def track_human(data):
    global pub_neck
    x = data[0]
    center_x = 100
    x_angle  = UInt16()
    while 0<angle_x<180:  
        if x< center_x+30:
           angle_x +=7
        if x>center_x+30:
           angle_x -=7
        pub_neck.publish(angle_x)

def look_around_for_human():
    global pub_face_detector,found_human
    print("Muovo la testa a dx sx e se c'è human start track(?)")
    pub_face_detector.publish("True")
    while not found_human:
        if angle_x<=180:
            angle_x += 5
        if angle_x >= 0:
            angle_x -= 5
        pub_neck.publish(angle_x)
        

def init_interaction(data):
    look_around_for_human()

def init():
    global pub_face_detector,pub_neck
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/PIR", String, init_interaction)
    rospy.Subscriber("/face_coords", UInt16MultiArray, get_face_coord)
    pub_neck = rospy.Publisher("/neck_x_mov", String, queue_size=10)
    pub_face_detector = rospy.Publisher("/face_detector_ctrl", String,queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    init()        