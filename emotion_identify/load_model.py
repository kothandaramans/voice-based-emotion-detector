# loading model and livepredictions
import keras
import librosa
import numpy as np
import pandas as pd
from keras.utils import np_utils
from keras.models import model_from_json
from sklearn.preprocessing import LabelEncoder

def dataset_extraction():
    trainfeatures = pd.read_csv('media/model/ravdess_trainfeatures.csv').iloc[:,1:]
    trainlabel = pd.read_csv('media/model/ravdess_trainlabel.csv').iloc[:,1:]

    testfeatures = pd.read_csv('media/model/ravdess_testfeatures.csv').iloc[:,1:]
    testlabel = pd.read_csv('media/model/ravdess_testlabel.csv').iloc[:,1:]

    global y_test
    X_train = np.array(trainfeatures)
    y_train = np.array(trainlabel)
    X_test = np.array(testfeatures)
    y_test = np.array(testlabel)

    global lb
    lb = LabelEncoder()
    global x_testcnn
    y_train = np_utils.to_categorical(lb.fit_transform(y_train))
    y_test = np_utils.to_categorical(lb.fit_transform(y_test))

    x_traincnn = np.expand_dims(X_train, axis=2)
    x_testcnn = np.expand_dims(X_test, axis=2)

    return x_traincnn,x_testcnn,y_train,y_test

def load_model():
    json_file = open('media/model/model1.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("media/model/Emotion_Voice_Detection_Model1.h5")
    opt = keras.optimizers.rmsprop(lr=0.00001, decay=1e-6)
    # evaluate loaded model on test data
    loaded_model.compile(loss='categorical_crossentropy',optimizer=opt, metrics=['accuracy'])
    # score = loaded_model.evaluate(x_testcnn, y_test, verbose=0)
    # print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))

    return loaded_model


def file_load(filename):
    X, sample_rate = librosa.load(filename, res_type='kaiser_fast',duration=2.5,sr=22050*2,offset=0.5)
    mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=13),axis=0)
    return mfccs

def predictions(filename):
    dataset_extraction()
    loaded_model = load_model()
    wav_feature = file_load(filename)
    livedf2= pd.DataFrame(data=wav_feature)
    livedf2 = livedf2.stack().to_frame().T
    twodim= np.expand_dims(livedf2, axis=2)

    livepreds = loaded_model.predict(twodim,batch_size=32, verbose=1)
    livepreds1=livepreds.argmax(axis=1)
    liveabc = livepreds1.astype(int).flatten()
    livepredictions = (lb.inverse_transform((liveabc)))

    return livepredictions
