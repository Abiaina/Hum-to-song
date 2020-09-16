# Hum to Song
An API that takes vocal input, identifies most probably song match and returns the list of matching songs. Helps users identify that unknown song title with just a hum or sung melody.

## Requirements
- Audio must be in .flac format. The sample audio is pulled from [youtube](https://www.youtube.com/watch?v=rinz9Avvq6A) via [youtube-to-mp3-converter](https://ytmp3.cc/en13/) and then converted into .flac with a [mp3-flac-converter](https://cloudconvert.com/mp3-to-flac).

## References
- [TF Audio Data](https://www.tensorflow.org/io/tutorials/audio)
- [Melody ML](https://melody.ml/)
- 
## How to use:
- Post hum or sung melody.  

## How to Run
### Locally
1. Set to python3 env.
1. Run `pip install -r requirements.txt`.
1. Run `python audio_processor.py`
