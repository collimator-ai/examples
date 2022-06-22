

<table>
<td><img src="https://user-images.githubusercontent.com/44644848/171918909-ca34ceca-8d40-4293-ab00-270818c6a868.jpg"  width=400/></td>
<td><p><h1>Car Suspension Design</h1></p>

Design and optimize a car's suspension system using [Collimator](https://www.collimator.ai/)

</table>

## Objective
Modeling and simulating the relationship between a car's mass and its suspension in order to gain a stable experience in spite of road interferance.

## Project Description
We begin by modeling the simple spring to see how it behaves. Then we increased the complexity of our system step by step to [simulate](https://www.collimator.ai/products/simulate) the relationship between the control force and displacement of the car and suspension system masses. We then add a PID controller in order to stabalize the system.

<ul>
<li><h3><a href="https://www.collimator.ai/tutorials/car-suspension-design" target="_blank" >Project Walkthrough</a></h3></li>
</ul>

## Results

We see amplitude of the response signal $(x1 – x2)$ equals about $0.01 [m] (1 [mm])$. For this exercise we will manually tune the PID controller. The parameters that minimize the car suspension system oscillations seems to be close to: 

$$\begin{array} 
{|l|l|}
\hline KP & 86 \\ 
\hline KD & 45 \\ 
\hline KI & 1 \\ 
\hline  
\end{array}$$

###### Fig. 19. Response of the system with controller

<p align="center">
<img src="https://user-images.githubusercontent.com/44644848/172445519-8f8a8da8-c7a6-4516-ad63-7bb9ea6f7392.png" width="100%"/>
</p>

To sum up, we modeled 1 of 4 car suspension systems. The PID controller made the overall car more stable, but there is still room for better tuning to get an even more comfortable and stable ride for our passengers.

  
<h6><a href="https://www.collimator.ai/tutorials/car-suspension-design" target="_blank">read more</a></h6></li>

