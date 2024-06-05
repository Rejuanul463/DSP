import matplotlib.pyplot as plt
import numpy as np
def correlate(signal1, signal2):
    len_signal1 = len(signal1)
    len_signal2 = len(signal2)
    len_output = abs(len_signal1 - len_signal2) + 1

    if len_signal1 > len_signal2:
        signal1, signal2 = signal2, signal1
        len_signal1, len_signal2 = len_signal2, len_signal1

    corr_result = np.zeros(len_output)

    for i in range(len_output):
        for j in range(len_signal1):
            corr_result[i] += signal1[j] * signal2[i + j]

    return corr_result


# Define two input signals
signal1 = [1, 2, 3, 4, 5]
signal2 = [2, 3, 4]

# Perform correlation
corr_result = correlate(signal1, signal2)

plt.subplot(3, 1, 1)
plt.stem(signal1)
plt.title('Signal 1')

plt.subplot(3, 1, 2)
plt.stem(signal2)
plt.title('Signal 2')

plt.subplot(3, 1, 3)
plt.stem(corr_result)
plt.title('Correlated Signal')

plt.tight_layout()
plt.show()
