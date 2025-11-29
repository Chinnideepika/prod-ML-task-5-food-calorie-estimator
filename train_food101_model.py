# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 23:39:28 2025

@author: Deepika
"""

import tensorflow as tf
from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras import layers, models
import os

# ------------------------------------
# CONFIG
# ------------------------------------
DATA_DIR = r"C:\Users\Deepika\Downloads\archive (2)\food-101\food-101\images" 
IMG_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 5   # start small; increase later

# ------------------------------------
# LOAD DATA
# ------------------------------------
train_ds = image_dataset_from_directory(
    DATA_DIR,
    validation_split=0.2,
    subset="training",
    seed=42,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
)

val_ds = image_dataset_from_directory(
    DATA_DIR,
    validation_split=0.2,
    subset="validation",
    seed=42,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
)

class_names = train_ds.class_names
num_classes = len(class_names)
print("Classes loaded:", num_classes)

# Save class names to file
with open("class_names.txt", "w") as f:
    for c in class_names:
        f.write(c + "\n")

AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.prefetch(AUTOTUNE)
val_ds = val_ds.prefetch(AUTOTUNE)

# ------------------------------------
# MODEL
# ------------------------------------
base_model = EfficientNetB0(include_top=False, weights="imagenet",
                            input_shape=IMG_SIZE + (3,))
base_model.trainable = False

inputs = layers.Input(shape=IMG_SIZE + (3,))
x = tf.keras.applications.efficientnet.preprocess_input(inputs)
x = base_model(x, training=False)
x = layers.GlobalAveragePooling2D()(x)
x = layers.Dropout(0.3)(x)
outputs = layers.Dense(num_classes, activation="softmax")(x)

model = models.Model(inputs, outputs)
model.summary()

model.compile(optimizer=tf.keras.optimizers.Adam(1e-3),
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

# ------------------------------------
# TRAIN
# ------------------------------------
history = model.fit(train_ds, validation_data=val_ds, epochs=EPOCHS)

# ------------------------------------
# SAVE MODEL
# ------------------------------------
model.save("food101_model.h5")
print("Model saved successfully!")


