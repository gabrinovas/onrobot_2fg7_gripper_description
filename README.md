# OnRobot 2FG7 Gripper Description for ROS2

URDF description and meshes for the OnRobot 2FG7 gripper, compatible with ROS2 Humble.

## Features

- Complete URDF model with accurate geometry
- High-quality mesh files
- RViz configuration for visualization
- ROS2 Humble compatibility

## Installation

### Prerequisites
- ROS2 Humble ([installation guide](https://docs.ros.org/en/humble/Installation.html))
- Colcon build system: `sudo apt install python3-colcon-common-extensions`

### Build Instructions

1. **Create a ROS2 workspace** (if you don't have one):
```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
```
  
2. Clone this repository:
```
git clone https://github.com/gabrinovas/onrobot_2fg7_gripper_description.git
```

3. Build the package:

```
cd ~/ros2_ws
colcon build --packages-select onrobot_2fg7_gripper_description
```

4. Source the workspace:
```
source ~/ros2_ws/install/setup.bash
```
