
# Inverted Pendulum System
""" 
# Objective
# Design a full-state feedback controller for an inverted pendulum system.
"""
"""
# Project Description
# We will show how to use Collimator notebook to design a full-state feedback controller for an inverted pendulum system.
"""
"""
# Model Requirements
# N/A
"""

# importing libraries native to collimator.
import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
import collimator as C

# defining our model parameters
g = 9.81
M = 0.4
m = 0.15                    
b = 0.08
L = 0.25
J = 0.005

# defining the state variable matrices
den = J*(M+m)+M*m*L**2
A = np.matrix([[0, 1, 0, 0],
              [0, -(J+m*L**2)*b/den, (m**2*g*L**2)/den, 0],
             [0, 0, 0, 1],
             [0, -(m*L*b)/den, m*g*L*(M+m)/den, 0]
             ])
B = np.matrix([0, (J+m*L**2)/den, 0, m*L/den]).T
C = np.matrix([[1, 0, 0, 0],[0, 0, 1, 0]])
D = np.matrix([0, 0]).T
IP_sys = ctrl.ss(A, B, C, D, states=['pos','pos_d','ang', 'ang_d'], 
                 inputs=['F'], outputs=['pos','ang'])
print(IP_sys)

# identifying the unstable pole
ctrl.pole(IP_sys)

# displaying the rank of the controllability matrix - should return 4
np.linalg.matrix_rank(ctrl.ctrb(IP_sys.A,IP_sys.B))

# We start by first trying unity weights for the position, angle, and inputs:
Q = np.diag([1, 0, 1, 0])
R = 1
K, S, E = ctrl.lqr(IP_sys,Q,R)
print(K)

# next we try close the feedback with the obtained gains and investigate a step respoonse
IP_sys_closed = ctrl.ss(A-B*K, B, C, D, states=['pos','pos_d','ang', 'ang_d'], 
                        inputs=['r'], outputs=['pos','ang'])
T, yout = ctrl.step_response(IP_sys_closed,T=np.arange(0, 5, 0.01))

plt.rcParams["figure.figsize"] = (12,8)
fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(T, yout[0,:].T)
ax2.plot(T, yout[1,:].T)
ax1.set_xlabel('Time')
ax1.set_ylabel('Position')
ax1.grid(which='both')
ax2.set_xlabel('Time')
ax2.set_ylabel('Angle')
ax2.grid(which='both')

# now we try some other gains combination.
Q = np.diag([1000, 0, 100, 0])
R = 1
K, S, E = ctrl.lqr(IP_sys,Q,R)
print(K)
 
IP_sys_closed = ctrl.ss(A-B*K, B, C, D, states=['pos','pos_d','ang', 'ang_d'], 
                        inputs=['r'], outputs=['pos','ang'])
T, yout = ctrl.step_response(IP_sys_closed,T=np.arange(0, 5, 0.01))
plt.rcParams["figure.figsize"] = (12,8)
fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(T, yout[0,:].T)
ax2.plot(T, yout[1,:].T)
ax1.set_xlabel('Time')
ax1.set_ylabel('Position')
ax1.grid(which='both')
ax2.set_xlabel('Time')
ax2.set_ylabel('Angle')
ax2.grid(which='both')

# 31.5 is the N value that eliminates our steady-state error
N = 31.5;
IP_sys_closed = ctrl.ss(A-B*K, B*N, C, D, states=['pos','pos_d','ang', 'ang_d'], 
                        inputs=['r'], outputs=['pos','ang'])
T, yout = ctrl.step_response(IP_sys_closed,T=np.arange(0, 5, 0.01))
#plt.rcParams["figure.figsize"] = (12,8)
#plt.grid(which='both')
fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(T, yout[0,:].T)
ax2.plot(T, yout[1,:].T)
ax1.set_xlabel('Time')
ax1.set_ylabel('Position')
ax1.grid(which='both')
ax2.set_xlabel('Time')
ax2.set_ylabel('Angle')
ax2.grid(which='both')
