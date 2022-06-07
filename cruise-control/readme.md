

<table>
<td><img src="https://user-images.githubusercontent.com/44644848/171924288-b91aefdb-55aa-49b7-93d6-4e0d7cfb503f.jpg"  width=400/></td>
<td><p><h1>DC Motor Position Controller Design</h1></p>
<p>Tuning a PID controller for a DC Motor Speed System.</p>
</table>

## Objective
Optimally tune a PI controller for a car cruise controller using Collimator.

## Project Description
Using Collimator's python notebook we will tune a cruise controller ensuring that it has zero steady error with no overshoot and a fast-settling time.

Click the link below for a detialed walkthrough of the creation and tuning of the models using Collimator.

<ul>
  <li><h3><a href="https://www.collimator.ai/tutorials/optimal-cruise-control" target="_blank">Project Walkthrough</a</h3> </li>
  <h3><a href="https://github.com/collimator-ai/examples/blob/main/cruise-control/cruise-control-notebook.py">Python Notebook</a</h3></li>
</ul>

## Results

The optimal PI gains are $K_p = 7.37$ and $K_i = 0.29$. 

```python
plt.rcParams("figure. figsize"] = (12,8)
plt.grid(which="both")
3 = ctrl.tf('s')
pi_controller = results.x[0}+results.x[11/s
plt.xlabel ("Time")
plt. ylabel("Speed")
cruise_closed_y = ctrl. feedback(pi_controllerscruise_tf,1)
T, yout = ctrl.step_response(10scruise_closed_y,T=np.arange(O, 50, 0.1))
plt.plot(T,yout)
ctrl. step_info(cruise_closed_y)   
```
```text
{'RiseTime': 2.059281027398911,
'SettlingTime’: 3.5694204474914453,
‘SettLinglMin': 0.9032064836020911,
‘SettLinglMax': 1.0,
'overshoot': 0,
'Undershoot': 0,
'Peak': 0.9999845586515097,
'PeakTime’: 177.9218807672659,
'SteadyStateValue': 1.0}
```

<p align="center">
<img src="https://user-images.githubusercontent.com/44644848/172439183-9eb304ea-53af-42c5-a033-82801b9acaaa.png" width="400"/>
</p>
    
We can see that the tuned controller has a zero steady error with no overshoot and a fast-settling time. By investigating the control action response, we can see that the controller yields a reasonable control action.     

<p align="center">
<img src="https://user-images.githubusercontent.com/44644848/172439189-5b7beb7f-d0b4-4426-bdb4-d97f271c7e3d.png" width="400"/>
</p>
  
<h6><a href="https://www.collimator.ai/tutorials/optimal-cruise-control" target="_blank">read more</a></h6></li>

