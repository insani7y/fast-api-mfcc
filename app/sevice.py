import scipy.io.wavfile as wav
from python_speech_features import mfcc
from scipy.signal.windows import hann

from .models import MFCCResponse

numcep = 20
nmels = 30
nfft = 512
hop_length = 160


def recursive_list(array):
    return list(map(lambda x: list(x), array))


def get_features(file):
    samplerate, signal = wav.read(file)
    params = {
        "signal": signal,
        "samplerate": samplerate,
        "winlen": nfft / samplerate,
        "winstep": hop_length / samplerate,
        "nfilt": nmels,
        "winfunc": hann,
        "nfft": nfft,
    }
    mfcc_res = recursive_list(mfcc(**params, numcep=numcep))

    return MFCCResponse(mfcc=mfcc_res)
