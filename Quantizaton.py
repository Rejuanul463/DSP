import matplotlib.pyplot as plt
def quantize_signal(signal, levels):
    max_value = max(signal)
    min_value = min(signal)
    step_size = (max_value - min_value) / levels

    quantized_signal = []
    for sample in signal:
        quantized_value = min_value + step_size * (round((sample - min_value) / step_size))
        quantized_signal.append(quantized_value)

    return quantized_signal

frequency = 5  # Hz
amplitude = 1
duration = 1  # seconds
sample_rate = 1000  # samples per second

# Generate original signal (sine wave)
import math

num_samples = int(duration * sample_rate)
original_signal = [amplitude * math.sin(2 * math.pi * frequency * t / sample_rate) for t in range(num_samples)]

# Parameters for quantization
quantization_levels = 8

# Quantize the signal
quantized_signal = quantize_signal(original_signal, quantization_levels)

# Plot original and quantized signals
plt.figure(figsize=(10,6))
plt.subplot(2, 1, 1)
plt.plot(original_signal, label='Original Signal')
plt.title('Quantization of a Digital Signal')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(quantized_signal, label='Quantized Signal')
plt.title('Quantization of a Digital Signal')

plt.show()
