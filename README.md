# German Autobahn Traffic Analysis and Bottleneck Detection

## Project Overview

This project analyzes German Autobahn traffic count data provided by the **Bundesanstalt für Straßenwesen (BASt)**.

The project investigates long-term traffic trends on selected Autobahns and proposes a rule-based algorithm to identify potential bottlenecks such as construction zones and high-risk congestion areas.

As an additional extension, a simulated real-time traffic dataset was created to demonstrate how the proposed methodology can be adapted for real-time traffic jam detection.

---

# Project Objectives

This project answers the following research questions:

### 1. Traffic Evolution

* Analyze traffic count data over time for the selected Autobahns:

  * A6
  * A9
  * A93
* Study how traffic evolved between 2003 and 2023.
* Identify traffic trends and growth.
* Compare traffic characteristics between roads.
* Perform correlation analysis between important traffic variables.

### 2. Bottleneck Detection

* Design a rule-based algorithm to identify potential bottlenecks.
* Detect locations affected by:

  * High traffic density
  * Heavy vehicle traffic
  * Construction activities
  * Sudden traffic changes
  * Statistical outliers
* Locate bottlenecks using station information and road coordinates.

### Extension

Since the BASt dataset contains annual traffic statistics rather than real-time measurements, an additional simulated dataset was created to demonstrate real-time traffic jam detection using:

* Vehicle speed
* Road occupancy
* Construction information
* Accident information

---

# Project Structure

```
German_Autobahn_Traffic_Analysis
│
├── data
│   ├── Zeitreihe.csv
│   ├── traffic_cleaned_final.csv
│   ├── cleaned_traffic.csv
│   ├── simulated_realtime_traffic.csv
│   ├── generate_data.py
│   └── descriptionof data.pdf
│
├── notebook
│   ├── 01_Data_Loading.ipynb
│   ├── 01.2_Data_Cleaning.ipynb
│   ├── 02_Exploratory_Data_Analysis.ipynb
│   ├── 03_Traffic_Evolution_pro.ipynb
│   ├── 04_Correlation_Analysis.ipynb
│   ├── 05_Bottleneck_Detection.ipynb
│   ├── 06_Report.ipynb
│   └── 07_Real_Time_Traffic_Jam_Detection.ipynb
│
├── plots
│
├── results
│
├── README.md
└── AI_Usage_Declaration.md
```

---

# Dataset Description

## Original Dataset

The original BASt dataset contains annual traffic statistics collected from traffic counting stations across the German Autobahn network.

Important variables include:

* Year
* Road Number
* Station Name
* Average Daily Traffic (DTV)
* Heavy Vehicle Traffic
* Number of Lanes
* Station Coordinates
* Construction Remarks

This dataset is used for:

* Traffic evolution analysis
* Correlation analysis
* Bottleneck detection

---

## Simulated Dataset

The simulated dataset was generated using `generate_data.py`.

It contains realistic high-frequency traffic information including:

* Timestamp
* Road
* Station
* Vehicle Speed
* Traffic Flow
* Road Occupancy
* Weather
* Construction
* Accident
* Traffic Jam Label

This dataset is used only for demonstrating real-time traffic jam detection.

---

# Notebook Guide

## 01_Data_Loading.ipynb

Purpose:

* Load the BASt traffic dataset.
* Inspect the dataset structure.
* Display basic dataset information.

Input:

* Zeitreihe.csv

Output:

* Loaded DataFrame

---

## 01.2_Data_Cleaning.ipynb

Purpose:

* Clean and preprocess the raw dataset.
* Handle missing values.
* Convert data types.
* Prepare the dataset for analysis.

Input:

* Raw BASt dataset

Output:

* cleaned_traffic.csv

---

## 02_Exploratory_Data_Analysis.ipynb

Purpose:

Explore the dataset by analysing:

* Number of years
* Road distribution
* Traffic stations
* Missing values
* Traffic statistics
* Data quality

---

## 03_Traffic_Evolution_pro.ipynb

Purpose:

Answer Research Question 1.

Main tasks:

* Select Autobahns A6, A9 and A93.
* Calculate yearly average traffic.
* Compare traffic evolution.
* Calculate traffic growth.
* Identify special traffic characteristics.

Outputs:

* Traffic evolution graphs
* Growth statistics
* Road comparison tables

---

## 04_Correlation_Analysis.ipynb

Purpose:

Study relationships between traffic variables.

Analysis includes:

* Pearson Correlation
* Correlation Matrix
* Heatmaps
* Traffic vs Heavy Vehicles
* Truck Percentage Relationships

Outputs:

* Correlation Heatmap
* Correlation Table

---

## 05_Bottleneck_Detection.ipynb

Purpose:

Answer Research Question 2.

The notebook implements a rule-based bottleneck detection algorithm.

The algorithm evaluates:

* Traffic Density
* Heavy Vehicle Percentage
* Construction Information
* Traffic Changes Between Stations
* Traffic Outliers

Each indicator contributes to a risk score that identifies potential bottlenecks.

Outputs:

* Bottleneck Risk Score
* Bottleneck Locations
* Risk Classification

---

## 06_Report.ipynb

Purpose:

Summarize the complete project.

Includes:

* Results
* Conclusions
* Limitations
* Future Work

---

## 07_Real_Time_Traffic_Jam_Detection.ipynb

Purpose:

Extension to the original project.

Uses the simulated traffic dataset to demonstrate real-time traffic jam detection.

Traffic jams are detected using:

* Speed
* Occupancy
* Construction
* Accidents

Outputs:

* Traffic Jam Detection
* Jam Severity
* Jam Locations

---

# Workflow

```
Raw BASt Dataset
        │
        ▼
Data Loading
        │
        ▼
Data Cleaning
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Traffic Evolution Analysis
        │
        ▼
Correlation Analysis
        │
        ▼
Rule-Based Bottleneck Detection
        │
        ▼
Final Report
        │
        ▼
Extension:
Real-Time Traffic Jam Detection
```

---

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Jupyter Notebook

---

# How to Run the Project

1. Clone or download the repository.
2. Install the required Python libraries:

```bash
pip install pandas numpy matplotlib scipy jupyter
```

3. Open the notebooks in the following order:

4. Data Loading

5. Data Cleaning

6. Exploratory Data Analysis

7. Traffic Evolution

8. Correlation Analysis

9. Bottleneck Detection

10. Final Report

11. Real-Time Traffic Jam Detection (Extension)

---

# Results

The project successfully:

* Analyzed long-term traffic evolution on Autobahns A6, A9, and A93.
* Compared yearly traffic trends.
* Calculated traffic growth.
* Identified relationships between important traffic variables.
* Developed a rule-based bottleneck detection algorithm.
* Located potential bottlenecks using traffic statistics and station information.
* Demonstrated an extension for real-time traffic jam detection using simulated traffic data.

---

# Limitations

The BASt dataset contains annual traffic statistics and therefore cannot directly detect real-time traffic jams.

To demonstrate how the proposed approach can be extended, a simulated real-time dataset was generated for the extension notebook.

---

# Authors

**Member 1:** Vikhyath Beecha

**Member 2:** Nithin Reddy Baddam
---

# AI Usage

This project was developed with limited AI assistance for learning, syntax guidance, debugging, and documentation.

For complete details, refer to:

**AI_Usage_Declaration.md**
Used AI ,Github copilot,ChatGPT, and Gemini for coding ,debugging and writing documentations.