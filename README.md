
# Loan Approval Prediction

## InternSpark - Task 2

### Project Overview

This project uses supervised machine learning to predict whether a loan application is likely to be approved or rejected based on borrower information.

### Objectives

- Perform data cleaning and preprocessing.
- Handle missing values.
- Encode categorical variables.
- Scale numerical features.
- Handle class imbalance using SMOTE.
- Train and compare multiple machine learning models.
- Evaluate model performance using Precision, Recall, F1-score and ROC-AUC.
- Provide business-oriented interpretations.

### Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Imbalanced-learn
- Jupyter Notebook

### Machine Learning Models

1. Logistic Regression
2. Decision Tree
3. Random Forest

### Project Structure

```text
Loan-Approval-Prediction/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── loan_approval_analysis.ipynb
├── src/
│   └── inspect_data.py
├── outputs/
├── figures/
├── requirements.txt
├── README.md
└── .gitignore
```

### How to Run

1. Download the dataset from Kaggle.
2. Place the CSV file inside data/raw/.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Open the Jupyter Notebook.
5. Run all cells from beginning to end.

### Evaluation

The project compares machine learning models using:

- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion Matrix

Actual evaluation results are generated when the notebook is executed.

### Conclusion

This project demonstrates how supervised machine learning can help analyse historical loan application data and support data-driven decision-making.

The model is an educational prototype and should not be used for actual lending decisions without appropriate fairness, legal and regulatory validation.
