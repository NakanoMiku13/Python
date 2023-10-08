import tensorflow as tf
import os.path
import math
import numpy as np
import datetime
NEURONS = 32
imSize = 1024
def CreateModel():
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Conv2D(NEURONS,(3,3),activation=tf.nn.relu,input_shape=(imSize,imSize,3)))
    model.add(tf.keras.layers.MaxPool2D(pool_size=(2,2)))
    model.add(tf.keras.layers.Conv2D(NEURONS * 2,(3,3),activation=tf.nn.relu))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(2,activation=tf.nn.sigmoid))
    model.compile(loss="binary_crossentropy",optimizer="adam",metrics=["accuracy"])
    return model
def ResizeDataset(fileFormat:str, source:str, images:list, destiny:str):
    from PIL import Image
    c = 0
    for i in images:
        try:
            image = destiny.format(i)
            os.remove(image)
        except:
            pass
    for i in images:
        try:
            photo = Image.open(fileFormat.format(str(i))).convert('RGB')
            newPhoto = photo.resize([imSize,imSize])
            img = newPhoto.save(destiny.format(i))
            c += 1
        except Exception as ex:
            print(str(ex))
def _parse_function(filename, label):
    image_string = tf.io.read_file(filename)
    image_decoded = tf.image.decode_jpeg(image_string, channels=3)
    image = tf.cast(image_decoded, tf.float32)
    image /= 255
    return image, label
def CreateDataset():
    correctSamples = list()
    incorrectSamples = list()
    datasetList = list()
    labelList = list()
    files = os.listdir("files/correctsamples/")
    correctDatasetSize = len(files)
    ResizeDataset("files/correctsamples/{0}","files/correctsamples/",files,"files/trainModelCorrect/{0}")
    files = os.listdir("files/wrongsamples/")
    incorrectDatasetSize = len(files)
    ResizeDataset("files/wrongsamples/{0}","files/wrongsamples/",files, "files/trainModelIncorrect/{0}")
    files = os.listdir("files/trainModelCorrect/")
    for i in files:
        correctSamples.append("files/trainModelCorrect/"+i)
        datasetList.append("files/trainModelCorrect/"+i)
        labelList.append(0)
    files = os.listdir("files/trainModelIncorrect/")
    for i in files:
        incorrectSamples.append("files/trainModelIncorrect/"+i)
        datasetList.append("files/trainModelIncorrect/"+i)
        labelList.append(1)
    datasetSize = correctDatasetSize + incorrectDatasetSize
    filenames = tf.constant(datasetList)
    labels = tf.constant(labelList, dtype=tf.int32)
    labels= tf.squeeze(labels)
    labels=tf.one_hot(labels,2)
    dataset = tf.data.Dataset.from_tensor_slices((datasetList,labels))
    dataset = dataset.map(_parse_function)
    return (dataset, datasetSize)
model = CreateModel()
dataset, datasetSize = CreateDataset()
train_data = dataset.repeat().shuffle(datasetSize).batch(15)
checkpoint_path = "checkpoints/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)
checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,save_weights_only=True,verbose=1)
steps = math.ceil(datasetSize / 15)
history = model.fit(train_data, epochs=50, steps_per_epoch=steps, callbacks=[checkpoint_callback])
modelName = "IdDetection_{0}.h5".format(datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S"))
model.save("models/"+modelName)