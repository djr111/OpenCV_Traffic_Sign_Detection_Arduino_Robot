#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from time import sleep


def publisher():
        pub = rospy.Publisher('ROS_Topic', Float64, queue_size=10)
        rospy.init_node("Ros_Topic", anonymous = True)
        rate = rospy.Rate(1)

        value = 0

        ledList = [0.0,3.0,5.0,6.0,2.0,10.0]
        while not rospy.is_shutdown():

            for i in range(0, len(ledList)-1):
                value = ledList[i]

                pub.publish(value)                                                                 
                                
                rospy.loginfo("The Value =%s",value)

                rate.sleep()


if __name__ == "__main__":
    
    publisher()
