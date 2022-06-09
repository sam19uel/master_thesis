# As an exercise, just translate formula of Eq (2) into coding language
# Reference paper:  Efficient on the fly calculation of time correlation functions in computer simulations - Jorge Ramírez1

import sys
import numpy as np
import matplotlib.pyplot as plt

print("Reminder: This script for calculating the Autocorrelation of a Function f(x) uses sys.argv which are, in order: [data_file] [x_column] [f(x)_column] [output_filename]")

# Systerm Arguments
# 1. Importing data using sys.argv:
data = np.loadtxt(sys.argv[1])

# 2. x-axis column
x_col = int(sys.argv[2])
# 3. f(x) column 
f_x_col = int(sys.argv[3])

# 4. Name of Outputfile
outputfilename = str(sys.argv[4])

# ASSUMPTION OF DATA INPUT FILE: [time] [funtion(time)]
# Dynamical Funtion
f = data[:,f_x_col]
# Time steps = N-1 as with notation of paper such that total traj time T = (N-1)*dt
time = data[:,x_col]

# Delta t of signal
dt = time[1] - time[0]

time_steps = np.size(time)

# Total Traj Length
total_time = time_steps*dt

# Calculating the TACF of the dynamical funtion f(t)
TACF = []

# lag time or shift
tau = []

for j in range(time_steps):
    tmp = []
    tau.append(j)
    for i in range(time_steps-j):
        tmp.append(f[i]*f[i+j])
    TACF.append(1/(time_steps+1-j)*np.sum(tmp))

# rescaling tau
tau_rescaled = [element * dt for element in tau]

#############################
## Writting to an output file:
# TACF
TACF_output = []
for line in range(len(time)):
    TACF_output.append([tau_rescaled[line],TACF[line]])

np.savetxt(outputfilename, TACF_output, delimiter='   ', newline='\r\n')

# Plotting the Autocorreltaion functions




# normal scale : note that we are multiplying by dt because we need to rescale the time shift with the dt
plt.plot(tau_rescaled, TACF, label='TACF')
plt.xlabel('Lag or Shift [s]')
plt.ylabel('Autocorrelation')
plt.legend()
plt.show()

# # # Plotting the TACF functions
# # # log scale - y axis
plt.plot(tau_rescaled, TACF, label='TACF')
plt.xlabel('Lag or Shift [s]')
plt.ylabel('Autocorrelation')
plt.yscale("log")
plt.legend()
plt.show()

# # # Plotting the TACF functions
# # # log scale - x axis
plt.plot(tau_rescaled, TACF, label='TACF')
plt.xlabel('Lag or Shift [s]')
plt.ylabel('Autocorrelation')
plt.xscale("log")
plt.legend()
plt.show()

# # # Plotting the TACF functions
# # # log scale - x and y axis
plt.plot(tau_rescaled, TACF, label='TACF')
plt.xlabel('Lag or Shift [s]')
plt.ylabel('Autocorrelation')
plt.xscale("log")
plt.yscale("log")
plt.legend()
plt.show()


# Normalized Autocorrelation Functions
plt.plot(tau_rescaled, TACF/TACF[0], label='Normalised TACF')
plt.xlabel('Lag or Shift [s]')
plt.ylabel('Autocorrelation')
plt.legend()
plt.show()
