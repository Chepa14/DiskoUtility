from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

samplerate, data = wavfile.read('./audio/wav/Mr_Kitty_After_Dark_Slowed_Down.wav')

print(samplerate)
print(data.shape)

length = data.shape[0] / samplerate
print(f"length = {length}s")

time = np.linspace(0., length, data.shape[0])
plt.plot(time, data[:, 0], label="Left channel")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()
