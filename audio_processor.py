import tensorflow as tf
import tensorflow_io as tfio
from IPython.display import Audio

audio = tfio.audio.AudioIOTensor('./The_Chiffons_Hes_So_Fine.flac')
audio_slice = audio[100:]
# Audio() is failing. Input is valid (tf and int objects).
Audio(audio_slice.numpy(), rate=int(audio.rate.numpy()))