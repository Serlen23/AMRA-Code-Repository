#!/bin/bash

px4_dir=~/Firmware

echo " __  __  _  _  ___  ____  _  _  _  _    __    ____  __    ____   
(  )(  )( \( )/ __)(_  _)( \( )( )/ )  /__\  (  _ \(  )  ( ___)  
 )(__)(  )  ( \__ \ _)(_  )  (  )  (  /(__)\  ) _ < )(__  )__)   
(______)(_)\_)(___/(____)(_)\_)(_)\_)(__)(__)(____/(____)(____)  "

source $px4_dir/Tools/setup_gazebo.bash $px4_dir $px4_dir/build/posix_sitl_default

export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$px4_dir
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$px4_dir/Tools/sitl_gazebo
