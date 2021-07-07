#!/usr/bin/env python2

import rospy
from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import PoseStamped

class OdomToPath:
    def __init__(self):
      odom_topic = rospy.get_param('~odom_topic')
      self.frame_name = rospy.get_param('~frame_name')
      self.offset_x = rospy.get_param('~offset_x')
      self.offset_y = rospy.get_param('~offset_y')
      self.offset_z = rospy.get_param('~offset_z')
      output_path_topic = rospy.get_param('~output_path_topic')
      self.odom_sub = \
        rospy.Subscriber(odom_topic, Odometry, self.odom_cb, queue_size=10)
      self.path_pub = \
        rospy.Publisher(output_path_topic, Path, queue_size=10)
      self.path = Path()

    def odom_cb(self, msg):
        cur_pose = PoseStamped()
        cur_pose.header = msg.header
        cur_pose.pose = msg.pose.pose
        cur_pose.pose.position.x -= self.offset_x
        cur_pose.pose.position.y -= self.offset_y
        cur_pose.pose.position.z -= self.offset_z
        cur_pose.header.frame_id = self.frame_name
        self.path.header = msg.header
        self.path.poses.append(cur_pose)
        self.path_pub.publish(self.path)

if __name__ == '__main__':
    rospy.init_node('odom_to_path')
    odom_to_path = OdomToPath()
    rospy.spin()