#include <ros/ros.h>
#include <openni_camera/openni_node.h>

int main(int argc, char** argv)
{
  ros::init(argc, argv, "openni_driver");

  openni_camera::OpenniNode node;
  node.initialize();

  // Manager service calls are on global callback queue
  ros::spin();
}
