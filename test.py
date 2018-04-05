
import numpy as np
import matplotlib.pyplot as plt

# Import the Preset class
from presets import Preset


# To use presets, we'll make a dummy import of librosa
# and the display submodule here.
import librosa as _librosa
import librosa.display as _display
# The assignment here is to circumvent python's inability
# to rename submodule imports within the package
_librosa.display = _display


# First, we need to set up the preset-wrapped librosa import

librosa = Preset(_librosa)

# To change the default sampling rate, we can set the `sr` entry:
librosa['sr'] = 44100

# and similarly for hop_length and n_fft
librosa['hop_length'] = 1024
librosa['n_fft'] = 4096

# In general, when you set `librosa['X']` for any string `X`, anywhere within
# librosa where the parameter `X` occurs as a keyword-argument,
# its default value will be replaced by whatever value you provide.


