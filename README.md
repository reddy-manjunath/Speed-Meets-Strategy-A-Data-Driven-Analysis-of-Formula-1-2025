# 🏎️ Formula 1 2025 Data Science Project

---

## 📑 Table of Contents
- Overview  
- Objectives  
- Tech Stack  
- Project Structure  
- Data Sources  
- Features Extracted  
- Machine Learning Models  
- Dashboard Highlights  
- Key F1 Concepts Used  
- Outcomes  
- Limitations  
- Future Improvements  
- Author  

---

## 📌 Project Title
###                                                 **Speed Meets Strategy: A Data-Driven Analysis of Formula 1 (2025)**

---

## 📘 Overview

This project explores the **2025 Formula 1 season** using a combination of **Exploratory Data Analysis (EDA)**, **Machine Learning**, and **interactive dashboards**.

The focus of the project is to understand **how race strategies are historically planned and executed**, rather than simply predicting race winners. It analyzes how **pit stops, tyre strategies, driver consistency, car performance, and race conditions** influence outcomes over the course of a race weekend.

The project converts raw Formula 1 data into **meaningful insights and strategy-focused predictive models**, enabling deeper understanding of decision-making in motorsport.

---

## 🎯 Objectives

- Analyze 2025 Formula 1 race data (laps, pit stops, weather, results)
- Understand performance patterns across drivers and teams
- Study tyre strategies, pit timing, consistency, and race evolution
- Build machine learning models to predict **historical strategy patterns**, including:
  - Pit stop count (1-stop / 2-stop / 3-stop)
  - First pit stop lap (pit window)
  - Tyre compound sequence (strategy type)
  - Strategy effectiveness indicators (finish position / points context)
- Create an interactive dashboard for strategy exploration
- Use storytelling to explain **why strategies succeed or fail**, not just who wins

---

## 🧰 Tech Stack

- Python  
- FastF1 (primary race data source)  
- Pandas, NumPy  
- Matplotlib, Seaborn, Plotly  
- Scikit-learn (machine learning)  
- Streamlit (interactive dashboard)  
- Google BigQuery (analytics & feature storage)  

---

## 📂 Project Structure

```text
F1-2025-Analysis/
│
├── data/
│   ├── raw/              # Raw FastF1 & results data
│   ├── processed/        # Cleaned & feature-ready datasets
│   └── exported/         # CSV / Parquet exports
│
├── notebooks/
│   ├── 01_Working_notebook.ipynb
│
├── dashboard/
│   └── app.py            # Streamlit dashboard
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

* LapTime, Sector1/2/3 Times
* Tyre Compound, Tyre Life, Stints
* PitInTime, PitOutTime, Pit Stop Count
* First Pit Stop Lap
* Average Pit Duration
* Grid Position, Finish Position, Points
* Driver and team performance aggregates
* Weather context (air temperature, track temperature, rain flags)

---

## 🤖 Machine Learning Models
The project uses interpretable, lightweight models focused on historical strategy behavior.

<img width="787" height="136" alt="{90B89681-4C02-479F-98DA-C3DB2CFEE605}" src="https://github.com/user-attachments/assets/4f6237c1-3b86-497e-ac0e-b150ded65fa1" />

Note : ⚠️ These models do not predict optimal strategies.
They learn historical strategy patterns under similar race conditions.
---

## 📺 Dashboard Highlights

The Streamlit dashboard enables interactive exploration of race strategies:

* Driver Performance Tracker
* Team-level strategy comparison
* Tyre Strategy Visualizer
* Lap time consistency and degradation analysis
* Strategy pattern prediction panel based on historical data
* Model evaluation plots (actual vs predicted, distributions)
* The dashboard is designed as a decision-support and storytelling tool, not a real-time race    simulator.
  
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

**This project does not claim to provide optimal or real-time race strategies.**

It predicts historically effective strategy patterns based on past race data and early-race indicators. Unpredictable events such as:

* Late safety cars
* Sudden weather changes
* Team orders
* Real-time driver feedback
are not modeled due to data access limitations.

**The project is positioned as a historical decision-support and pattern-learning system, not a real-time optimization engine.**

---

## 💡 Future Improvements

* Add telemetry-based driver aggression score
* Add multi-year comparison (2022–2025)
* Integrate social sentiment analysis

---

## 👤 Author

**Manjunath Reddy**

