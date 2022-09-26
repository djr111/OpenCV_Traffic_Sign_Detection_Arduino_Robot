#!/usr/bin/env python

from student_pkg.srv import AddTwoInts 
from student_pkg.srv import AddTwoIntsResponse
from student_pkg.srv import AddTwoIntsRequest
import rospy


# The CallBack_addTwoInts execute the request from client
def CallBack_addTwoInts(req):
    print("Here is your request : [%s + %s = %s]" %(req.firstnumber,
    req.secondnumber, (req.firstnumber+ req.secondnumber)))
    return AddTwoIntsResponse(req.firstnumber + req.secondnumber)

# Creating the service

def addInts_Server():
    rospy.init_node('addInts_Server')

# Create a service object from the Service Class, with 3 arguments
# Arugments 1. Service Name, 2. Service Type, 3. callback function

    s = rospy.Service('Add_Two_Ints', AddTwoInts, CallBack_addTwoInts)

    print("The Server is waiting to process requests")

    # starts the service and waits for requests
    rospy.spin()


if __name__ == "__main__":
    addInts_Server()

