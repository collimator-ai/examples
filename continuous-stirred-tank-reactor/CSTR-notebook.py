# continuous stirred-tank reactor (CSTR)
""" 
# Objective
# Designing a Continuous Stirred-Tank Reactor
"""
"""
# Project Description
# We will investigate how to model a CSTR process in Collimator.
"""
"""
# Model Requirements
# Import the CSTR Model
"""

import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
import collimator as C

# We begin modelling the CSTR by defining the system parameters: 
F = 1.2
V = 1.2
R = 1.987204259
dH = -6250
E = 12640
k_0 = 36750400
rho = 1000
Cp = 0.5
UA = 200

# Then, we define the following lumped constants to simplify the modelling process in Collimator Model Editor:
F_over_V = F/V
Tr_const = F/V+UA/rho/Cp/V
Tc_const = UA/rho/Cp/V
exp_const = -E/R
pre_exp_const = dH/rho/Cp
print(F_over_V)
print(Tr_const)
print(Tc_const)
print(exp_const)
print(pre_exp_const)

# Before extracting the model, we will install the the "slycot" library so that we can linearize multi-input multi-output systems: 
get_ipython().system('conda install --yes --prefix {sys.prefix} slycot')

# we extract the CSTR linearized model: 
my_model = C.load_model('CSTR')
CSTR_model = my_model.find_block('CSTR_model')
CSTR  = ctrl.ss2tf(C.linearize(my_model, CSTR_model).to_state_space())
print(CSTR)

# The CSTR transfer function between the manipulated variable of the colling medium temperature Tc and the concnetration of the reactor mix Cr is:
G_cstr = CSTR[0,0]
print(G_cstr)

# First, we have a look at the step response of the CSTR linearized transfer function:
T, yout = ctrl.step_response(-G_cstr,T=np.arange(0, 20, 0.01))
fig = plt.figure(figsize=(12,8))
plt.grid(which='both')
plt.ylabel('Concentration')
plt.xlabel('Time')
plt.plot(T,yout)
plt.show()
print(ctrl.step_info(-G_cstr))

# Meanwhile, the gain can be computed easily from the CSTR DC gain as follows:  
a = 2.2/3.0998531905140876
b = ctrl.dcgain(-G_cstr)*a
s = ctrl.tf('s')
G = b/(s+a)
T, yout = ctrl.step_response(-G_cstr,T=np.arange(0, 20, 0.01))
fig = plt.figure(figsize=(12,8))
plt.grid(which='both')
plt.ylabel('Concentration')
plt.xlabel('Time')
plt.plot(T,yout,label='CSTR linearized tf')
T, yout = ctrl.step_response(G,T=np.arange(0, 20, 0.01),)
plt.plot(T,yout,label='1st order approx.')
plt.legend()

# Tuning the PI controller through parameters $\omega_0$ and $\zeta$ is much easier as they have more meaningful physical interpretation. We can increase the response speed be increasing omega while we can control the shape of response with zeta. Therefore, we define the following interactive tuning function:  
def interactive_lead_tuning(w0=1, zeta=0.25):
    s = ctrl.tf('s')
    kp = (2*zeta*w0-a)/b
    ki = (w0**2)/b
    G_closed = ctrl.feedback((kp+ki/s)*-G_cstr,1)
    fig = plt.figure(figsize=(12,8))
    t, y = ctrl.step_response(G_closed,T=np.arange(0, 20, 0.01))
    plt.grid(which='both')
    plt.ylabel('Concentration')
    plt.xlabel('Time')
    plt.plot(t, y)
    plt.show()
    print(kp+ki/s)
    
from ipywidgets import interact, fixed
interact(interactive_lead_tuning, w0 = (0,5,0.01), zeta = (0,1,0.01))
