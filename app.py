import streamlit as st
import joblib
import numpy as np
import os
import base64

# Page Configuration
st.set_page_config(page_title="Iris Flower Prediction", page_icon=" ", layout="centered")

# Background Image Function
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        [data-testid="stHeader"] {{
            background: rgba(0,0,0,0);
        }}

        [data-testid="stHeader"] a,
        a[href="#stMain"] {{
            color: #000000 !important;
            font-weight: 900 !important;
            text-decoration: none !important;
        }}

        .main-title {{
            text-align: center;
            color: #000000 !important;
            font-size: 38px;
            font-weight: 900;
        }}

        .subtitle {{
            text-align: center;
            color: #000000 !important;
            font-size: 17px;
            font-weight: 900;
        }}

        h1, h2, h3, h4, h5, h6 {{
            color: #000000 !important;
            font-weight: 900 !important;
        }}

        [data-testid="stSubheader"] {{
            color: #000000 !important;
            font-weight: 900 !important;
        }}

        [data-testid="stWidgetLabel"] p {{
            color: #000000 !important;
            font-weight: 900 !important;
        }}

        [data-testid="stNumberInput"] input {{
            color: #000000 !important;
            font-weight: 900 !important;
            background-color: rgba(255,255,255,0.95) !important;
        }}

        .stMarkdown p {{
            color: #000000 !important;
            font-weight: 900 !important;
        }}

        .result {{
            background-color: rgba(255,255,255,0.95);
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 3px 12px rgba(0,0,0,0.2);
        }}

        .stButton > button {{
            background-color: #4a148c;
            color: #ffffff !important;
            font-weight: 900 !important;
            border-radius: 10px;
            border: none;
        }}

        .stButton > button:hover {{
            background-color: #6a1b9a;
            color: #ffffff !important;
        }}

        /* Footer Caption */
        .stCaption,
        [data-testid="stCaptionContainer"] p {{
            color: #000000 !important;
            font-weight: bold !important;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

# Set Background Image
BACKGROUND_PATH = os.path.join("images", "background.jpg")
if os.path.exists(BACKGROUND_PATH):
    set_background(BACKGROUND_PATH)
else:
    st.warning("Background image not found. Please check images/background.jpg")

# Load Model
MODEL_PATH = os.path.join("models", "iris_model.pkl")
@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


# Header
st.markdown('<div class="main-title">Iris Flower Classification</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Machine Learning Based Flower Prediction System</div>', unsafe_allow_html=True)
st.divider()

# Check Model
if not os.path.exists(MODEL_PATH):
    st.error("Model file not found. Please run train_model.py first.")
    st.stop()
model = load_model()

# Flower Measurements
st.subheader("Enter Flower Measurements")
col1, col2 = st.columns(2)
with col1:
    sepal_length = st.number_input("Sepal Length (cm)", min_value=0.1, max_value=10.0, value=5.1, step=0.1)
    petal_length = st.number_input("Petal Length (cm)", min_value=0.1, max_value=10.0, value=1.4, step=0.1)
with col2:
    sepal_width = st.number_input("Sepal Width (cm)", min_value=0.1, max_value=10.0, value=3.5, step=0.1)
    petal_width = st.number_input("Petal Width (cm)", min_value=0.1, max_value=10.0, value=0.2, step=0.1)
st.divider()

# Prediction
if st.button("Predict Iris Flower", use_container_width=True):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]
    class_names = ["Setosa", "Versicolor", "Virginica"]
    predicted_name = class_names[prediction]
    confidence = probabilities[prediction] * 100

    # Display Prediction Result
    st.markdown(
        f"""
        <div class="result">
            <h2>🌼 Prediction Result</h2>
            <h1 style="color:#000000 !important;">{predicted_name}</h1>
            <h3>Confidence: {confidence:.2f}%</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Prediction Probabilities
    st.subheader("Prediction Probabilities")
    for name, probability in zip(class_names, probabilities):
        st.markdown(f"<p style='color:#000000; font-weight:900;'>" f"{name}: {probability * 100:.2f}%</p>", unsafe_allow_html=True)
        st.progress(float(probability))

# Footer
st.divider()
st.caption("Developed using Python, Scikit-learn and Streamlit.")