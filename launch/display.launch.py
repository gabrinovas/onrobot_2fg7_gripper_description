# launch/display_launch.py
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_share = get_package_share_directory('onrobot_2FG7_gripper_description')

    default_model_path = os.path.join(pkg_share, 'urdf', 'onrobot_2fg7_upload.xacro')
    default_rviz_config_path = os.path.join(pkg_share, 'launch', 'urdf.rviz')

    return LaunchDescription([
        DeclareLaunchArgument(name='model', default_value=default_model_path,
                              description='Absolute path to robot urdf file'),
        DeclareLaunchArgument(name='rvizconfig', default_value=default_rviz_config_path,
                              description='Absolute path to rviz config file'),

        Node(
            package='xacro',
            executable='xacro',
            arguments=[LaunchConfiguration('model')],
            output='screen'
        ),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'use_sim_time': True}],
            output='screen'
        ),

        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui'
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', LaunchConfiguration('rvizconfig')],
            output='screen'
        )
    ])
