import soundfile as sf
import numpy as np
from scipy.signal import resample

def convert_to_azure_pcm(input_path, output_path):
    data, samplerate = sf.read(input_path)

    # Ensure mono
    if len(data.shape) > 1:
        data = data[:, 0]  # take first channel

    # Resample to 16000 Hz if necessary
    if samplerate != 16000:
        num_samples = round(len(data) * float(16000) / samplerate)
        data = resample(data, num_samples)

    # Convert to 16-bit PCM
    data = np.int16(data * 32767)
    sf.write(output_path, data, 16000, subtype='PCM_16')