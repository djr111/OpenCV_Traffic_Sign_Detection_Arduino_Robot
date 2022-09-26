#!/usr/bin/env python
import rospy

from student_pkg.msg import two_ints
from std_msgs.msg import Int16

# Create object to be published

result = Int16()

# Function to do the calculations
def callback(msg):
    result.data = msg.a + msg.b

    # Log the result with ros
    rospy.loginfo(result)


def main():
    rospy.init_node("two_ints_subscriber")
    # Publish to sum Topic
    pub = rospy.Publisher("sum", Int16, queue_size=1)
    
    # subscribe to two_ints Topic
    # Sub receives msgs and pass to callback function
    sub = rospy.Subscriber("two_ints", two_ints, callback)
    r = rospy.Rate(1)

    while not rospy.is_shutdown():
        pub.publish(result )
        r.sleep()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass


