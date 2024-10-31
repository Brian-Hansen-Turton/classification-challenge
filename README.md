# classification-challenge

This project is a spam detection classifier that compares two machine learning models, `LogisticRegression` and `RandomForestClassifier`, to determine which is more effective at identifying spam messages.

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Models Used](#models-used)
- [Setup](#setup)
- [Usage](#usage)
- [Results](#results)
- [Conclusion](#conclusion)

## Overview
This notebook aims to create and compare the performance of two different machine learning models in detecting spam. The models evaluated include:
- **Logistic Regression**: A simple linear model known for its interpretability.
- **Random Forest Classifier**: An ensemble model capable of capturing complex, non-linear relationships.

## Dataset
The dataset used in this project is from the UCI Machine Learning Repository: [Spam Base Dataset](https://archive.ics.uci.edu/dataset/94/spambase). The data has been loaded from a CSV file, which can be accessed [here](https://static.bc-edx.com/ai/ail-v-1-0/m13/challenge/spam-data.csv).

- **Target variable**: `spam`
- **Features**: Various email characteristics (word frequencies, punctuation counts, etc.)

## Models Used
1. **Logistic Regression**: Known for its simplicity and effectiveness in binary classification problems.
2. **Random Forest Classifier**: Known for its ability to handle non-linear data and its robustness in avoiding overfitting.

## Setup
To set up the project locally, follow these steps:

1. Clone the repository or download the notebook.
2. Install the necessary Python packages:
   ```bash
   pip install pandas scikit-learn

