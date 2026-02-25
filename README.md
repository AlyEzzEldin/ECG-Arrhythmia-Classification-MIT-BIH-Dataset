# ECG-Arrhythmia-Classification-MIT-BIH-Dataset

## Overview

This project implements an end-to-end biomedical signal processing and machine learning pipeline for arrhythmia detection using the MIT-BIH Arrhythmia Database.

The objective is to classify ECG recordings into Normal and Abnormal rhythms through structured signal preprocessing, feature extraction, and supervised learning.

This repository demonstrates practical application of:
- Digital signal processing
- Heart rate variability (HRV) feature engineering
- Machine learning model development
- Quantitative performance evaluation

---

## Dataset

The MIT-BIH Arrhythmia Database contains annotated ECG recordings sampled at 360 Hz.

Each record includes:
- Raw ECG waveform
- Beat annotations
- Arrhythmia labels

For this project:
- Selected ECG records were preprocessed
- R-peaks were detected
- HRV-based statistical features were extracted
- A binary classification dataset was constructed

---

## Methodology

### 1. Signal Preprocessing

The ECG signals were cleaned using:

- Baseline wander removal  
- Notch filtering (50 Hz) to suppress power-line interference  
- Bandpass filtering (0.5–40 Hz) to retain physiological frequency components  

These steps improve signal quality prior to feature extraction.

---

### 2. R-Peak Detection

R-peaks were identified to compute RR intervals.

From RR intervals, the following Heart Rate Variability (HRV) features were extracted:

- Mean RR interval  
- SDNN (Standard Deviation of NN intervals)  
- RMSSD (Root Mean Square of Successive Differences)  
- NN50 (Number of successive RR differences > 50 ms)  

These features capture rhythm irregularities relevant to arrhythmia detection.

---

### 3. Feature Engineering

A structured feature dataset was built from extracted HRV metrics.

Steps included:
- Handling missing values
- Feature normalization
- Train/test splitting
- Optional cross-validation

---

### 4. Model Development

A Random Forest classifier was trained to distinguish between:

- Normal rhythm
- Abnormal rhythm

Hyperparameters were tuned experimentally.

---

### 5. Evaluation Metrics

Model performance was evaluated using:

- Accuracy  
- Precision  
- Recall  
- F1-score  
- ROC-AUC  

Confusion matrix and ROC curves were generated for performance visualization.

---

## Results

> Replace the numbers below with your actual results.

- Accuracy: 0.87  
- Precision: 0.85  
- Recall: 0.82  
- F1-score: 0.83  
- ROC-AUC: 0.90  

The model demonstrates strong discriminative capability between normal and arrhythmic ECG patterns based on HRV-derived features.

---

## Repository Structure

ecg-arrhythmia-classification/
│
├── notebooks/ # Exploratory analysis and experiments
├── src/ # Preprocessing, feature extraction, modeling scripts
├── models/ # Saved trained models
├── requirements.txt
└── README.md


---

## Key Skills Demonstrated

- Biomedical signal processing  
- Digital filtering techniques  
- Feature engineering from time-series data  
- Supervised machine learning  
- Model evaluation and performance visualization  
- Reproducible experimental workflow  

---

## Future Improvements

- Multi-class arrhythmia classification  
- Deep learning approaches (1D CNN / LSTM)  
- Cross-patient validation  
- Feature importance analysis  
- Comparison with additional classifiers  

---

## Motivation

This project reflects an interest in applying machine learning techniques to healthcare and biomedical data analysis, with a focus on interpretable and reproducible modeling pipelines.
