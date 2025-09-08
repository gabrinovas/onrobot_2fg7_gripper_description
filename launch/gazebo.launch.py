# launch/gazebo_launch.py
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_share = get_package_share_directory('onrobot_2FG7_gripper_description')
    gazebo_ros_share = get_package_share_directory('gazebo_ros')

    # Path al URDF/Xacro
    urdf_file = os.path.join(pkg_share, 'urdf', 'onrobot_2fg7_upload.xacro')

    return LaunchDescription([
        # Lanzar Gazebo vacío
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(gazebo_ros_share, 'launch', 'gazebo.launch.py')
            ),
            launch_arguments={'pause': 'false', 'use_sim_time': 'true'}.items(),
        ),

        # Spawner para el robot
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-file', urdf_file, '-entity', '2FG7_outwards'],
            output='screen'
        )
    ])
