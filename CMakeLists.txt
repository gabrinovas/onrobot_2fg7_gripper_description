cmake_minimum_required(VERSION 3.5)
project(onrobot_2fg7_description)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(robot_state_publisher REQUIRED)
find_package(xacro REQUIRED)
find_package(gazebo_ros REQUIRED)

# Include directories
include_directories(
  include
)

# Install URDF/Xacro files
install(DIRECTORY urdf launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
