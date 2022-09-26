#!/usr/bin/env python
import sys
from student_pkg.srv import AddTwoInts 
from student_pkg.srv import AddTwoIntsResponse
from student_pkg.srv import AddTwoIntsRequest
import rospy

def addInts_Client(x,y):

    # Wait for service to start until server is awake
    # "Add_Two_Ints is the service name"

    rospy.wait_for_service('Add_Two_Ints')

    try:
        # Client creates a Servver Proxy imitating the server
        Server_Proxy = rospy.ServiceProxy('Add_Two_Ints', AddTwoInts)
        clientResponse = Server_Proxy(x,y)
        return clientResponse.total

    except rospy.ServiceException(e):
        print("The Service has failed : %s" %e)


def usage():
    return

if __name__ == '__main__':
    if len(sys.argv)== 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print("%s [x,y]" %sys.argv[0])
        sys.exit(1)
    print(" Requesting %s+%s" %(x,y))
    s = addInts_Client(x,y)
    print("%s +%s = %s" %(x,y,s))