#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import UInt16MultiArray

def talker():
    pub = rospy.Publisher('/servo', UInt16MultiArray, queue_size=1)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        angle = UInt16MultiArray() 
        angle.data.insert(0,0)
        angle.data.insert(0,0)
        angle_fingers = input('Scrivi   FINGERS : 2(thumb) to 7(wrist) : \n ') 
        angle_bicep = input('Scrivi   BICEP: 8(bicep) to 9(rotate) : \n')
        angle_shoulder = input('Scrivi   SHOULDER: 10(shoulder) to 11(rotate) : \n')
        angle_neck= input('Scrivi   NECK: 12(y) to 13(x) : \n')
        for empty in range(0,11):
           angle.data.insert(0,0)
        angle_mouth = input('Scrivi   MOUTH 26: \n')
        angle_pre = angle_fingers+ ' '+angle_bicep+ ' '+angle_shoulder+ ' '+angle_neck + ' '+angle_mouth
        angle_pre = angle_pre.split(' ')[::-1] 
        for x in angle_pre:
            x = int(x)
            angle.data.insert(0,x)
        '''
        angle.data.insert(0,0)
        angle.data.insert(1,0)
        angle.data.insert(2,0)
        angle.data.insert(3,0)
        angle.data.insert(4,0)
        angle.data.insert(5,0)
        angle.data.insert(6,0)
        angle.data.insert(7,0)
        angle.data.insert(8,0)
        angle.data.insert(9,0)
        angle.data.insert(10,0)
        angle.data.insert(11,40)
        angle.data.insert(12,0)
        angle.data.insert(13,0)
        angle.data.insert(14,0)
        angle.data.insert(15,0)
        angle.data.insert(16,0)
        angle.data.insert(17,0)
        angle.data.insert(18,0)
        angle.data.insert(19,0)
        angle.data.insert(20,0)
        angle.data.insert(21,0)
        angle.data.insert(22,0)
        angle.data.insert(23,0)
        angle.data.insert(24,0)
        angle.data.insert(25,0)
        angle.data.insert(26,0)
        '''

        pub.publish(angle)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass