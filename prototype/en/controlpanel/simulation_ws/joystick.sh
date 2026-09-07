#!/bin/bash
source /opt/ros/kinetic/setup.sh
source /usr/share/gazebo/setup.sh
source /var/www/html/husky/prototype1/en/controlpanel/simulation_ws/devel/setup.sh
export HUSKY_GAZEBO_DESCRIPTION=/opt/ros/kinetic/share/husky_gazebo/urdf/descri$
export ROS_DISTRO="kinetic"
export ROS_ETC_DIR="/opt/ros/kinetic/etc/ros"
export ROS_MASTER_URI="http://localhost:11311"
export ROS_PACKAGE_PATH="/var/www/html/husky/prototype1/en/controlpanel/simulation_ws/src:/opt/ros/kinetic/share"
export ROS_PYTHON_VERSION="2"
export ROS_ROOT="/opt/ros/kinetic/share/ros"
export ROS_VERSION="1"
roslaunch robot_gui_bridge websocket.launch
