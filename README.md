# Financial Risk Analysis System

## Overview
This project is an end-to-end financial analytics system that extracts data from financial reports, computes risk metrics, applies machine learning models, and visualizes insights using Power BI.

## Features
- Excel & PDF financial data extraction
- Financial ratio calculation (ROA, Debt-to-Equity, Liquidity)
- Risk scoring system
- Machine learning models:
  - XGBoost (trend prediction)
  - LSTM (time-series forecasting)
  - Isolation Forest (anomaly detection)
  - KMeans (risk clustering)
- AI-generated financial reports
- FastAPI backend
- Interactive Power BI dashboard

## AI Chatbot (Financial Risk Assistant)

The system includes an AI-powered chatbot that provides explanations and insights based on computed financial data.

Features:
- Answers questions about financial metrics (ROA, leverage, liquidity)
- Explains risk levels and trends
- Uses only system-generated data (no external assumptions)
- Acts as an interactive financial risk tutor

Example Questions:
- What is the current risk level?
- Why is Debt-to-Equity high?
- Explain the trend in ROA
- Which quarter had anomalies?

## System Architecture
1. Data Extraction (Excel/PDF)
2. Data Processing (Pandas)
3. Feature Engineering (Financial Ratios)
4. Machine Learning Analysis
5. API Layer (FastAPI)
6. Visualization (Power BI)

## Dashboard
The Power BI dashboard provides:
- Profit trend analysis
- ROA visualization
- Debt-to-Equity monitoring
- Risk level filtering
- Time-based insights

## How to Run
1. Run the Python script
2. Generate CSV outputs
3. Load CSV into Power BI dashboard

## Author
Sai Siddhanth