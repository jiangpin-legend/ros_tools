import rospy
import tf
from geometry_msgs.msg import PoseStamped,TransformStamped

class tf_republisher():
  def callback_tf(self,tf_msg : PoseStamped):
    for tfmessage in tf_msg.transforms:
        self.tf_broadcaster.sendTransform(tfmessage)

  def __init__(self) -> None:
      self.tf_sub = rospy.Subscriber('/tf2', PoseStamped, self.callback_tf)
      self.tf_broadcaster = tf.TransformBroadcaster()
      # self.listener = tf.TransformListener()

if __name__ == '__main__':
    rospy.init_node('tf_republisher')
    transformer = tf_republisher()
    rospy.spin()
   