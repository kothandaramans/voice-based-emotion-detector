# voice-based-emotion-detector
voice based emotion detector - using CNN

This project presents the implementation of emotion detection from voice with a deep
Convolutional Neural Network architecture (CNN) that processes and classifies voice samples.
The architecture is an adaptation of an image processing CNN, programmed in Python using Keras
model-level library and TensorFlow backend. According to the obtained results, the model
achieves the mean accuracy of 70.7% for eight emotions (neutral, calm, happiness, fear, sadness,
disgust, anger, surprise). This model alone took approximately 5 hours to train.

Data Used: I got audio datasets with around 2000 audio files which were in the ‘wav’ format
from the following websites: http://neuron.arts.ryerson.ca/ravdess/?f=3.
The website contains speech data that is available in three different formats.
1. Audio Visual – Video with speech
2. Speech – Audio only
3. Visual – Video only

I went with the Audio only zip file because we are dealing with finding emotions from speech.
The zip file consisted of around 1400 audio files which were in ‘wav’ format.

demo

![index](screenshot/10 index.png?raw=true "Title")
