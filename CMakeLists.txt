cmake_minimum_required(VERSION 3.5)
project(onrobot_2fg7_gripper_description)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(robot_state_publisher REQUIRED)
find_package(xacro REQUIRED)
find_package(urdf REQUIRED)
find_package(gazebo_ros REQUIRED)

# Install files from the launch, meshes, and urdf directories
install(
  DIRECTORY
    launch
    meshes
    urdf
  DESTINATION
    share/${PROJECT_NAME}
)

ament_package()