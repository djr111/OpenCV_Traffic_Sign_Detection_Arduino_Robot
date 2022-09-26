#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from time import sleep

# Create object to be published

result = Float64()

# Function to do the calculations
def callback(msg):
    result.data = msg

    # Log the result with ros
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", msg.data)


def main():
    rospy.init_node("Arduino_Topic", anonymous=True)     
 
    sub = rospy.Subscriber("Arduino_Topic", Float64, callback)
    r = rospy.Rate(1)

    rospy.spin()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass


