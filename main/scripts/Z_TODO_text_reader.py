#!/usr/bin/env python3
import rospy # Python library for ROS
from sensor_msgs.msg import Image # Image is the message type
from std_msgs.msg import String # Image is the message typ
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 


global message
message=""

def callback(data):
  global message
  br = CvBridge()
  frame = br.imgmsg_to_cv2(data)
  image = cv2.flip(frame, 1)
  # read text from image save it on message var
  # if message var is empty say "I' cant read, put the paper under my sight"
  
  

def receive_message():
  global detector
  rospy.init_node('test_reader', anonymous=True)
  rospy.Subscriber('video_frames', Image, callback)
  pub = rospy.Publisher('/text_red', String, queue_size=10)
  rospy.spin()
  cv2.destroyAllWindows()

if __name__ == '__main__':
  receive_message()
