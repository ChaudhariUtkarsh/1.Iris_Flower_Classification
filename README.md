# 🌸 Iris Flower Classification

A machine learning web application that classifies Iris flowers into **Setosa**, **Versicolor**, or **Virginica** based on sepal and petal measurements, built with a custom-styled Streamlit UI.

---

## 📁 Project Structure

```
Iris_Flower_Classification/
├── images/
│   └── background.jpg          # Background image for the web app
├── models/
│   └── iris_model.pkl          # Trained Random Forest model
├── app.py                      # Streamlit web application
├── train_model.py              # Model training script
├── Iris_Flower_Classification.ipynb  # EDA & experimentation notebook
├── requirements.txt            # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### 1. Create & Activate Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install packages individually:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn jupyter streamlit
```

### 3. Train the Model

```bash
python train_model.py
```

Trains a **Random Forest Classifier** (200 estimators, `random_state=42`) on the Scikit-learn Iris dataset and saves the model to `models/iris_model.pkl`.

### 4. Run the App

```bash
streamlit run app.py
```

---

## 🧠 Model Details

| Property       | Value                         |
|----------------|-------------------------------|
| Algorithm      | Random Forest Classifier      |
| Estimators     | 200                           |
| Random State   | 42                            |
| Dataset        | Scikit-learn Iris Dataset     |
| Output Classes | Setosa, Versicolor, Virginica |
| Serialization  | Joblib (`.pkl`)               |

---

## 🌼 Input Features

| Feature      | Range (cm) | Default |
|--------------|------------|---------|
| Sepal Length | 0.1 – 10.0 | 5.1     |
| Sepal Width  | 0.1 – 10.0 | 3.5     |
| Petal Length | 0.1 – 10.0 | 1.4     |
| Petal Width  | 0.1 – 10.0 | 0.2     |

---

## 🖥️ App Features

- Custom background image with CSS styling
- Two-column input layout for flower measurements
- Displays predicted species name with confidence score (%)
- Shows per-class prediction probabilities with progress bars
- Model cached with `@st.cache_resource` for performance

---

## 🛠️ Tech Stack

- **Python**
- **Scikit-learn** — Model training & prediction
- **Streamlit** — Web UI
- **Joblib** — Model serialization
- **NumPy** — Input array processing
- **Pandas / Matplotlib / Seaborn** — Data analysis (notebook)

---

## 📓 Notebook

Explore `Iris_Flower_Classification.ipynb` for data analysis, visualization, and model experimentation.

---

## 👤 Author

Developed as part of the **Oasis Infobyte** internship program.
