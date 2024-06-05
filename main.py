import numpy as np, matplotlib.pyplot as plt

t_min = -1
t_max = 1
num_t = 100
Fs = 10

#continuous time signal
t = np.linspace(t_min, t_max, num_t)
xt = np.sin(2 * np.pi * 2 * t)

#sampling
Ts = 1 / Fs
n = np.arange(t_min, t_max, Ts)
xn = np.sin(2 * np.pi * 2 * n)

plt.figure(figsize=(10, 6))
# plt.plot(t,xt)
plt.stem(n,xn)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Continuous and Discrete Time Signals')
plt.legend()
plt.grid(True)
plt.show()