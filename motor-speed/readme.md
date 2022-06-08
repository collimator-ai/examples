
<table>
<td><img src="https://user-images.githubusercontent.com/44644848/171729465-95d15fc9-1337-4082-8cf9-6ce7e46fd641.jpg"  width=500/></td>
<td><p><h1>DC Motor Speed Controller Design</h1></p>
<p>Tuning a PID controller for a DC Motor Speed System.</p>
</table>

## Objective
This example will show how to model a DC motor's speed using different approaches in [Collimator](https://www.collimator.ai/). 

## Project Description
The three approaches we will use in order to model a DC motor's speed involve [simulating](https://www.collimator.ai/products/simulate) diagrams from a [differential equation](https://docs.collimator.ai/using-model-editors/block-library/continuous-blocks#integrator), [a transfer function](https://docs.collimator.ai/using-model-editors/block-library/discrete-blocks#transfer-function-discrete), and a state variable model. Then, we will design and simulate a PID controller for the DC motor speed.

Click the link below for a detialed walkthrough of the creation and tuning of the models using Collimator.
<ul>
  <li>
    <h3><a href="https://www.collimator.ai/tutorials/dc-motor-speed-controller-design" target="_blank" >Project Walkthrough</a</h3>
  </li>
</ul>

## Results

###### The PID controller simulation diagram is implemented as in Figure 11.
  
<p align="center">
<img src="https://user-images.githubusercontent.com/44644848/172411107-d1e5226a-3820-44ce-a99b-eef9e2ca2f0a.png" width="100%"/>
</p>

The final step response is plotted in Figure 15
  
###### Figure 15 Step response for PID with: kp=80, Ki=50, Kd=6 
  
<p align="center">
<img src="https://user-images.githubusercontent.com/44644848/172411738-ac3de590-d1f1-4610-b573-803c7caaafa8.png" width="100%"/>
</p>

  
<h6><a href="https://www.collimator.ai/tutorials/dc-motor-speed-controller-design" target="_blank">read more</a></h6></li>

