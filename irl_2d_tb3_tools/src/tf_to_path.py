#!/usr/bin/env python2

import rospy
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
import tf

class TfToPath:
    def __init__(self):
      self.from_frame = rospy.get_param('~from_frame')
      self.to_frame = rospy.get_param('~to_frame')
      self.listener = tf.TransformListener()
      self.path_pub = \
        rospy.Publisher('tf_{}_{}'.format(self.from_frame, self.to_frame), Path, queue_size=10)
      self.path = Path()

    def run(self):
        try:
            (trans, rot) = self.listener.lookupTransform(self.from_frame, self.to_frame, rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            return
        cur_pose = PoseStamped()
        cur_pose.header.stamp = rospy.Time.now()
        cur_pose.pose.position.x = trans[0]
        cur_pose.pose.position.y = trans[1]
        cur_pose.pose.position.z = trans[2]
        cur_pose.pose.orientation.x = rot[0]
        cur_pose.pose.orientation.y = rot[1]
        cur_pose.pose.orientation.z = rot[2]
        cur_pose.pose.orientation.w = rot[3]
        self.path.header = cur_pose.header
        self.path.header.frame_id = self.from_frame
        self.path.poses.append(cur_pose)
        self.path_pub.publish(self.path)

if __name__ == '__main__':
    rospy.init_node('tf_to_path')
    tf_to_path = TfToPath()
    while not rospy.is_shutdown():
        tf_to_path.run()
    rospy.spin()