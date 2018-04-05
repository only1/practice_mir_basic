import matplotlib.pyplot as plt
import librosa.display

import librosa
x, sr = librosa.load('samples/simpleLoop.wav')

print(x.shape)
print(sr)

plt.figure(figsize=(14, 5))
librosa.display.waveplot(x, sr=sr)

X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X))
plt.figure(figsize=(14, 5))
librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')

