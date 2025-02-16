import wave
import matplotlib.pyplot as plt
import numpy as np


obj = wave.open('../file/record_out.wav', 'rb')

sample_frequency = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)

obj.close()

t_audio = n_samples / sample_frequency

print(t_audio)

signal_arrays = np.frombuffer(signal_wave, dtype=np.int16)

times = np.linspace(0, t_audio, n_samples)

plt.figure(figsize=(15, 5))
plt.plot(times, signal_arrays)
plt.title('Audio Signal')
plt.ylabel('Wave')
plt.xlabel('Time')
plt.xlim(0, t_audio)
plt.show()