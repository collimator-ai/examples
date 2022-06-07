
<table>
<td><img src="https://user-images.githubusercontent.com/44644848/171729465-95d15fc9-1337-4082-8cf9-6ce7e46fd641.jpg"  width=500/></td>
<td><p><h1>DC Motor Position Controller Design</h1></p>
<p>Tuning a PID controller for a DC Motor Position System.</p>
</table>

## Objective
In this example using the Ziegler-Nichols method for empirically tuning the PID controller, we will show how to design and simulate a PID controller for controlling the position of a DC motor shaftin Collimator

## Project Description
Click the link below for a detialed look at the creation and tuning of the models, or the link below that for the Python Notebook file to view the python code that can be run on Collimator.
<ol>
<li><h3><a href="https://www.collimator.ai/tutorials/dc-motor-position-controller-design">Detailed Project Walkthrough</a></h3></li>
<li><h3><a href="https://github.com/collimator-ai/examples/blob/main/motor-position/motor-position-notebook.py">Python Notebook</a></h3></li>
</ol>

## Results

“PID 2” yields the best step response among the available controllers. Therefore, we will have another look at the “PID 2” controller to investigate the step response the characteristics:

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

<h6><a href="https://www.collimator.ai/tutorials/dc-motor-position-controller-design">read more</a></h6></li>

