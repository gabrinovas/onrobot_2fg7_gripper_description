cmake_minimum_required(VERSION 3.8)
project(onrobot_2fg7_gripper_description)

# Find dependencies
find_package(ament_cmake REQUIRED)

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