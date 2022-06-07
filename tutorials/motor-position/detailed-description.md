
## Tuning a PID controller for a DC Motor Position System - Project Description

### Motor Position Model

The motor is conceptually modeled as in Figure 1 with the parameters given in Table 1.
<br /><br />

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


The transfer function of the DC motor position to the input voltage is described in the following Equation:

$$\frac{Φ(s)}{U(s)} =\frac{K}{(LJs^3+(RJ+Lb) s^2+(Rb+K^2 )s)}$$

We can build the simulation diagram for the DC motor position with the PID controller as in Figure 2. We have also added a disturbance to later assess the disturbance rejection capability of the tuned controller.

###### Figure 2 DC motor position transfer function model with PID

<p align="center">
<img src="https://user-images.githubusercontent.com/44644848/171925900-40d0ecf1-a6f2-4fa5-901b-210e1175ac8f.png"  width="100%"/>
</p>

$$Numerator= [0.05]$$

$$Denominator= [0.005,0.105,0.4025,0]$$

Then, we add the controller parameters to the model parameters configuration tab:

###### Figure 3 Model parameters for PID controller

<p align="center">
<img src="https://user-images.githubusercontent.com/44644848/172247156-fb173fb0-ba27-4353-8221-d7588fb91821.png"  width="300"/>
</p>

### PID Controller Tuning within Collimator Notebook

Before we start analyzing the model and tuning the controller, we will need to import some useful libraries:

```python
import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
import collimator as C
from matplotlib.ticker import AutoMinorLocator
```

We will also define a function that returns the step response information as overshoot, rising time, and settling time:

```python
def step_info(t,response):
    print("Overshoot: %f%s"%((response.max()/response[-1)-1)*100,'%'))
    print("Rise time (90%%): %fs"%(t[next(i for i in range(0, len(response)-1) if response[i]>response [-1]*.90)]-t[0])) 
    print("Settling time (2%%): %fs"%(t[next(len (response) -i for i in range (2,len (response)-1) if abs (response[-i]/response[-1])&lt;0.98)]-t[0]))
```

The first step is to list the available models within our workspace and define a variable that links the simulation diagram within the notebook.

```python
C.list_models()
```

```text
[<Model name='DC Motor Position TF>]
```

```python
my_model = C. load_model('DC Motor Position TF')
my_model
```

```text
[<Model name='DC Motor Position TF>]
```

Then, we run a test simulation to check that we implemented our model correctly with no syntactical error:

```python
sim = C.run_simulation (my_model)
sim.show_logs()
```

```text
2022-05-02 15:51:42 INF starting model binary 
2022-05-02 15:51:42 INF simulation completed successfully exit code=0 total_time=0.161123 simulation time=0.037949
```

To tune the PID controller, we begin with a simple P controller with $K_p=1$

```python
kp = 1
ki = 0
kd = 0
my_model.set_parameters({ "kp":kp, "ki":ki, "kd":kd)) 
my_model.set_configuration({"stop_time":50}) 
sim = C.run_simulation (my_model) 
my_results = sim.results.to_pandas() 
plt.rcParams["figure.figsize") = (12,8) 
plt.plot(my_results['time'],my_results['DCMotor Position'],label="kp = "+str(kp)) 
plt.legend()
plt.xlabel("Time")
plt.ylabel("Motor Position")
step_info(my_results['time'].to_numpy(),my_results['DCMotorPosition'].to_numpy())
```

The step response for the DC motor position with the P controller is shown in Figure 4.

###### Figure 4 Step response for P controller with $K_p = 1$

<p align="center">
<img src="https://user-images.githubusercontent.com/44644848/172248012-9aaf5eb8-0a14-490b-990c-518ae26c7ff1.png"  width="50%"/>
</p>

The initially tuned P controller yields a very slow step response:


$$\begin{array}
{|l|l|}
\hline \text{Overshoot} & 0.00000 \\ 
\hline \text{Raise Time (90) } & 18.080000s \\ 
\hline \text{Settling time (2)} & 30.080000s \\ 
\hline  
\end{array}$$


Therefore, we will consider the Ziegler-Nichols table for empirical tuning of the PID controller. The Ziegler-Nichols tuning rule is defined in Table 2

###### Table 2 Ziegler-Nichols tuning rules:


$$\begin{array} 
{|l|l|}
\hline \text{Controller Type} & Kp & Ki & Kd \\ 
\hline P & 0.5K_u & 0 & 0 \\ 
\hline PI & 0.45K_u & 0.54\frac{K_u}{T_u} & 0\frac{K_u}{T_u} \\ 
\hline PD & 0.8K_u & 0 & 0.1K_uT_u \\ 
\hline \text{PID} 1 & 0.6K_u & 1.2\frac{K_u}{T_u} & 0.075K_uT_u \\ 
\hline \text{PID} 2 & 0.33K_u & 0.66\frac{K_u}{T_u} & 0.11K_uT_u \\ 
\hline \text{PID} 3 & 0.20K_u & 0.40\frac{K_u}{T_u} & 0.066K_uT_u \\ 
\hline  
\end{array}$$


The tuning rules depend on determining the ultimate gain $K_u$ and the oscillation period $T_u$. To determine these values, we perform a sweep for the P gain until we get a pure oscillatory response:

```python
plt.rcParams["figure.figsize"] = (12,8)
plt.axes().xaxis.set_minor_locator(AutoMinorLocator())
plt.grid which='both')
my_model.set_configuration({"stop_time":5})
for kp in np.array([100, 160, 170, 200]):
    my_model.set_parameters({"kp":kp})
    sim = C.run_simulation(my_model)
    my_results = sim.results.to_pandas()
    plt.plot(my_results['time'],my_results['DCMotor Position'], label="kp = "+str(kp))
    plt.legend()
    plt.xlabel("Time")
    plt.ylabel("Motor Position")
```

From Figure 5, we can see that the ultimate gain is and the ultimate period is approximately $T_u. = 0.65$

###### Figure 5 Sweep response for some P gains

<p align="center">
<img src="https://user-images.githubusercontent.com/44644848/172380081-c4d5feeb-9ae4-4cb8-9fcf-22361be4cb0b.png"  width="50%"/>
</p>

Consequently, we apply the extracted gain to find the PID controller gains as defined in the Ziegler-Nichols tuning rules:

```python
Ku = 170
Tu = 0.65

kp = [0.5*Ku,	0.45*ku, 0.8*ku, 0.6*Ku, 0.333*Ku, 0.2*Ku]
ki = [0, 0.54*Ku/Tu, 0, 1.2*Ku/Tu, 0.667*Ku/Tu, 0.4*Ku/Tu] 
kd = [0, 0, 0.1*Ku*Tu, 0.075*Ku*Tu, 0.111*Ku*Tu, 0.0667*Ku*Tu] 
labels = ["P", "PI", "PD", "PID 1", "PID 2", "PID 3"]
plt.rcParams["figure. figsize"] = (12,8)
for i inrange(0, len(labels)):
    my_model.set_parameters({"kp": kp[i]})
    my_model.set_parameters({"ki":ki[i]})
    my_model.set_parameters({"kd":kd[i]})
    sim = C.run_simulation (my_model)
    my_results = sim.results. to_pandas()
    plt.plot(my_results['time'], my_results['DCMotor Position'], label=labels[i])
    plt.xlabel("Time")
    plt.ylabel("Motor Position")
    plt.legend()
```

###### Figure 6 Step response for Ziegler-Nichols PID controllers

<p align="center">
<img src="https://user-images.githubusercontent.com/44644848/172380097-aa21ff29-e91a-47f1-a4d6-7b597a266e2c.png"  width="50%"/>
</p>

From the step responses, we can see that “PID 2” yields the best step response among the available controllers. Therefore, we will have another look at the “PID 2” controller to investigate the step response the characteristics:

```python
plt.rcParams["figure.figsize"] = (12,8)
plt.grid()
my_model.set_parameters({"kp":kp[i]})
my_model.set_parameters({"ki":ki[i]})
my_model.set_parameters({"kd":kd[i]})
sim = C.run_simulation (my_model)
my_results = sim.results.to_pandas()
plt.plot(my_results['time'],my_results['DCMotorPosition'],label=labels[i])
plt.xlabel("Time")
plt.ylabel("Motor Position")
plt.legend() 
step_info(my_results['time'].to_numpy(),my_results['DCMotor Position'].to_numpy())
my_model.parameters
```

###### Figure 7 Step response of controller “PID 2”

<p align="center">
<img src="https://user-images.githubusercontent.com/44644848/172380747-f1a8a587-2043-44e4-8365-5f1c596835a0.png"  width="50%"/>
</p>

Finally, we investigate the tuned PID controller parameters in the model editor to further study the disturbance rejection of the controller. The characteristics of controller disturbance rejection are illustrated in Figure 8.

###### Figure 8 Step response for disturbance rejection of PID 2 controller

<p align="center">
<img src="https://user-images.githubusercontent.com/44644848/172380960-dd6ad4af-701d-47df-9911-25bb6569f691.png"  width="100%"/>
</p>
