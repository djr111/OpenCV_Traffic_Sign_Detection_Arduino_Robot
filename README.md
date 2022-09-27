# Advanced robot navigation and pathplanning ( Assignment 2 in Computer science and robotic engineering)

<b />Task required previously designed Arduino robot to recognise traffic signs on the camera and perform movement either on left or right  
<b />For this purpose advanced machine learning algorithms were used to train neural network to clasify and valide traffic signs  
<b />Trained model was integrated in python script with OpenCV to process required task on live camera  
<b />Script was integrated in Robotic Operating System (ROS) as mainframe development and communication platform of the Arduino designed robot  

<b />Video presentation of performance with description can be reviewed with link below:  

<b />https://drive.google.com/drive/folders/1VLR-XyFgT5LPZoJVJFnIOW50bDpxL9nQ?usp=sharing

<b />More detailed description can be reviewed in Assignment2...docx file

<b />    Part  1 - Neural network, python and OpenCV <b />
<b />
  
<b />    Initially core component of neural network was to provide relevant dataset for high accuracy results  
<b />    For this purpose German Traffic Sign Recognition Benchmark (GTSRB) were selected containing 35000 images  
<b />    of road signs within 44 classes -  
https://benchmark.ini.rub.de  

<b />    Code was developed in python 3.6.2 version with essential libraries as OpenCV,Sklearn,Tensorflow and others  
<b />    Full requirements and in depth explanation can be reviewed on  
https://www.computervision.zone/courses/traffic-sign-classification/    

<b />    Values provided in my script (pithontrain.py) have 98% stable performance in classification and validation, however it was 30min training process on powerfull desktop station  
![image](https://user-images.githubusercontent.com/58305266/192403694-90d246c9-25e1-4feb-a8a5-7d6e6b104ce6.png)

<b />    I was using TensorFlow "save" function in my solution as pickle library was depricated on python3 versions and higher to  
<b />    generate file model.5h
<b />    This file contains attributes and values from neural network training results in binary form and used to seperate OpenCV script from training one  
Since running training part each time using the camera would be ineffective  
  
traffictest.py is the main script used with USB camera and OpenCV library. Previously generated model.5h is being loaded and used for validation and classification of the road sign image on the camera

![image](https://user-images.githubusercontent.com/58305266/192403330-05a1cba6-59bb-40c1-845b-7326b2c8a6e3.png)

Part 2 - Linux, ROS and Arduino  
  
