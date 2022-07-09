#  Aircraft Pitch Loop
""" 
# Objective
# Optimally tune a PI controller for a car Aircraft Pitch Loop
"""
"""
# Project Description
# Using Collimator's python notebook we will show how to design a PID tuner for an aircraft's pitch control loop.
"""
"""
# Model Requirements
# N/A
"""

import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
import collimator as C


# In[2]:


A = np.matrix([[-0.298, 54.3, 0],
               [-0.0141, -0.399, 0],
               [0, 54.3, 0]])
B = np.matrix([0.223, 0.0199, 0]).T
C = np.matrix([0, 0, 1])
D = [0]
pitch_sys = ctrl.ss(A,B,C,D)
print(pitch_sys)


# In[3]:


print(ctrl.zero(pitch_sys))
print(ctrl.pole(pitch_sys))


# In[4]:


plt.figure(figsize=(12,8))
plt.grid(which='both')
T, yout = ctrl.step_response(0.2*pitch_sys,T=np.arange(0, 20, 0.01))
plt.plot(T, yout,label='Open Loop')
pitch_sys_closed = ctrl.feedback(pitch_sys,1)
T, yout = ctrl.step_response(0.2*pitch_sys_closed,T=np.arange(0, 60, 0.01))
plt.plot(T, yout,label='Closed Loop')
plt.legend()


# In[5]:


ctrl.step_info(0.2*pitch_sys_closed)


# In[6]:


def interactive_tuning(kp = 1, ki=0, kd=0):
    s = ctrl.tf('s')
    pid = kp+ki/s+kd*10000*s/(s+10000)
    pitch_y = ctrl.feedback(pid*pitch_sys,1)
    print(ctrl.step_info(0.2*pitch_y))
    plt.figure(figsize=(12,8))
    T, y = ctrl.step_response(0.2*pitch_y,T=np.arange(0, 50, 0.1))
    plt.grid(which='both')
    plt.plot(T, y)
    plt.ylabel('Pitch Angle')
    plt.xlabel('Time')


# In[7]:


from ipywidgets import interact, fixed
interact(interactive_tuning,kp = (0,10,0.01),ki = (0,10,0.01),kd = (0,10,0.01))


# In[ ]:
