#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from time import sleep


def publisher():
        msg = String()

        pub = rospy.Publisher('Blink_Topic', String, queue_size=10)
        rospy.init_node("Blink_Test", anonymous = True)

        rate = rospy.Rate(1)

        while not rospy.is_shutdown():
               
                userInput = input("Off = 0, On = 1:- Enter Choice:")
                msg.data = str(userInput)

                print("Connecting to Subscriber.....")  
                print("=============================")                       

                pub.publish(msg)                                                                 
                                
                rospy.loginfo("I received: %s"%msg)

                rate.sleep()


if __name__ == "__main__":
    
    publisher()
