from setuptools import find_packages, setup

package_name = 'onrobot_2fg7_gripper_description'

setup(
    name=package_name,
    version='1.0.0',  # Match your package.xml version
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Add these to ensure all files are installed:
        ('share/' + package_name, ['setup.cfg']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gabri',
    maintainer_email='gabri@todo.todo',
    description='URDF description and meshes for OnRobot 2FG7 gripper',  # Updated description
    license='Apache-2.0',  # Match your license
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)