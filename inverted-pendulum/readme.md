<table>
<td><img src="https://user-images.githubusercontent.com/44644848/172479832-4c941581-a926-4169-b7ff-207f3a0eb29f.jpg"  width=400/></td>
<td><p><h1>DC Motor Position Controller Design</h1></p>
<p>Tuning a PID controller for a DC Motor Speed System.</p>
</table>

## Objective
Design a full-state feedback controller for an inverted pendulum system. 


## Project Description
In this tutorial, we will show how to use Collimator notebook to design a full-state feedback controller for an inverted pendulum system. 
<ul>  
<li><h3><a href="https://www.collimator.ai/tutorials/inverted-pendulum-system" target="_blank" >Project Walkthrough</a></h3></li>
<li><h3><a href="https://github.com/collimator-ai/examples/blob/main/inverted-pendulum/inverted-pendulum-notebook.py">Python Notebook</a></h3></li>
</ul>
    
## Results

```python
The optimal PI gains are $K_p = 7.37$ and $K_i = 0.29$. 
Q = np.diag([1000, 0, 100, 0]) 
R = 1
K, S, E = ctrl.lar(IP_sys,Q,R)
print(K)
```
```text
[(-31.6227766	-18.39531133	57.42616018	10.98399441]]
```
```python
N = 31.5;
IP_sys_closed = ctrl.ss(A-B*K, BAN, C, D, states=['pos', 'pos_d', 'ang', 'ang_d'], inputs=['r'), outputs=['pos', 'ang']) 
T, yout = ctrl.step_response(IP_sys_closed, Tanp.arange(0, 5, 0.01)) 

fig, (axi, ax2) = plt.subplots(2) 
ax1.plot(t, yout(0, :).T) 
ax2.plot(t, yout(1,:).T) 
ax1.set_xlabel('Time')
ax1.set_ylabel('Position) 
ax1.grid(which='both') 
ax2.set_xlabel('Time') 
ax2.set_ylabel('Angle') 
ax2.grid(which='both')
```

<p align="center">
<img src="https://user-images.githubusercontent.com/44644848/172479802-f4b94c16-965b-47f1-a3cd-9d4e692807eb.png" width="400"/>
</p>

The final controller now meets the design requirements for our inverted pendulum system    

<h6><a href="https://www.collimator.ai/tutorials/inverted-pendulum-system" target="_blank">read more</a></h6></li>

