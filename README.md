# 📱 Mobile Price Prediction Project (Egyptian Market)

A machine learning project for predicting mobile phone prices in the Egyptian market using real collected data from phones released during the last 3 years.

Unlike generic datasets from Kaggle, this project is based on actual Egyptian market data, where prices are affected by many real-world factors such as:

- Taxes
- Phone condition
- RAM
- Storage capacity
- Battery health
- Brand popularity
- Market demand

The project uses Machine Learning models to predict mobile prices for both Android and iPhone devices separately.

---

# 🚀 Project Idea

This project predicts the price of used and new mobile phones in Egypt using Machine Learning.

We collected and cleaned real phone data from the Egyptian market, then trained two different models:

- Android Model
- iPhone Model

Both models use:

```python
RandomForestRegressor
```

---

# 📂 Project Structure

```text
Project Folder/
│
├── data/
│   ├── All data for android
│   ├── All data for iphone (1)
│   └── Dataset containing all mobile phones
│
├── cleaning data android/
│   └── Cleans Android dataset
│
├── cleaning data iphone/
│   └── Cleans iPhone dataset
│
├── data analysis/
│   └── Generates 5 matplotlib analysis charts
│
├── GUI/
│   └── GUI code for the application
│
├── machine learning/
│   ├── Android model
│   └── iPhone model
│
├── images/
│   └── Icons and GUI images
│
└── Final project.py
```

---

# ⚙️ How The Project Works

## 1️⃣ Dataset Folder

Inside the `data` folder, you will find:

- Android dataset
- iPhone dataset
- Combined dataset for all phones

These datasets are the raw collected data from the Egyptian market.

---

# 🧹 Android Data Cleaning

Folder:

```text
cleaning data android
```

### Required File

The code requires this dataset inside the `data` folder:

```text
All data for android
```

### What It Does

This code:

- Cleans Android phone data
- Removes invalid values
- Processes the dataset
- Generates a cleaned dataset named:

```text
datafinallllll
```

---

# 🍎 iPhone Data Cleaning

Folder:

```text
cleaning data iphone
```

### Required File

The code requires this dataset inside the `data` folder:

```text
All data for iphone (1)
```

### What It Does

This code:

- Cleans iPhone data
- Processes the dataset
- Generates a cleaned dataset named:

```text
datafinaliphone
```

---

# 📊 Data Analysis

Folder:

```text
data analysis
```

This folder contains analysis code using:

```python
matplotlib
```

The code generates 5 charts that explain and visualize the data.

Examples of analysis:

- Price distribution
- RAM vs Price
- Storage vs Price
- Brand comparisons
- Market trends

---

# 🤖 Machine Learning

Folder:

```text
machine learning
```

This folder contains:

- Android Machine Learning model
- iPhone Machine Learning model

Both models depend on the cleaned datasets generated from:

- `cleaning data android`
- `cleaning data iphone`

### Model Used

```python
RandomForestRegressor
```

---

# 🖥️ GUI

Folder:

```text
GUI
```

Contains the graphical user interface code for the application.

The GUI allows users to:

- Enter phone specifications
- Predict phone prices easily
- Interact with the ML models

---

# 🖼️ Images Folder

Folder:

```text
images
```

Contains:

- Icons
- GUI images
- Visual assets used in the application

---

# 🎯 Final Application

Main file:

```text
Final project.py
```

This is the final integrated application that connects:

- GUI
- Machine Learning models
- Data processing
- Price prediction system

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Tkinter

---

# 📈 Why This Project Is Different

Most mobile price prediction projects use public datasets from websites like Kaggle.

This project is different because:

✅ The data was collected manually from the Egyptian market  
✅ Prices reflect real Egyptian market conditions  
✅ Includes important local pricing factors  
✅ Separate models for Android and iPhone  
✅ Realistic predictions for local users

---

# 👨‍💻 Features

- Real Egyptian market data
- Separate ML models for Android & iPhone
- Data cleaning pipeline
- Data visualization
- GUI application
- Machine Learning price prediction
- Easy to use

---

# ▶️ How To Run The Project

## Step 1

Make sure all datasets are inside the `data` folder.

## Step 2

Run Android cleaning code.

## Step 3

Run iPhone cleaning code.

## Step 4

Run Machine Learning training files.

## Step 5

Run:

```text
Final project.py
```

---

# 📌 Notes

- Make sure all required datasets exist before running the project.
- The project was designed specifically for the Egyptian mobile market.
- Predictions may vary depending on market changes.

---

# ❤️ Project Goal

The main goal of this project is to create a realistic mobile price prediction system based on actual Egyptian market data using Machine Learning.# UsedPhone-Price-Prediction-ML
