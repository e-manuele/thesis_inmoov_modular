#!/usr/bin/env python3
import rospy 
from std_msgs.msg import UInt16MultiArray
from std_msgs.msg import String
import time
import random
global user_choice
user_choice = ""

def update_value(data):   # CALLBACK PER OGNI FRAME DL VIDEO: AGGIORNA VALORE DITA IN CONTINUO
  global user_choice
  fingers_info =list( map(int, list(data.data.replace(',', '').replace(' ', ''))))
  #print("LISTA : ",fingers_info)
  rospy.loginfo("Receiving :")
  rospy.loginfo(fingers_info)
  scissor_hand= [0,1,1,0,0]
  rock_hand =[0,0,0,0,0]
  paper_hand= [1,1,1,1,1]

  if fingers_info ==rock_hand:
        user_choice = "rock" # sasso
  elif fingers_info == scissor_hand:
        user_choice = "scissor" #forbice
  elif fingers_info ==paper_hand:
        user_choice = "paper" #carta
  #print("USER CHOICE : "+ user_choice + " .")


def callback_init_game(stringa):  # CALLBACK SU init_game: FA INIZIARE IL GIOCO 
    say(stringa)
    #E PRENDE DALLA VAR user_choice AGGIORANTA DALLA CALLBACK PRIMA
    global user_choice    
    activate_hand_recognition()
    arduino_pub = rospy.Publisher('/hand_pos', UInt16MultiArray, queue_size=1)
    hand_pub = UInt16MultiArray() 
    game_list = ["rock","scissor","paper"]
    say("Start")
    time.sleep(1)
    say("One")
    time.sleep(1)
    say("Two")
    time.sleep(1)
    say("Three")
    time.sleep(1)
    say("Let me check")
    time.sleep(1)

    value = random.choice(game_list)# CREO LISTE PER INVIARE GLI ANGOLI

    
    if value == "rock":
       for x in range(0,5):
           hand_pub.data.insert(0,0)

    if value == "scissor":
       hand_pub.data.insert(0,0)
       for x in range(0,2):
           hand_pub.data.insert(0,180)
       for x in range(0,2):
           hand_pub.data.insert(0,0)

    if value == "paper":
       for x in range(0,5):
           hand_pub.data.insert(0,180)
      
    arduino_pub.publish(hand_pub)
    
    say("Ok")
    time.sleep(1)
    
    if value == user_choice :
      say("Draw, both "+ value+".")

    if (value == "rock") & (user_choice =="paper"):
      say("I choosed "+ value +". You choosed paper. You won!")

    if (value == "paper") & (user_choice =="scissor"):
      say("I choosed "+ value +". You choosed scissor. You won!")

    if (value == "scissor") & (user_choice =="rock"):
      say("I choosed "+ value +". You choosed rock. You won!")

    if (value == "paper") & (user_choice =="rock"):
      say("I choosed "+ value +". You choosed rock. You lost!")

    if (value == "scissor") & (user_choice =="paper"):
      say("I choosed "+ value +". You choosed paper. You lost!")
      
    if (value == "rock") & (user_choice =="scissor"):
      say("I choosed "+ value +". You choosed scissor. You lost!")

    if value =="":
      say("I can't see your hand")
    rospy.loginfo("Ho visto la mano in pos :" +user_choice)
    say("Game over!")  
    deactivate_hand_recognition()

def   activate_hand_recognition():
  pub_activator = rospy.Publisher('/hand_detector_ctrl', String, queue_size=1)
  pub_activator.publish("True")
  rospy.loginfo("Activate hand detector!")


def   deactivate_hand_recognition():
  pub_activator = rospy.Publisher('/hand_detector_ctrl', String, queue_size=1)
  pub_activator.publish("False")
  rospy.loginfo("Deactivate hand detector!")

def say(command):
  pub = rospy.Publisher('text_to_speech', String, queue_size=1)
  pub.publish(command)


def listen_to_start():
  rospy.init_node('rsp_game_py', anonymous=True)
  rospy.Subscriber('/fingers_info', String, update_value)
  rospy.Subscriber('/rsp_game', String, callback_init_game)
  rospy.spin()

if __name__ == '__main__':
  listen_to_start()


'''
roslaunch main rsp_launcher.launch
rostopic pub -1 rsp_game std_msgs/String "data: start game"
'''