#!/usr/bin/env python2

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseWithCovarianceStamped


class OdomToPose:
    def __init__(self):
        odom_topic = rospy.get_param('~odom_topic')
        self.frame_name = rospy.get_param('~frame_name')
        self.offset_x = rospy.get_param('~offset_x')
        self.offset_y = rospy.get_param('~offset_y')
        self.offset_z = rospy.get_param('~offset_z')
        output_pose_topic = rospy.get_param('~output_pose_topic')
        self.odom_sub = \
            rospy.Subscriber(odom_topic, Odometry, self.odom_cb, queue_size=10)
        self.pose_pub = \
            rospy.Publisher(
                output_pose_topic, PoseWithCovarianceStamped, queue_size=10)

    def odom_cb(self, msg):
        cur_pose = PoseWithCovarianceStamped()
        cur_pose.header = msg.header
        cur_pose.header.frame_id = self.frame_name
        cur_pose.pose.covariance = msg.pose.covariance
        cur_pose.pose.pose.position = msg.pose.pose.position
        cur_pose.pose.pose.orientation = msg.pose.pose.orientation
        cur_pose.pose.pose.position.x -= self.offset_x
        cur_pose.pose.pose.position.y -= self.offset_y
        cur_pose.pose.pose.position.z -= self.offset_z
        self.pose_pub.publish(cur_pose)


if __name__ == '__main__':
    rospy.init_node('odom_to_pose')
    odom_to_pose = OdomToPose()
    rospy.spin()