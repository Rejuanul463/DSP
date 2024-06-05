import numpy as np
import matplotlib.pyplot as plt

def _DFT(x):
    signal_len = len(x)
    result = np.zeros(signal_len)
    for i in range(signal_len):
        for j in range(signal_len):
            result[i] += x[j] * np.exp(-2j*np.pi*i*j/signal_len)

    return result

def _IDFT(x):
    signal_len = len(x)
    result = np.zeros(signal_len)
    for i in range(signal_len):
        for j in range(signal_len):
            x[i] += result[j] * np.exp(2j*np.pi*i*j/signal_len)
            x[i]/=signal_len

    return result
#define parameters
f1 = 1000
f2 = 2000
fs = 8000
T = 1/fs
phase_shift = 3*np.pi/4
number_of_samples = 8

#vector for N samples
n = np.arange(number_of_samples)

#define the input signal x(nT)
xn = np.sin(2*np.pi*f1*n*T) + 0.5 * np.sin(2*np.pi*f2*n*T + phase_shift)

#compute the 8-point DFT
# dft = np.fft.fft(xn)
dft = _DFT(xn)

#compute the magnitude spectrum
magnitude_spectrum = np.abs(dft)

#compute the phase
phase = np.angle(dft)

#compute the power spectrum
power_spectrum = np.abs(dft) ** 2

#compute the inverse DFT
idft = _IDFT(xn)

#plot the results
plt.figure(figsize=(12, 10))

plt.subplot(5, 1, 1)
plt.plot(n, xn)
plt.title("Signal Output")
plt.xlabel("n")
plt.ylabel("Amplitude")

plt.subplot(5, 1, 2)
k = np.arange(number_of_samples)
plt.stem(k, magnitude_spectrum)
plt.title("Magnitude Spectrum")
plt.xlabel("Frequency (k)")
plt.ylabel("Magnitude")

plt.subplot(5, 1, 3)
plt.stem(k, phase)
plt.title("Phase")
plt.xlabel("Frequency (k)")
plt.ylabel("Phase (radians)")

plt.subplot(5, 1, 4)
plt.stem(k, power_spectrum)
plt.title("Power Spectrum")
plt.xlabel("Frequency (k)")
plt.ylabel("Power")

plt.subplot(5, 1, 5)
plt.plot(n, xn)
plt.stem(n, idft.real)
plt.title("Inverse DFT")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.show()