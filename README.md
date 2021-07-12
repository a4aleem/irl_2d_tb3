
# Turtlebot3

## Getting Started:

### Prerequisites:

   The build is only yet tested on ROS melodic but it may work on other distributions as well.

Install:

  Make a catkin workspace:

    mkdir -p ~/catkin_ws/src

  Clone the repository to your workspace:
  
    cd ~/catkin_ws/src
    git clone https://github.com/a4aleem/irl_2d_tb3 

  Install project dependencies using rosdep:

    cd ~/catkin_ws
    rosdep install --from-paths src --ignore-src -r -y

  Build and source the workspace:

    cd ~/catkin_ws
    catkin_make
    source ~/catkin_ws/devel/setup.bash

  Launch:

    roslaunch irl_2d_tb3_gazebo turtlebot3_world.launch


## Turtlebot3 based SLAM and NAV:

### Terminal#1

    cd catkin_ws/
    source devel/setup.bash
    roslaunch irl_2d_tb3_gazebo turtlebot3_irllab.launch 

### Terminal#2
    
    cd catkin_ws/
    source devel/setup.bash
    roslaunch irl_2d_tb3_navigation turtlebot3_map_nav.launch 


## Frontier based Exploration on Turtlebot3

### TERMINAL#1

    cd catkin_ws/
    source devel/setup.bash
    roslaunch irl_2d_tb3_gazebo turtlebot3_irllab.launch

## TERMINAL#2

    cd catkin_ws/
    source devel/setup.bash
    roslaunch irl_2d_tb3_autonomous_exploration turtlebot3_exploration.launch 


## Multi Turtlebot3 Navigation
 ### TERMINAL#1
 
    cd catkin_ws/
    rsource devel/setup.bash
    roslaunch irl_2d_tb3_gazebo multi_turtlebot3_irl.launch 

### TERMINAL#2
    
    cd catkin_ws/
    source devel/setup.bash
    roslaunch irl_2d_tb3_navigation multi_turtlebot3_irl_nav.launch


 
