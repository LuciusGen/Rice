import cv2
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
from object_det import main
import os


def teach_neural(dir):
    neural = list()
    for pic in os.listdir(dir):
        pic = cv2.imread(dir + "\\" + pic)
        pic = cv2.cvtColor(pic, cv2.COLOR_BGR2RGB)
        main(pic, neural)
    return neural

train_set_rice = "C:\\dowloads\\practic\\train_data\\rice"
train_set_weed = "C:\\dowloads\\practic\\train_data\\weed"


if __name__ == "__main__":
    ner1, ner2 = teach_neural(train_set_rice), teach_neural(train_set_weed)
    train_inp, train_out = list(), list()

    for i in ner1:
        train_inp.append(np.array(i))
        train_out.append("rice")

    for i in ner2:
        train_inp.append(np.array(i))
        train_out.append("weed")

    inputs = keras.Input(shape=(784,), name='digits')
    x = layers.Dense(64, activation='relu', name='dense_1')(inputs)
    x = layers.Dense(64, activation='relu', name='dense_2')(x)
    outputs = layers.Dense(10, activation='softmax', name='predictions')(x)

    model = keras.Model(inputs=inputs, outputs=outputs)

    model.compile(optimizer=keras.optimizers.RMSprop(),
                  loss=keras.losses.SparseCategoricalCrossentropy(),
                  metrics=[keras.metrics.SparseCategoricalAccuracy()])

    history = model.fit(train_inp, train_out)

    print('\n# Оцениваем на тестовых данных')
    results = model.evaluate(x_test, y_test, batch_size=128)
    print('test loss, test acc:', results)