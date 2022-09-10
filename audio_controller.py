import pyaudio
import wave


pa = pyaudio.PyAudio()
output_device = pa.get_default_output_device_info()
print(output_device)

RATE = 48000
CHUNK = 1024
FORMAT = pyaudio.paInt16
RECORD_SECONDS = 5
CHANNELS = 2

output_filename = 'audio-recording.wav'
wav_file = wave.open(output_filename, 'wb')

# # define audio stream properties
wav_file.setnchannels(CHANNELS)        # number of channels
wav_file.setsampwidth(pa.get_sample_size(FORMAT))        # sample width in bytes
wav_file.setframerate(RATE)    # sampling rate in Hz

stream_out = pa.open(
    rate=RATE,
    channels=CHANNELS,
    format=FORMAT,
    input=True  # Reading microphone
)


frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream_out.read(CHUNK)
    frames.append(data)

stream_out.close()

# write frames to the file
wav_file.writeframes(b''.join(frames))
wav_file.close()
