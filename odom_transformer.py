import rospy
import tf
from geometry_msgs.msg import PoseStamped

class pose_transformer():
  def callback_odm(self,pose_msg : PoseStamped):
    try:
      transformed_pose = self.listener.transformPose('/global_map', pose_msg)
      self.odm_tf_pub.publish(transformed_pose) 
    except(tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
      print('tf_error,can not find transform from /global_map to %s'%(pose_msg.header.frame_id))

  def __init__(self,robot_id) -> None:
      self.odom_sub = rospy.Subscriber('/robot_'+str(robot_id)+'/Odometry', PoseStamped, self.callback_odm)
      self.odm_tf_pub = rospy.Publisher('/robot_'+str(robot_id)+'/Odometry_tf', PoseStamped, queue_size=5)
      self.listener = tf.TransformListener()

if __name__ == '__main__':
    rospy.init_node('pose_transformer')
    robot_id = 0
    transformer = pose_transformer(robot_id)
    rospy.spin()
   