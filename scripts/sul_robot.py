#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
x1= 0
x2= 0
x3= 0

def sul_move():

    global x1,x2,x3
    publisher = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('joint_state_publisher', anonymous=True)
    rate = rospy.Rate(20) 
    joints = JointState()
    joints.header = Header()
    joints.header.stamp = rospy.Time.now()
    joints.name = ['j1', 'j3','j4']
    joints.position = [ 0, 0, 0]
    
    while not rospy.is_shutdown():
        joints.header.stamp = rospy.Time.now()
        if  x1 == 0 :
            joints.position[0] -= 0.05
            if joints.position[0] < -1.57: 
                x1 = 1
        elif  x1 == 1  :
            joints.position[0] += 0.05
            if joints.position[0] >= 1:
                x1 = 0
        if  x2 == 0 and x1==0 :
            joints.position[1] -= 0.01
            if joints.position[1] <  -0.5:
                x2 = 1
        elif x2 == 1 and x1==1  :
            joints.position[1] += 0.01
            if joints.position[1] > 0:
                x2 = 0

        if  x3 == 0 and x1==0 :
            joints.position[2] -= 0.1
            if joints.position[2] < 1.55:
                x3 = 1
        elif x3 == 1 and x1==1 :
            joints.position[2] += 0.1
            if joints.position[2] >= 3.14:
                x3 = 0


       

        publisher.publish(joints)
        rate.sleep()
	
if __name__ == '__main__':
    try:
        sul_move()
    except rospy.ROSInterruptException:
        pass