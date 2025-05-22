#  Predictive Modeling for Energy Usage 

(Time Series Forecasting)

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Problem Statement](#problem-statement)
- [Approach](#approach)
- [Results](#results)
- [Future Scope](#future-scope)
- [How to Run](#how-to-run)
- [Authors](#authors)

---

## Overview
This project focuses on forecasting electricity consumption using a Long Short-Term Memory (LSTM) network. The goal is to enhance energy management and planning by predicting future usage based on historical trends.

We use six years of hourly electricity consumption data from Finland’s transmission system operator to build and evaluate the model.

---

## Dataset
- **Source:** Fingrid (Finland Transmission Operator)  
- **Period:** 2016–2021  
- **Type:** Univariate time series  
- **Observations:** ~53,000 hourly records  

---

## Problem Statement
To develop an LSTM-based deep learning model capable of predicting future electricity consumption using historical time series data.

---

## Approach
- **Preprocessing:** Selected relevant features, resampled data to daily frequency, and normalized values using `MinMaxScaler`.
- **Model Architecture:** Stacked LSTM with four hidden layers, a `Dropout` layer, and a dense output layer.
- **Training Strategy:** 80/20 train-test split, trained for 60 epochs with a batch size of 20.
- **Evaluation Metric:** Root Mean Squared Error (RMSE).

---

## Results
- The model was successful in capturing seasonal trends in energy usage.
- RMSE indicates potential for improvement through hyperparameter tuning or feature engineering.

---

## Future Scope
- Introduce multivariate features (e.g., weather, public holidays, economic indicators).
- Experiment with GRU, Bidirectional LSTM, or Transformer-based models.
- Deploy the model in a real-time environment such as a smart grid dashboard.
- Use transfer learning for broader regional forecasting applications.

---


## How to Run

### 1. Clone the Repository
git clone https://github.com/mayuri-lakhotia-official/Predictive-Modeling-for-Energy-Usage

cd predictive-energy-usage


### 2. Install Dependencies
It’s recommended to use a virtual environment:

pip install -r requirements.txt


### 3. Run the App or Notebooks
Launch the notebook: jupyter notebook

Run the Gradio app: python app/app_interface.py

---

## Authors
- **Mayuri Lakhotia**
- **Sakshi Kubitkar**
