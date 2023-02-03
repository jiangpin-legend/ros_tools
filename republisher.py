#! /usr/bin/env python
import sys
import rospy
from  sensor_msgs.msg import PointCloud2



class msg_republisher():  
  def callback_pcd(self,ros_pcd : PointCloud2):
    msg = PointCloud2
    msg.header.timestamp = rospy.Time.now()
    self.pcd_publisher.publish(msg)
    
  def __init__(self,config,robot_id,isMaster = False) -> None:
      self.pcd_kf_sub = rospy.Subscriber('/robot_'+str(robot_id)+'/keyframe_pcd', PointCloud2, self.callback_pcd)
      self.pcd_publisher = rospy.Publisher('/pointcloud_repub', PointCloud2, queue_size=5)


            


if __name__ == '__main__':
    rospy.init_node('pointcloud_republisher')
    print('starting node')
    repulisher =msg_republisher()
    rate = rospy.Rate(10.0)
    rospy.spin() 