import numpy as np, matplotlib.pyplot as plt

#discrete signals
f = np.array([1, 2, 3 ,4 ,5])
g = np.array([2,3,4])
y = np.zeros(len(f)+len(g)-1)

#convolution
for i in range(len(f)):
    for j in range(len(g)):
        y[i+j] += f[i]*g[j]

#plot the signals
plt.figure(figsize=(14, 6))

plt.subplot(3, 1, 1)
plt.stem(np.arange(len(f)), f)
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('f[n]')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(np.arange(len(g)), g)
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('g[n]')
plt.grid(True)

plt.subplot(3,1,3)
plt.stem(np.arange(len(y)),y)
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('f[n]*g[n]')
plt.grid(True)

plt.tight_layout()
plt.show()