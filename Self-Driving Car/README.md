# Self-Driving Car

The aim of this project is to ultimately move towards a centrally controlled AI traffic system. We are attempting to do this by using a single set of sensors whose data is shared between multiple cars, and their movements are determined accordingly. These sensors are part of the environment and not any car in particular. In autonomous driving parlance, we are looking at level 4 autonomy where cars can take care of most driving functionalities within a geo-locked location of shared sensor data. 

We begin our simulation with raspberry pi controlled toy cars and an external cellphone camera. Using [haar cascade](https://github.com/Sidc1991/Machine-Learning-Projects/tree/master/Computer%20Vision) we are able to detect the toy car in our environment. 

![object](https://github.com/Sidc1991/Machine-Learning-Projects/blob/master/Self-Driving%20Car/Trial%20Images/Object%20Detection.jpeg)

We next use the camera to determine distance between cars. So far, the ARuler app has worked exceptionally well in determining distance through just a camera. As we can see from the image below, the app creates a triangular mesh to understand the shape of surface it is being aimed at. It then produces an xyz co-ordinate axis to determine the orientation of the surface. Finally, it is ready to determine distance between the two objects.     

![distance](https://raw.githubusercontent.com/Sidc1991/Machine-Learning-Projects/master/Self-Driving%20Car/Trial%20Images/Object%20Detection.jpeg?token=Ats9XBIwmxwhcJFEzxC9LLRQGi024uQYks5ceCTZwA%3D%3D)


Unfortunately, this has to be done manually. Our next priority is to automatically combine the functionalities of object detection algorithm with distance detection app and find the accurate distance between the bounding boxes.  

