# prod-ML-task-5-food-calorie-estimator
AI-powered Food Recognition and Calorie Estimation using Food-101 + Streamlit  
Built with **TensorFlow**, **Food-101**, and **Streamlit**.

---

## 📘 Project Summary  
This project combines **computer vision** and **nutrition intelligence** to help users track their dietary habits more easily.  
The system identifies food from an image (among 101 classes from the Food-101 dataset) and predicts calories using a custom nutrition mapping.

It’s lightweight, interactive, and deployable as a simple web app — ideal for learning, demos, and practical calorie awareness.

---

## 🚀 Features

### 🔎 Food Recognition  
- Trained on **Food-101** dataset (101 classes, 101,000 images)  
- Uses **EfficientNetB0** backbone for accurate classification  
- Outputs **Top-3 predictions** with confidence scores  

### 🔢 Calorie Estimation  
- Custom `calorie_database.py` with **all 101 classes mapped to approximate kcal**  
- Portion multiplier (0.5× to 3×) for more accurate calorie tracking  

### 🧾 Meal Logging  
- Each result can be added to a **local CSV log (food_log.csv)**  
- Displays timestamp, predicted food, confidence, and final calorie count  

### 🌐 Interactive Web App  
- Built using **Streamlit**  
- Clean UI to upload images, view predictions, adjust portion, and log meals  

---

## 🧠 How It Works (High-Level Architecture)

```mermaid
flowchart LR
    A[User uploads food image] --> B[Streamlit UI]
    B --> C[Preprocessing (resize + normalize)]
    C --> D[EfficientNetB0 Classifier]
    D --> E[Top-3 Predictions]
    E --> F[Calorie Lookup Table<br/>calorie_database.py]
    F --> G[Portion Adjustment]
    G --> H[Final Calorie Output]
    H --> I[Optional: Log to CSV]

