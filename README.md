# Crane-Load-Zone-Monitoring 🏗️👷‍♂️
This repository contains files and models for drone video communication, image analysis, object detection, object tracking and depth estimation to be used in crane load zone monitoring.<br>
The approach is to target the crane lift zone from the video feed to ensure safety and efficiency while the load is being carried. The major accidents that occur in the scenario of a crane carrying a load are:<br>
  <b>🚧Overloading</b><br> Overloading stands out as a prevalent factor in crane accidents, occurring when operators surpass the designated weight capacity of the equipment.<br><br>
  <b>🚧Dropped Load</b><br> Dropped load incidents often occur when a load exceeds weight limits, is improperly secured, or becomes unbalanced during lifting operations.<br><br>
  <b>🚧Transportation Incidents</b><br> These accidents can occur when a vehicle collides with a crane during transportation or when the crane operator unintentionally runs the machine into a structure, person, vehicle, piece of equipment, or other obstacles. Such incidents highlight the importance of careful manoeuvring and vigilant operation during the transportation of cranes.<br><br>
  <b>🚧Crane Workers’ Fall Hazards</b><br> Such incidents occur when operators fall from a crane to a lower level, with scenarios including maintenance work on a hoist or crane or unloading materials from an overhead crane. Preventive measures, such as the use of appropriate safety equipment and heightened awareness during tasks performed at elevated heights, are critical to averting accidents involving operators falling from cranes.<br><br>
  <b>🚧Crane Striking Incidents</b><br> Being struck by the load, boom, or jib represents a significant risk factor in common crane accidents, often leading to serious injuries for workers involved in crane operations.<br><br>
</ol>

These accidents can be avoided with a heightened level of situational awareness.




To identify critical objects like construction vehicles, workers, obstacles and other hazards while the load is being carried, we have used a couple of object detection models. In order to understand the relative position of the load being carried and nearby workers, we have used depth estimation, trajectory prediction and Multi-Object Tracking (MOT) algorithms. 
### 📍Drone to PC video live streaming
For live video streaming between drone and end device like a PC, Gstreamer 1.24.12 is used.<br>
<ol>
  <li>drone.py: Python implementation with gstreamer pipeline to send video feed to a PC</li>
  <li>PC_receiver.py: Python implementation with gstreamer pipeline to receive video feed from a drone with the help of PC ip address and Port No.</li>
</ol>

### 📍Depth Estimation
We have implemented image processing, person and load identification models to calculate the relative postions of the load being carried and workers. If the worker is close to the load, the image is highlighted in red. Otherwise it is highlighted in green if the worker is at a safe distance.

| Case 1 | Case 2 |
|---------|---------|
| ![](https://github.com/Parth-D3/Crane-Load-Zone-Monitoring/blob/main/output_images/mot1.png) | ![](https://github.com/Parth-D3/Crane-Load-Zone-Monitoring/blob/main/output_images/mot2.png) |

### 📍Image Segmentation
To identify the load and danger zones (red, yellow, green), image segmentation is used to highlight the load and blur out the surroundings.

![](https://github.com/Parth-D3/Crane-Load-Zone-Monitoring/blob/main/output_images/img_seg1.png)
![](https://github.com/Parth-D3/Crane-Load-Zone-Monitoring/blob/main/output_images/img_seg2.png)

### 📍Object Detection
Various object detection models are used to detect entities in the load/lift zone.
<br>
<b>Vehicle Detection: </b> Detect all type of construction vehicles nearby the crane and load being carried.
![](https://github.com/Parth-D3/Crane-Load-Zone-Monitoring/blob/main/output_images/crane3.png)

<b>Person Detection: </b> Detect workers near the drone, crane and load being carried. <br>
![](https://github.com/Parth-D3/Crane-Load-Zone-Monitoring/blob/main/output_images/person1.jpg)
![](https://github.com/Parth-D3/Crane-Load-Zone-Monitoring/blob/main/output_images/person2.jpg)

<b>Fire Detection: </b> Detect fires in case of accidents near the crane to alert the crane operator and other personnel<br>
| Input | Output |
|---------|---------|
| ![](https://github.com/Parth-D3/Crane-Load-Zone-Monitoring/blob/main/output_images/fire.jpg) | ![](https://github.com/Parth-D3/Crane-Load-Zone-Monitoring/blob/main/output_images/detected_fire.jpeg) |

