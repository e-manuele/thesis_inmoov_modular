#!/usr/bin/env python3
import rospy # Python library for ROS
from sensor_msgs.msg import Image # Image is the message type
from std_msgs.msg import String # Image is the message typ
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 
from cvzone.HandTrackingModule import HandDetector

global hand_data, hands,message,hand_detector,sub
hand_data={}
message=""
check =""

def get_hand_info(data):
  global hand_data, hands, hand_detector,check
  x= 0
  y = 0
  br = CvBridge()
  frame = br.imgmsg_to_cv2(data)
  image = cv2.flip(frame, 1)
  hands, image = hand_detector.findHands(image)
  rows, cols, _ = image.shape
  center_y = int(rows / 2)
  center_x = int(cols / 2)
  if hands:
    hand1 = hands[0]
    hand_data["lmList"] = hand1["lmList"]
    hand_data["bbox"] = hand1["bbox"]
    hand_data["centerPoint"] = hand1['center']
    hand_data["handType"] = hand1["type"]
    hand_data["fingers"] = hand_detector.fingersUp(hand1)
    x = hand_data["centerPoint"][0]
    y = hand_data["centerPoint"][1]  
  #image = cv2.circle(image, (x,y), radius=3, color=(0, 255, 0), thickness=1) 
  #image = cv2.circle(image, (center_x,center_y), radius=3, color=(0, 0, 255), thickness=1) 
  #cv2.imshow("camera",image)
  
  cv2.waitKey(1)
  if check == "False":
    #cv2.destroyAllWindows
    rospy.loginfo("Hand detector shutdown")


def timer_pub_data(event):
    global hand_data, hands, message
    if len(hand_data) != 0: 
        message = str(hand_data["fingers"]).replace('[', '').replace(']', '')
    pub = rospy.Publisher('/fingers_info', String, queue_size=1)
    rospy.loginfo("Sending:" + message)
    pub.publish(message)
    rospy.loginfo("fingers info :" +message)


def manager(data):
    global hand_detector,sub,check, timer
    check = data.data
    rospy.loginfo("Manager_hand ha ricevuto "+ data.data)
    if data.data == "True":
        hand_detector = HandDetector(detectionCon=0.8, maxHands=1)
        sub = rospy.Subscriber('video_frames', Image, get_hand_info)
        rospy.loginfo("Hand detector subscriber registered")
        timer = rospy.Timer(rospy.Duration(0.5), timer_pub_data)
    if data.data == "False":
        rospy.loginfo("Hand detector subscriber unregistered")
        sub.unregister()
        timer.shutdown()

def init():
    global detector
    rospy.init_node('hand_detector', anonymous=False)
    rospy.Subscriber("/hand_detector_ctrl", String, manager)
    rospy.spin()
    

if __name__ == '__main__':
    init()




'''
def receive_message():
  global detector
  rospy.init_node('hand_detector', anonymous=True)
  detector = HandDetector(detectionCon=0.8, maxHands=1)
  rospy.Subscriber('video_frames', Image, callback)
  pub = rospy.Publisher('/hand_info', String, queue_size=1000)
  timer = rospy.Timer(rospy.Duration(1), timer_callback)
  rospy.spin()
  cv2.destroyAllWindows()
  timer.shutdown()


rostopic pub -1 /hand_detector_ctrl std_msgs/String "data: True"


roslaunch hand_detector.launch
rostopic pub -1 /hand_detector_ctrl std_msgs/String "'True'"
rostopic pub -1 /hand_detector_ctrl std_msgs/String "'False'"
'''