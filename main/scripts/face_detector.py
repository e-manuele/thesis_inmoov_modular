#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from cvzone.PoseModule import PoseDetector
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from std_msgs.msg import UInt16MultiArray

global face_sub,pose_detector,x,y
x=0
y=0

def get_face_coords(data):
    global pose_detector,face_coords,x,y
    br = CvBridge()
    frame = br.imgmsg_to_cv2(data)
    image = cv2.flip(frame, 1)
    img = pose_detector.findPose(image)
    lmList, bboxInfo = pose_detector.findPosition(img, bboxWithHands=False)
    if bboxInfo:
        center = bboxInfo["center"]
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
        x = lmList[0][1]
        y = lmList[0][2]
        #print("x=" +str(x)+ " y= "+str(y))
    # qua riconosco la posizione del volto e continuo il tracker pubblicando su face coords
    face_coords = UInt16MultiArray()
    face_coords.data=[]
    face_coords.data.insert(0,[x,y])
    rospy.loginfo(face_coords.data)
    '''
    if good_face_position(lmList[7],lmList[8]):  #TODO
        #print("Salvo l'immagine che ho come foto di volto da riconoscere...")
        rospy.loginfo("Dato che l volto è ben visibile dovrei attivare una funzione esterna che salva l'immagine")

def good_face_position(sette,otto):  #TODO confronto tra grandezza faccia e dimensione cam(?)
    #print("Face coords")# es distanza 8-7(orecchie)
    return True
'''
def timer_pub_data(event):
    global face_coords
    if len(face_coords) != 0: 
        message = face_coords
    pub_face_coords = rospy.Publisher("/face_coords", UInt16MultiArray)
    pub_face_coords.publish(message)

def manager(data):
    global face_sub,pose_detector
    if data.data == "True":
        pose_detector = PoseDetector()
        face_sub =rospy.Subscriber('video_frames', Image, get_face_coords)
        rospy.loginfo("Face detector subscriber registered")
        timer =rospy.Timer(rospy.Duration(0.5), timer_pub_data)
    if data.data == "False":
        rospy.loginfo("Face detector subscriber unregister")
        face_sub.unregister()
        timer.stop()

def init():
    rospy.init_node('face_detector', anonymous=True)
    rospy.Subscriber("/face_detector_ctrl", String, manager)
    rospy.spin()

if __name__ == '__main__':
    init()



'''   
roslaunch face_detector.launch
rostopic pub -1 /face_detector_ctrl std_msgs/String "'True'"
rostopic pub -1 /face_detector_ctrl std_msgs/String "'False'"
'''