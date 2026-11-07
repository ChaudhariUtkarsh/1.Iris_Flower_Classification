# 🌸 Iris Flower Classification

A machine learning web application that classifies Iris flowers into **Setosa**, **Versicolor**, or **Virginica** based on sepal and petal measurements.

---

## 📁 Project Structure

```
Iris_Flower_Classification/
├── images/
│   └── background.jpg
├── models/
│   └── iris_model.pkl
├── app.py
├── train_model.py
├── Iris_Flower_Classification.ipynb
├── requirements.txt
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

### 3. Train the Model

```bash
python train_model.py
```

This trains a **Random Forest Classifier** (200 estimators) on the Iris dataset and saves the model to `models/iris_model.pkl`.

### 3. Run the App

```bash
streamlit run app.py
```

---

## 🧠 Model Details

| Property       | Value                     |
|----------------|---------------------------|
| Algorithm      | Random Forest Classifier  |
| Estimators     | 200                       |
| Dataset        | Scikit-learn Iris Dataset |
| Output Classes | Setosa, Versicolor, Virginica |

---

## 🌼 Input Features

| Feature        | Description              |
|----------------|--------------------------|
| Sepal Length   | Length of sepal (cm)     |
| Sepal Width    | Width of sepal (cm)      |
| Petal Length   | Length of petal (cm)     |
| Petal Width    | Width of petal (cm)      |

---

## 🛠️ Tech Stack

- **Python**
- **Scikit-learn** — Model training
- **Streamlit** — Web UI
- **Joblib** — Model serialization
- **Pandas / NumPy / Matplotlib / Seaborn** — Data analysis (notebook)

---

## 📓 Notebook

Explore `Iris_Flower_Classification.ipynb` for data analysis, visualization, and model experimentation.

---

## 👤 Author

Developed as part of the **Oasis Infobyte** internship program.
