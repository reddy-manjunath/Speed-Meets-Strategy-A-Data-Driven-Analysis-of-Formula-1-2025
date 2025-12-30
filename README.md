# 🏎️ Formula 1 2025 Data Science Project

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue" />
  <img src="https://img.shields.io/badge/FastF1-Data%20Powered-red" />
  <img src="https://img.shields.io/badge/ML-Scikit--learn-green" />
  <img src="https://img.shields.io/badge/Dashboard-Streamlit-orange" />
</p>

---

## 📑 Table of Contents

* [Overview](#-overview)
* [Objectives](#-objectives)
* [Tech Stack](#-tech-stack)
* [Project Structure](#-project-structure)
* [Data Sources](#-data-sources)
* [Features Extracted](#-features-extracted)
* [Machine Learning Models](#-machine-learning-models)
* [Dashboard Highlights](#-dashboard-highlights)
* [Key F1 Concepts Used](#-key-f1-concepts-used)
* [Outcomes](#-outcomes)
* [Future Improvements](#-future-improvements)
* [Author](#-author)
* [License](#-license)

---

## 📌 Project Title

**Speed Meets Strategy: A Data-Driven Analysis of Formula 1 2025**

---

## 📘 Overview

This project explores the **2025 Formula 1 season** using a combination of **Exploratory Data Analysis (EDA)**, **Machine Learning**, and **interactive dashboards**. It covers how physics, race strategy, car engineering, driver performance, and weather influence race outcomes.

The goal is to convert raw F1 data into meaningful insights and **strategy-focused predictive models**, enabling a deeper understanding of how **race strategies are planned and executed** under different conditions.

---

## 🎯 Objectives

* Analyze 2025 F1 race data (laps, telemetry, pit stops, weather)
* Understand performance patterns across drivers and teams
* Study tire strategies, pit timing, downforce effects, and consistency
* Build ML models to predict:

  * Pit stop count (1-stop / 2-stop / 3-stop)
  * First pit stop lap (pit window)
  * Tire compound sequence (strategy type)
  * Strategy effectiveness (positions gained/lost)
* Create an interactive dashboard to visualize insights
* Use storytelling to explain why drivers win or lose

---

## 🧰 Tech Stack

* **Python**
* **FastF1** (main data source)
* **Pandas, NumPy**
* **Matplotlib, Seaborn, Plotly**
* **Scikit-learn (ML)**
* **Streamlit (dashboard)**

---

## 📂 Project Structure

```
F1-2025-Analysis/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── exported/
│
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_feature_engineering.ipynb
│   └── 04_ml_models.ipynb
│
├── dashboard/
│   └── app.py
│
├── reports/
│   └── final_report.pdf
│
├── fastf1_cache/
│
└── README.md
```

---

## 🔍 Data Sources

### **FastF1 Library**

Used for collecting:

* Lap times
* Sector performance
* Telemetry (speed, gear, throttle, braking)
* Pit stop events
* Tire compounds
* Weather

### **Ergast API**

Used for:

* Race results
* Driver standings
* Constructor standings

---

## 📊 Features Extracted

* LapTime, SectorTimes
* Speed, Throttle, Brake usage
* Tire Compound, TireLife
* PitInTime, PitOutTime, PitStopCount
* Weather: AirTemp, TrackTemp, Rain
* GridPosition, RacePosition, Overtakes
* RaceStint patterns

---

## 🤖 Machine Learning Models

* **Random Forest / XGBoost Classifier** (Pit Stop Count Prediction)
* **XGBoost Regressor** (First Pit Stop Lap Prediction)
* **Multiclass Classifier** (Tire Strategy Type)
* **Logistic Regression** (Strategy Effectiveness Classification)

---

## 📺 Dashboard Highlights

Built using **Streamlit**, featuring:

* Driver Performance Tracker
* Team Comparison
* Tire Strategy Visualizer
* Lap Time Consistency Heatmaps
* Strategy Recommendation Panel based on historical patterns

---

## 🧠 Key F1 Concepts Used

* Downforce and aerodynamic drag
* DRS impact on overtakes
* Tire degradation physics
* Fuel load effects
* Weather and grip levels
* Mechanical grip vs aerodynamic grip
* Race strategy (undercut, overcut)

These concepts are explained in the storytelling sections of the project.

---

## 🏁 Outcomes

By the end of this project, you will have:

* A strategy-focused race analytics system
* ML models that predict **historically effective race strategies**
* A Streamlit dashboard for strategy exploration
* Strong storytelling combining physics, strategy, and data
* A portfolio-ready project demonstrating decision-support modeling skills

---

## ⚠️ Limitations

**This project does **not** claim to provide optimal or real-time race strategies. It predicts **historically effective strategy patterns under similar conditions**, based on past race data and early-race indicators. Unpredictable events such as late safety cars, sudden weather changes, team orders, and real-time driver feedback are not modeled due to data access limitations. The project is therefore positioned as a **historical decision-support and pattern-learning system**, not a real-time optimization engine.
**
---

## 💡 Future Improvements

* Add telemetry-based driver aggression score
* Add multi-year comparison (2022–2025)
* Integrate social sentiment analysis

---

## 👤 Author

**Manjunath Reddy**

---

## 📜 License

This project is created for educational and portfolio purposes.
