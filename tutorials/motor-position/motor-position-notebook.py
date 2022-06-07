# import the following libraries in order to ensure we can analyze and tune the controller
import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
import collimator as C
from matplotlib.ticker import AutoMinorLocator

# define a function that returns the step response information as overshoot, rising time, and settling time:
def step_info(t,response):
    print("Overshoot: %f%s"%((response.max()/response[-1)-1)*100,'%'))
    print("Rise time (90%%): %fs"%(t[next(i for i in range(0, len(response)-1) if response[i]>response [-1]*.90)]-t[0])) 
    print("Settling time (2%%): %fs"%(t[next(len (response) -i for i in range (2,len (response)-1) if abs (response[-i]/response[-1])&lt;0.98)]-t[0]))

# Then, we list the available models within our workspace and define a variable that links the simulation diagram within the notebook.
C.list_models()                                                 
my_model = C. load_model('DC Motor Position TF')

# then, we run a test simulation to check that we implemented our model correctly with no syntactical error:
sim = C.run_simulation (my_model)
sim.show_logs()

# we begin with a kp = 1 to tune the PID controller
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

# in order to determine the ultimate gain Ku and the oscillation period Tu. we perform a sweep for the P gain until we get a pure oscillatory response:
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

# Consequently, we apply the extracted gain to find the PID controller gains as defined in the Ziegler-Nichols tuning rules:           
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

# the “PID 2” controller yields the best step response. Therefore, we will have another look at the “PID 2” controller:
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
             
   
