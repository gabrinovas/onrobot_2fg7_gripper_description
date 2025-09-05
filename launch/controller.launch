# launch/controller_launch.py
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Cargar parámetros del YAML en controller_manager
        Node(
            package="controller_manager",
            executable="ros2_control_node",
            parameters=["config/controller.yaml"],
            output="screen"
        ),

        # Spawner del joint state broadcaster
        Node(
            package="controller_manager",
            executable="spawner",
            arguments=["joint_state_broadcaster"],
            output="screen"
        ),

        # Spawner del controlador del dedo
        Node(
            package="controller_manager",
            executable="spawner",
            arguments=["left_finger_controller"],
            output="screen"
        ),

        # Robot State Publisher
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            output="screen",
            parameters=[{"use_sim_time": True}]
        )
    ])
