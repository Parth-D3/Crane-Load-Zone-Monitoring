# Crane-Load-Zone-Monitoring
This repository contains files and models for drone video communication, image analysis, object detection, object tracking and depth estimation to be used in crane load zone monitoring.<br>
The approach is to target the crane lift zone from the video feed to ensure safety and efficiency while the load is being carried. The major accidents that occur in the scenario of a crane carrying a load are:<br>
<ol>
  <li>Overloading: Overloading stands out as a prevalent factor in crane accidents, occurring when operators surpass the designated weight capacity of the equipment.</li>
  <li>Dropped Load: Dropped load incidents often occur when a load exceeds weight limits, is improperly secured, or becomes unbalanced during lifting operations.</li>
  <li>Transportation Incidents: These accidents can occur when a vehicle collides with a crane during transportation or when the crane operator unintentionally runs the machine into a structure, person, vehicle, piece of equipment, or other obstacles. Such incidents highlight the importance of careful manoeuvring and vigilant operation during the transportation of cranes.</li>
  <li>Crane Workers’ Fall Hazards: Such incidents occur when operators fall from a crane to a lower level, with scenarios including maintenance work on a hoist or crane or unloading materials from an overhead crane. Preventive measures, such as the use of appropriate safety equipment and heightened awareness during tasks performed at elevated heights, are critical to averting accidents involving operators falling from cranes. </li>
  <li>Crane Striking Incidents: Being struck by the load, boom, or jib represents a significant risk factor in common crane accidents, often leading to serious injuries for workers involved in crane operations.</li>
</ol>

These accidents can be avoided with a heightened level of situational awareness.




To identify critical objects like construction vehicles, workers, obstacles and other hazards while the load is being carried, we have used a couple of object detection models. In order to understand the relative position of the load being carried and nearby workers, we have used depth estimation, trajectory prediction and Multi-Object Tracking (MOT) algorithms. 
### Drone to PC video live streaming
For live video streaming between drone and end device like a PC, Gstreamer 1.24.12 is used.<br>
<ol>
  <li>drone.py: Python implementation with gstreamer pipeline to send video feed to a PC</li>
  <li>PC_receiver.py: Python implementation with gstreamer pipeline to receive video feed from a drone with the help of PC ip address and Port No.</li>
</ol>

### Object Detection
Various object detection models are used to detect entities in the load/lift zone of the 
