
## Tuning a PID controller for a DC Motor Speed System - Project Description

### Overview

A DC motor combines mechanical and electrical subsystems. The electrical part is an armature coil with a resistance and inductance to drive a field causing motion. The mechanical part can be modeled as an inertial rotor with friction. The DC motor is conceptually modeled as in Figure 1 with the parameters given in Table 1.

###### Figure 1 DC motor model block diagram

<p align="center">
<img src="https://user-images.githubusercontent.com/44644848/171924892-4ccf72f5-9d73-4756-aff4-affc24b5c835.jpg"  width="300" alt="Figure 1 DC motor model block diagram"/>
</p>

###### Table 1 DC motor model parameters:

$$\begin{array} 
{|l|l|}
\hline Symbol & Description & Value & Unit \\ 
\hline R & \text{Shunt Resistance} & 4 & \Omega \\ 
\hline L & \text{Coil inductance} & .25 & H \\ 
\hline K & \text{Motor Electromotive/torque constant} & .05 & N.m/A \\ 
\hline j & \text{Rotor intertia} & .02 & Kg.m2 \\ 
\hline b & \text{Friction constant}  & 0.1 & N.m.s \\ 
\hline  
\end{array}$$

### DC Motor Speed Model

The DC motor dynamics are given as the following system of differential equations:

$$L\frac{di}{dt} + Ri + K\frac{dϕ}{dt} = u$$

$$J\frac{d^2ϕ}{dt^2} +b \frac{dϕ}{dt} = Ki$$

Applying the Laplace transform for the above equations to get the domain equivalent as:

$$(Ls+R)I(s)+KΦ ̇(s) = U(s)$$

$$(Js+b) \dotΦ (s) = KIs)$$

Then, both equations are combined by eliminating the current variable to get the open-loop transfer function as:

$$\frac{\dotΦ (s)}{U(s)} = \frac{K}{(LJs^2+ (RJ +Lb)s + (Rb + K^2 ))}$$

The transfer function can also be converted into an equivalent state space form as:

###### Equation 6

$$\frac{d}{dt}\begin{bmatrix}
Φ\\ 
\dotΦ\\ 
i \end{bmatrix}
\= \begin{bmatrix}
0 & 1 & 0\\
0 &-\frac{b}{j} &\frac{K}{J}\\
0 & -\frac{K}{L} &-\frac{R}{L}
\end{bmatrix}
\begin{bmatrix}
Φ\\
\dotΦ\\
i \end{bmatrix}
\+ \begin{bmatrix}
0\\
0\\
\frac{1}{L}\end{bmatrix}u$$

###### Equation 7

$$y=\begin{bmatrix}0 & 1 & 0\end{bmatrix}
\begin{bmatrix}
Φ\\
\dotΦ\\
i\end{bmatrix}$$

### Simulating Models

##### Differential Equations Model

Substituting the parameter values in Table 1 within Equations $Ldi/dt + Ri + Kdϕ/dt = u$ and, $J(dϕ)/(dt)+bdϕ/dt = Ki$ , the DC motor speed model as a system of differential equations is described as:

$$0.25\frac{di}{dt} + 4i+ 0.05\frac{dϕ}{dt} = u$$

$$0.02\frac{(d^2 ϕ)}{(dt^2)} + 0.1 \frac{dϕ}{dt} = 0.05i$$

The dataflow of the system of differential equations can be formulated as a simulation diagram as in Figure 2.

###### Figure 2 DC motor differential equations model

<p align="center">
<img src="https://user-images.githubusercontent.com/44644848/172415527-81f4c950-e7e0-4e8a-bec6-5a17c35c3c77.png"  width="300"/>
</p>

The parameters of the models are defined in Figure 3.

###### Figure 3 DC motor model parameters

<p align="center">
<img src="https://user-images.githubusercontent.com/44644848/172415543-28c61103-6c36-4963-a1cd-0924bb939569.png"  width="300"/>
</p>

After running the simulation, the step response is visualized as in Figure 4.

###### Figure 4 Step response for DC motor differential equations model

<p align="center">
<img src="https://user-images.githubusercontent.com/44644848/172416068-bc4038f8-1900-4e42-bfe8-e7c011f04ed4.png"  width="100%"/>
</p>

##### Transfer Equations Model

The obtained transfer function for the DC motor is defined as:

$$\frac{Φ ̇(s)}{U(s)} =\frac{0.05}{(0.005s^2+ 0.105s + 0.4025)}$$

The transfer function model is implemented as in Figure 5 with the transfer function block is configured as in Figure 6. The visualization of the step response of the transfer function model is shown in Figure 7.

###### Figure 5 DC motor transfer function model

<p align="center">
<img src="https://user-images.githubusercontent.com/44644848/172419588-d690112b-83a6-496a-b838-5b8124866b19.png"  width="500"/>
</p>

###### Figure 6 Configuration of the transfer function block

<p align="center">
<img src="https://user-images.githubusercontent.com/44644848/172419606-b5f13c5a-25ed-4c5c-a000-493603f36c4c.png"  width="300"/>
</p>

###### Figure 7 Step response for DC motor transfer function model

<p align="center">
<img src="https://user-images.githubusercontent.com/44644848/172419634-eaa415d2-449e-4c17-8cdb-febd2d9105fd.png"  width="100%"/>
</p>

### State Space Model

By substituting for the DC motor model parameters in the state space model of Equations in Equation 6 and Equation 7, the following equations are obtained:

###### From Equation 6

$$\frac{d}{dt}\begin{bmatrix}
Φ\\ 
\dotΦ\\ 
i \end{bmatrix}
\= \begin{bmatrix}
0 & 1 & 0\\
0 & -5 & 2.5 \\
0 & -0.2 & -16
\end{bmatrix}
\begin{bmatrix}
Φ\\
\dotΦ\\
i \end{bmatrix}
\+ \begin{bmatrix}
0\\
0\\
4\end{bmatrix}u$$

###### Equation 7

$$y=\begin{bmatrix}0 & 1 & 0\end{bmatrix}
\begin{bmatrix}
Φ\\
\dotΦ\\
i\end{bmatrix}$$



