# auto_docking
QR code + docking
# PACKAGES INSTALLATION 
```
 $ sudo apt install ros-melodic-visp
```
# BUILD 

```
$ mkdir -p ~/catkin_ws/src

$ cd catkin_ws/src   

$ git clone https://github.com/Jenifen/auto_docking.git

$ cd ..

$ catkin_make  

$ source devel/setup.bash
 
```
# MINI-LAB GAZEBO LAUNCH
```
$  roslaunch minilab_demo_simulation minilab_demo_teleop.launch
 
```
![1](https://user-images.githubusercontent.com/85931327/123406021-5d336680-d5a2-11eb-9d79-6e0e32c5b61a.png)

![1](https://user-images.githubusercontent.com/85931327/123717020-df0de300-d873-11eb-9b58-850d4a102317.png)


# MINI-LAB TRACKING QR LAUNCH
```
$  roslaunch tracking_qr_code visual-servo-minilab.launch 

```

![2](https://user-images.githubusercontent.com/85931327/123717043-ed5bff00-d873-11eb-939c-a805b234cdf8.png)


![3](https://user-images.githubusercontent.com/85931327/123717056-f1881c80-d873-11eb-9fa3-f4e2d9d12448.png)


# MINI-LAB QR DECODE
```
$  rostopic echo /visp_auto_tracker/code_message 

```
![6](https://user-images.githubusercontent.com/85931327/124024491-2ec0eb80-d9e7-11eb-86a1-210365f57555.png)



