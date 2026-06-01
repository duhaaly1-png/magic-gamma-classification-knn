# magic-gamma-classification-knn
Machine Learning classification project using K-Nearest Neighbors (KNN) to classify gamma and hadron events from the MAGIC Gamma Telescope dataset.
# MAGIC Gamma Telescope Classification using K-Nearest Neighbors (KNN)

## Overview

This project applies the K-Nearest Neighbors (KNN) algorithm to classify events from the MAGIC Gamma Telescope dataset as either Gamma Rays or Hadrons.

The project covers the complete machine learning pipeline, including data preprocessing, class balancing, model training, hyperparameter tuning, performance evaluation, and visualization.

---

## Dataset

The MAGIC Gamma Telescope dataset contains measurements collected by the MAGIC telescope to distinguish between:

- Gamma Events (g)
- Hadron Events (h)

The dataset consists of 10 numerical features describing particle shower characteristics.

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn

---

## Project Workflow

### Data Preprocessing

- Loaded dataset using Pandas
- Renamed feature columns
- Encoded target labels
- Balanced classes using downsampling
- Shuffled the dataset

### Data Splitting

Dataset was divided into:

- Training Set: 70%
- Validation Set: 15%
- Test Set: 15%

### Model Training

Implemented K-Nearest Neighbors (KNN) classification with multiple values of:

```text
k = 1, 3, 5, 7, 9, 11
```

### Hyperparameter Tuning

Compared model performance across different k values using:

- Accuracy
- Precision
- Recall
- F1 Score

Selected the best-performing model for final evaluation.

---

## Evaluation Metrics

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## Visualizations

### Confusion Matrix

Displays classification performance for:

- Gamma Events
- Hadron Events

### Accuracy vs K Value

Shows the impact of different K values on model accuracy.

---

## Skills Demonstrated

- Machine Learning
- K-Nearest Neighbors (KNN)
- Data Preprocessing
- Data Balancing
- Feature Analysis
- Hyperparameter Tuning
- Model Evaluation
- Classification Algorithms
- Data Visualization
- Scikit-learn

---

## Installation

Install required libraries:

```bash
pip install pandas scikit-learn matplotlib seaborn
```

---

## Run the Project

```bash
python knn_classification.py
```

---

## Future Improvements

- Feature Scaling
- Cross Validation
- Random Forest Comparison
- Support Vector Machine (SVM)
- XGBoost Implementation
- Automated Hyperparameter Optimization

---

## Author

### Duha Aly

Computer and Data Science Student (Class of 2027)

Areas of Interest:
- Artificial Intelligence
- Machine Learning
- Computer Vision
- Data Science
