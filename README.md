# 🏥 Hospital Patient Report Generator

## 🎯 Project Overview

This Python script, **`321020.py`**, is designed to load, process, and visualize clinical patient data to generate a single-page, multi-panel report using **Pandas** and **Matplotlib**.

The report provides a high-level summary of the patient population, key clinical metrics, demographic distributions, and doctor workload, outputting the results as a displayed plot and a saved **PDF file (`week7_report.pdf`)**.

-----

## 📁 Project Structure

```
.
├── 321020.py                       # The main Python script for data processing and report generation.
├── merged_output.csv               # The expected input dataset (must be present for live data processing).
├── README.md                       # This file.
└── week7_report.pdf                # The generated output report (after running the script).
```

-----

## ⚙️ Installation and Setup

### Prerequisites

  * **Python 3.x**
  * **Git** (optional, for cloning)

### 1\. Install Dependencies

The script relies on the following Python libraries:

```bash
pip install pandas numpy matplotlib
```

### 2\. Data Requirement

The script attempts to load data from the file path `C:\AI PYTHON\merged_output.csv`.

  * **If the file exists:** The script processes the live data.
  * **If the file does not exist:** The script automatically generates a **sample DataFrame (50 rows)** with synthetic data to demonstrate the dashboard's functionality.

-----

## 🚀 Usage

### 1\. Run the Script

Execute the main Python script from your terminal:

```bash
python 321020.py
```

### 2\. View Output

Upon execution, the script will:

1.  Display the one-page report as an interactive plot window (using `plt.show()`).
2.  Save the complete report as a PDF file named **`week7_report.pdf`** in the same directory.

-----

## ✨ Report Sections & Key Metrics

The generated report features a **3x3 grid** of visualizations and data summaries:

| Panel | Type | Description |
| :--- | :--- | :--- |
| **1. KPI Box** | Text | **Key Performance Indicators** (Total Patients, Avg Age, Avg Hemoglobin, Mean Systolic BP, High-Risk Patients Percentage). |
| **2. Age Group** | Bar Chart | Distribution of patients across predefined age bins (0-20, 21-40, etc.). |
| **3. Gender** | Pie Chart | Distribution of patients by gender. |
| **4. Hemoglobin** | Histogram | Distribution of patient Hemoglobin levels (g/dL). |
| **5. Hb vs Creatinine** | Scatter Plot | Visualizing the correlation between Hemoglobin and Serum Creatinine. |
| **6. Blood Sugar** | Histogram | Distribution of Random Blood Sugar levels. |
| **7. Condition vs Medication** | Heatmap | A cross-tabulation showing the counts of medications prescribed per medical condition. |
| **8. Doctor Workload** | Stacked Bar Chart | Breakdown of each doctor's patient count segmented by medical condition. |
| **9. Summary** | Text | Case-based summary of findings and presenter details. |

-----

## 🛠️ Data Processing Highlights

The script performs the following key data preparation steps:

1.  **Age Grouping:** Patients are categorized into 5 fixed age groups.
2.  **BP Extraction:** The **Systolic** Blood Pressure is extracted from the `bp` string column.
3.  **Risk Stratification:** A custom function assigns patients to **"High Risk"**, **"Borderline"**, or **"Normal"** categories based on Blood Sugar and Serum Creatinine levels.

-----

## 👤 Presenter Details

  * **Name:** V. HIMACHAND
  * **Roll No:** 321020
  * **Date:** The current date will be included in the report.

-----
