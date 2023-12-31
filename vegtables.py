# -*- coding: utf-8 -*-
"""vegtables.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tEne9HVG3uAD9pI4PVw1M8KH4bEb1KqN

# Import kaggle dataset
If you do not lnow how to import a dataset from kaggle follow the link below here :<br>https://www.kaggle.com/discussions/general/74235 <br>
You can also my codes in kaggle :<br> https://www.kaggle.com/code/matinmobayen/vegetables-imageclasssification-resnet50
"""

! pip install -q kaggle
from google.colab import files
files.upload()

! mkdir ~/.kaggle
! cp kaggle.json ~/.kaggle/

! chmod 600 ~/.kaggle/kaggle.json

"""## I downloaded dataset here"""

! kaggle datasets download -d misrakahmed/vegetable-image-dataset

"""### lets unzip the zip file"""

! unzip vegetable-image-dataset.zip

"""## lets import necessary libraries here"""

import os
import numpy as np
import keras
from keras import layers
from tensorflow import data as tf_data
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import numpy as np

"""## Take a look at a picture un dataset here and realize the shape of pictures
(Beacuse we have to set the image shape in our model)
"""

pic = r"Vegetable Images/test/Bean/0001.jpg"
image = mpimg.imread(pic)
plt.imshow(image)
plt.show()
imagse=np.array(image)
! ls "Vegetable Images/"
print(imagse.shape)

"""## Lets get ready with train test valid"""

train_path = "Vegetable Images/train"
test_path = "Vegetable Images/test"
valid_path = "Vegetable Images/validation"
# image generator , flow from directory
# you can use image generator then using flow from directory instead of what I did
import tensorflow as tf
train_data = tf.keras.utils.image_dataset_from_directory(
    train_path,
    labels='inferred',
    label_mode='categorical',
    class_names=None,
    color_mode='rgb',
    batch_size=32,
    image_size=(224, 224),
    shuffle=True,
)
test_data = tf.keras.utils.image_dataset_from_directory(
    test_path,
    labels='inferred',
    label_mode='categorical',
    class_names=None,
    color_mode='rgb',
    batch_size=32,
    image_size=(224, 224),
    shuffle=True,
)
valid_data = tf.keras.utils.image_dataset_from_directory(
    valid_path,
    labels='inferred',
    label_mode='categorical',
    class_names=None,
    color_mode='rgb',
    batch_size=32,
    image_size=(224, 224),
    shuffle=True,
)

"""# Lets create model
## I used ResNet50
"""

model = keras.applications.ResNet50(
    include_top = True,
    weights=None,
    input_shape=(224, 224, 3),
    pooling=max,
    classes = 15,
    classifier_activation="softmax",
)
model.compile(
    optimizer=keras.optimizers.SGD(learning_rate=0.01),
    loss=keras.losses.CategoricalCrossentropy(),
    metrics=["accuracy"],
)
# model.summary()
history = model.fit(
    x = train_data,
    y = None,
    batch_size=128,
    epochs=10,
    validation_split=0.0,
    validation_data=valid_data,
    shuffle=False
    )

"""## Lets visualize train and validation against epochs"""

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()

"""### Lets evaluate on test dataset"""

model.evaluate(test_data)