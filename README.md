# Ros noetic description package for the onrobot 2fg7 gripper
------
## General info
This repository contains the URDF and meshes for the [OnRobot 2FG7 gripper](https://onrobot.com/en/products/2fg7).  
It also has a simple control implementation to be used with Gazebo simulator.  

The model was developed using the [Fusion 360 to URDF script](https://github.com/syuntoku14/fusion2urdf) and CAD files taken from the OnRobot official webpage.

## Installation and ussage:
1. Install dependencies (from source):
From source (if not already available in your ROS 2 distribution):
- [mimic joint fix plugin](https://github.com/roboticsgroup/roboticsgroup_upatras_gazebo_plugins) – ROS 2 fork or migration may be required.
- [gazebo_ros_pkgs](https://github.com/ros-simulation/gazebo_ros_pkgs) (for Gazebo integration).

  
2. Install this package:
```
bash
cd ~/ros2_ws/src
git clone https://github.com/juandpenan/onrobot_2FG7_gripper_description
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
```

3. Launch:

  * Display the gripper with RVIZ:
  ```
  ros2 launch onrobot_2FG7_gripper_description display_launch.py
  ```
  
  * Launch gazebo with controllers: 
  ```
  ros2 launch onrobot_2FG7_gripper_description gazebo_control_launch.py
  ```
