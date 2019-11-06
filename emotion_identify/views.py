from django.shortcuts import render, redirect
from .models import UploadVoice,Sample
import librosa
from . import load_model as lm
import sounddevice as sd
from scipy.io.wavfile import write

# Create your views here.
def upload(request):
    if sample:
        try:
            voice = UploadVoice.objects.latest('id')
            voice.description = voice.audio.url
            voice.emotion = lm.predictions(voice.description)[0].upper()
            voice.save()
            return render(request, 'index.html',{'voice':voice,'upload':True})
        except Exception as e:
            return render(request, 'index.html',{'upload':False,'Exception':e})
    else:
        return render(request, 'index.html',{'voice':samp,'upload':True})

def hnd_load(request):
    u_file = request.FILES['file']
    extension = u_file.name.split(".")[1].lower()
    if(extension == 'wav'):
        global sample
        shr = UploadVoice()
        shr.audio = request.FILES['file']
        shr.save()
        sample = True
    else:
        return render(request, 'index.html',{'upload':False,'Exception':""})
    return redirect('main')

def recording(request):
    global sample
    fs = 44100  # Sample rate
    seconds = 3.0  # Duration of recording

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('media/speech/recording_voice.wav', fs, myrecording)
    shr = UploadVoice()
    shr.audio = 'speech/recording_voice.wav'
    shr.save()
    sample = True
    return redirect('main')

def sample(request, value):
    try:
        global samp
        global sample
        samp = Sample.objects.get(id = value)
        sample = False
        return redirect('main')
    except Exception as e:
        return render(request, 'index.html',{'upload':False,'Exception':e})
