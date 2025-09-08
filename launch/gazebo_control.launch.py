# launch/gazebo_control_launch.py
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_share = get_package_share_directory('onrobot_2FG7_gripper_description')

    gazebo_launch = os.path.join(
        get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py'
    )

    return LaunchDescription([
        # Lanzar Gazebo vacío
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(gazebo_launch),
            launch_arguments={'verbose': 'true'}.items(),
        ),

        # Spawner del robot en Gazebo
        Node(
            package="gazebo_ros",
            executable="spawn_entity.py",
            arguments=["-topic", "robot_description", "-entity", "2FG7_outwards"],
            output="screen"
        ),

        # Nodo de control (ros2_control_node con el YAML de controladores)
        Node(
            package="controller_manager",
            executable="ros2_control_node",
            parameters=[os.path.join(pkg_share, 'config', 'controller.yaml')],
            output="screen"
        ),

        Node(
            package="controller_manager",
            executable="spawner",
            arguments=["joint_state_broadcaster"],
            output="screen"
        ),

        Node(
            package="controller_manager",
            executable="spawner",
            arguments=["left_finger_controller"],
            output="screen"
        )
    ])
