# Adey Innovations Inc. Fraud Detection System

## 📌 Project Overview
As a Data Scientist at **Adey Innovations Inc.**, this project focuses on enhancing transaction security by developing sophisticated fraud detection models. The system targets two distinct financial domains: **E-commerce transactions** and **Bank credit transactions**. 

The primary objective is to accurately identify fraudulent activities while maintaining a delicate balance between security and user experience—minimizing financial loss without alienating customers through false positives.

## 🔍 Core Challenges
* **Extreme Class Imbalance:** Fraudulent transactions represent a tiny fraction of the total data (e.g., ~0.17% in bank data), requiring specialized techniques like SMOTE and robust evaluation metrics like AUC-PR.
* **Behavioral Mimicry:** Fraudsters often replicate the purchasing habits and demographic profiles of legitimate users, making advanced feature engineering essential.
* **Real-time Requirements:** The system is designed to support efficient monitoring and reporting to allow for rapid risk mitigation.

## 🛠️ Technical Approach
This project follows a systematic workflow to transform raw data into actionable business intelligence:

1.  **Data Preprocessing & Cleaning:** Handling missing values, removing duplicates, and integrating geolocation data through IP-to-country mapping.
2.  **Feature Engineering:** Extracting temporal patterns (time-since-signup, hour of day) and transaction velocity (frequency per device/user).
3.  **Advanced Modeling:** Implementing baseline Logistic Regression and advanced Ensemble models (Random Forest, XGBoost, or LightGBM).
4.  **Resampling Strategy:** Applying SMOTE (Synthetic Minority Over-sampling Technique) to address class imbalance during training.
5.  **Model Explainability (XAI):** Utilizing **SHAP** to interpret model decisions, ensuring transparency and providing clear business recommendations.



## 🎯 Learning Outcomes
* Mastering the end-to-end machine learning pipeline for highly imbalanced data.
* Justifying model selection based on both technical performance and business context.
* Developing actionable security recommendations based on model insights.
