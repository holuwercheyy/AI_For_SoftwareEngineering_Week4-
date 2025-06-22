
# AI_For_SoftwareEngineering_Week4-
## 🧠 AI Development Project – Theoretical and Practical Exploration

This project covers a comprehensive introduction to AI using Python and popular libraries such as TensorFlow, PyTorch, Scikit-learn, and spaCy. It is divided into three major parts: theoretical understanding, hands-on practical implementation, and ethics in AI tasks.

# ✅ Part 1: Theoretical Understanding – Summary

## 📌1. Short Answer Questions

3 questions were answered.

Q1: Explain the primary differences between TensorFlow and PyTorch. When would you choose one over the other?

Q2: Describe two use cases for Jupyter Notebooks in AI development.

Q3: How does spaCy enhance NLP tasks compared to basic Python string operations?

## 📌2. Comparative Analysis: Scikit-learn vs TensorFlow

```
| Feature         | Scikit-learn                        | TensorFlow                          |
| --------------- | ----------------------------------- | ----------------------------------- |
| **Target Use**  | Classical ML: SVM, Random Forests   | Deep Learning: Neural Networks      |
| **Ease of Use** | Very beginner-friendly              | Steeper learning curve              |
| **Community**   | Strong in academia and ML tutorials | Large global backing + industry use |
```

# ✅ Part 2: Practical Implementation – Detailed Summary & Responses

## 🔷 Task 1: Classical Machine Learning with Scikit-learn

We Used Scikit-learn to build a Decision Tree Classifier to predict iris flower species. 
Our Outcome: A simple, interpretable ML model capable of classifying iris species with decent performance using basic metrics.

# 🔷 Task 2: Deep Learning with TensorFlow/PyTorch (MNIST Classification)

We Build a CNN (Convolutional Neural Network) to classify handwritten digits from the MNIST dataset.
Outcome: A performant CNN achieving >95% accuracy, with sample predictions visualized to demonstrate understanding of model performance.


# Task3: Predictive Analytics for Resource Allocation

## Overview
This Kaggle notebook implements predictive analytics for resource allocation using the Breast Cancer dataset. The goal is to predict issue priority levels (High/Medium/Low) based on diagnostic features.

## Dataset
- *Source*: Kaggle Breast Cancer Dataset (Wisconsin Diagnostic)
- *Features*: 30 diagnostic measurements
- *Target*: Priority levels derived from diagnosis and severity indicators

## Methodology

### 1. Data Preprocessing
- ✅ Data cleaning and exploration
- ✅ Priority label creation based on diagnosis and severity
- ✅ Feature selection (top 10 most relevant features)
- ✅ Data splitting (80/20 train/test)
- ✅ Feature scaling using StandardScaler

### 2. Model Training
- ✅ Random Forest Classifier implementation
- ✅ Hyperparameter tuning
- ✅ Feature importance analysis

### 3. Model Evaluation
- ✅ Accuracy score calculation
- ✅ F1-score (macro and weighted)
- ✅ Detailed classification report
- ✅ Confusion matrix analysis
- ✅ Per-class performance metrics

## Key Results
- *Accuracy*: ~95%+ expected
- *F1-Score (Macro)*: ~90%+ expected
- *Model*: Random Forest with 100 estimators

## Files Structure
```
├── scripts/
│   ├── breast-cancer-predictive-analytics.py  # Main analysis
│   ├── data-visualization.py                  # Visualizations
│   └── model-comparison.py                    # Model comparison
└── README.md                                  # This file
```

## Usage Instructions
1. Run breast-cancer-predictive-analytics.py for main analysis
2. Run data-visualization.py for charts and plots
3. Run model-comparison.py for model benchmarking

## Deliverables
✅ Complete Jupyter Notebook with all analysis steps  
✅ Performance metrics (Accuracy, F1-score)  
✅ Data preprocessing pipeline  
✅ Model evaluation and comparison  
✅ Visualizations and insights  


## Team Members:

- [Brian Ouko](https://github.com/WellBrian)
- [Mmabath Naseba](https://github.com/Mmabatho)
- [Hisserhah Holuwercheyy](https://github.com/holuwercheyy)
- [Letshego Sephiri](https://github.com/CaramelF)
- [Christopher Obegi](https://github.com/mechriz)
