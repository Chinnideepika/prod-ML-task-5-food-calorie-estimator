# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 01:25:04 2025

@author: Deepika
"""

# app.py

import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
import pandas as pd
import os
from datetime import datetime

from calorie_database import get_food_info

# -------------------------
# CONFIG
# -------------------------
IMG_SIZE = (224, 224)
MODEL_PATH = "food101_model.h5"
CLASS_NAMES_PATH = "class_names.txt"


# -------------------------
# LOAD MODEL & CLASS NAMES
# -------------------------
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model(MODEL_PATH)
    return model


@st.cache_data
def load_class_names():
    with open(CLASS_NAMES_PATH, "r") as f:
        classes = [line.strip() for line in f.readlines()]
    idx_to_class = {i: name for i, name in enumerate(classes)}
    return idx_to_class


# -------------------------
# HELPER FUNCTIONS
# -------------------------
def preprocess_image(image: Image.Image):
    image = image.resize(IMG_SIZE)
    img_array = np.array(image).astype("float32")

    # Convert grayscale to RGB if needed
    if img_array.ndim == 2:
        img_array = np.stack([img_array] * 3, axis=-1)

    # Convert RGBA → RGB if needed
    if img_array.shape[-1] == 4:
        img_array = img_array[:, :, :3]

    img_array = np.expand_dims(img_array, axis=0)

    # Same preprocessing we used in training (EfficientNet)
    img_array = tf.keras.applications.efficientnet.preprocess_input(img_array)
    return img_array


def predict_top_k(model, img_array, idx_to_class, k=3):
    preds = model.predict(img_array)[0]  # shape: (num_classes,)
    top_indices = preds.argsort()[-k:][::-1]

    results = []
    for idx in top_indices:
        label = idx_to_class[idx]
        confidence = float(preds[idx])
        results.append((label, confidence))
    return results


def log_to_csv(date, label, display_name, calories, portion_factor, confidence):
    log_file = "food_log.csv"
    row = {
        "date": date,
        "label": label,
        "food_name": display_name,
        "portion_factor": portion_factor,
        "calories": calories,
        "confidence": confidence,
    }

    if os.path.exists(log_file):
        df = pd.read_csv(log_file)
        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    else:
        df = pd.DataFrame([row])

    df.to_csv(log_file, index=False)
    return df


# -------------------------
# STREAMLIT APP LAYOUT
# -------------------------
st.set_page_config(page_title="Food-101 Calorie Estimator", layout="centered")

st.title("🍽️ Food Image Calorie Estimator")
st.write(
    "Upload a food image. The model will recognize the dish using Food-101 "
    "and estimate calories based on a standard serving. You can adjust the portion."
)

model = load_model()
idx_to_class = load_class_names()

uploaded_file = st.file_uploader("Upload a food image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Show image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Predict
    with st.spinner("Analyzing image..."):
        img_array = preprocess_image(image)
        top_preds = predict_top_k(model, img_array, idx_to_class, k=3)

    st.subheader("Top Predictions")
    for label, conf in top_preds:
        st.write(f"- **{label}** — {conf:.1%} confidence")

    # Best prediction
    best_label, best_conf = top_preds[0]

    display_name, base_cal, serving_desc = get_food_info(best_label)

    if display_name is None:
        st.warning(
            "I recognized the food, but calorie info for this specific class "
            "is not in the database yet. Please update calorie_database.py."
        )
    else:
        st.markdown("---")
        st.subheader("Calorie Estimation")

        st.write(f"**Predicted dish:** {display_name} (*{best_label}*)")
        st.write(f"**Standard serving:** {serving_desc}")
        st.write(f"**Calories per serving:** ~{base_cal} kcal")

        portion = st.slider(
            "How many servings did you eat?",
            min_value=0.5,
            max_value=3.0,
            step=0.5,
            value=1.0,
        )

        total_cal = base_cal * portion
        st.metric("Estimated total calories", f"{total_cal:.0f} kcal")

        if st.button("Log this meal"):
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            df = log_to_csv(
                date=now,
                label=best_label,
                display_name=display_name,
                calories=total_cal,
                portion_factor=portion,
                confidence=best_conf,
            )
            st.success("Meal logged successfully!")

            with st.expander("View logged meals"):
                st.dataframe(df)

else:
    st.info("Upload a food image to get started.")
