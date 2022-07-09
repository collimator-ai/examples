
# Optimal Cruise Control
""" 
# Objective
# Optimally tune a PI controller for a car cruise controller using Collimator
"""
"""
# Project Description
# Using Collimator's python notebook we will tune a cruise controller ensuring that it has zero steady error with no overshoot and a fast-settling time.
"""
"""
# Model Requirements
# Import the Cruise Control Model
"""
"""
# Results
# The optimal PI gains are $K_p = 7.37$ and $K_i = 0.29$. 
"""

import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
import collimator as C
from scipy import optimize

# linearizing the car dynamics submodel and the engine dynamics submodel in order to extract the total transfer function of the car cruise system.
my_model = c.load_model('Cruise Control')
car_model = my_model.find_block('car_dynamics')
car_ss = c.linearize(my_model, car_model).to_state_space()
engine_model = my_model.find_block('engine_dynamics')
engine_ss = C.linearize(my_model, engine_model).to_state_space()
cruise_tf = ctrl.ss2tf(car_ss) * ctrl.ss2tf(engine_ss)
print(cruise_tf)

# begin designing the controller by introducing a proportional controller and evaluating some empirical gains:
plt.rcParams["figure.figsize"]= (12,8)
plt.grid(which='both')
plt.xlabel("Time")
plt.ylabel("Speed")
for kp in np.array([1, 5, 10, 50]):
    cruise_closed_y = ctrl.feedback (kp*cruise_tf,1)
    T, yout= ctrl.step_response (10*cruise_closed_y, T=np.arange(0, 50, 0.1))
    plt.plot(T,yout, label="kp = "+str(kp))
    plt.legend()

# investigating the error response 
plt.xlabel("Time")
plt.ylabel("Error")
for kp in np.array([1, 5, 10, 50]):
    cruise_closed_e = ctrl.feedback(1,kp*cruise_tf)
    T, e = ctrl.step_response (10*cruise_closed_e, T=np. arange(0, 30, 0.1))
    plt.plot(T, e, label="kp = "+str(kp))
    plt.legend()

# defining the integral objective function and running the optimization algorithm to find the optimal gains: 
def cost fun(x):
    s = ctrl.tf('s')
    pi_controller = x[0]+x[1]/s
    # for e
    cruise_closed_e = ctrl.feedback((1,pi_controller*cruise_tf)
    T, e = ctrl.step_response(10*cruise_closed_e,T=np.arange(0, 30, 0.1))
    # for u
    cruise_closed_u = ctrl.feedback(pi_controller,cruise_tf)
    T, u = ctrl.step_response(10*cruise_closed_u,T=np.arange(0, 30, 0.1))
    return np.square(e).sum() + 0.01*np.square(u).sum()
                                    
bounds = [(0, 100), (0, 100)] 
results = optimize.shgo(cost_fun, bounds) 

# Applying the PI optimal gains to the controller
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
   
# Viewing the control action response
plt.rcParams["figure.figsize"] = (12,8) 
plt.grid(which='both') 
plt.xlabel("Time") 
plt.ylabel("Control Action") 
cruise_closed_u = ctrl.feedback (pi_controller, cruise_tf) 
T, u = ctrl.step_response(10*cruise_closed_u,T=np.arange(0, 8, 0, 0.01))
plt.plot(T,0)
 
