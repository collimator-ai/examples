
<table>
<td><img src="https://user-images.githubusercontent.com/44644848/171729465-95d15fc9-1337-4082-8cf9-6ce7e46fd641.jpg"  width=500/></td>
<td><p><h1>DC Motor Position Controller Design</h1></p>
<p>Tuning a PID controller for a DC Motor Position System.</p>
</table>

## Objective
In this example using the Ziegler-Nichols method for empirically tuning the PID controller, we will show how to design and simulate a PID controller for controlling the position of a DC motor shaftin Collimator

## Project Description



### Motor Position Model

The motor is conceptually modeled as in Figure 1 with the parameters given in Table 1.
<br /><br />

###### Figure 1 DC motor model block diagram

<p align="center">
<img src="https://user-images.githubusercontent.com/44644848/171924892-4ccf72f5-9d73-4756-aff4-affc24b5c835.jpg"  width="400" alt="Figure 1 DC motor model block diagram"/>
</p>

###### Table 1 DC motor model parameters:

The transfer function of the DC motor position to the input voltage is described in the following Equation:

<p align="center">
<img src="https://user-images.githubusercontent.com/44644848/171734152-10bee237-df67-4050-b2b7-5feb31295afc.png"  width="400"/>
</p>

We can build the simulation diagram for the DC motor position with the PID controller as in Figure 2. We have also added a disturbance to later assess the disturbance rejection capability of the tuned controller.

###### Figure 2 DC motor position transfer function model with PID

<p align="center">
<img src="https://user-images.githubusercontent.com/44644848/171925900-40d0ecf1-a6f2-4fa5-901b-210e1175ac8f.png"  width="400"/>
</p>

## Results

