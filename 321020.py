import pandas as pd
import numpy as np
from datetime import date
import os
import matplotlib.pyplot as plt

# ---------------- Load dataset ----------------
# Try to load the dataset, if not found, create a sample DataFrame for demonstration
csv_path = r"C:\AI PYTHON\merged_output.csv"

if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
else:
    # Create a sample DataFrame with similar structure for demonstration
    np.random.seed(0)
    n = 50
    df = pd.DataFrame({
        'patient_id': range(1, n+1),
        'age': np.random.randint(18, 90, n),
        'gender': np.random.choice(['Male', 'Female', 'Other'], n),
        'bp': np.random.choice(['120/80', '140/90', '130/85', '150/95', '110/70'], n),
        'hemoglobin': np.round(np.random.normal(13.5, 2, n), 1),
        'random_blood_sugar': np.round(np.random.normal(150, 50, n)),
        'serum_creatinine': np.round(np.random.normal(1.0, 0.3, n), 2),
        'condition': np.random.choice(['Diabetes', 'Hypertension', 'CKD', 'Anemia'], n),
        'medication': np.random.choice(['Metformin', 'Amlodipine', 'EPO', 'Insulin', 'None'], n),
        'doctor_name': np.random.choice(['Dr. Rao', 'Dr. Singh', 'Dr. Patel', 'Dr. Lee'], n)
    })

# ---------------- Data Preparation ----------------
# Age groups
df['age_group'] = pd.cut(df['age'], bins=[0,20,40,60,80,100],
                         labels=["0-20","21-40","41-60","61-80","81-100"])

# Extract systolic BP
df['systolic'] = df['bp'].str.split('/').str[0].astype(float)

# Risk category
def risk_category(row):
    if row['random_blood_sugar'] >= 200 or row['serum_creatinine'] > 1.5:
        return "High Risk"
    elif 140 <= row['random_blood_sugar'] < 200 or 1.2 <= row['serum_creatinine'] <= 1.5:
        return "Borderline"
    else:
        return "Normal"
df['risk'] = df.apply(risk_category, axis=1)

# Condition vs Medication matrix
cond_med = pd.crosstab(df['condition'], df['medication'])

# Doctor workload
doctor_condition = df.groupby(['doctor_name','condition']).size().unstack(fill_value=0)

# ---------------- KPI Calculations ----------------
total_patients = df['patient_id'].nunique()
avg_age = round(df['age'].mean(), 1)
avg_hb = round(df['hemoglobin'].mean(), 1)
avg_bp = round(df['systolic'].mean(), 1)
high_risk_pct = round((df['risk'].value_counts(normalize=True).get("High Risk",0) * 100),1)

# ---------------- Dashboard Layout ----------------
fig, axes = plt.subplots(3, 3, figsize=(22, 14))
fig.suptitle("Hospital Patient Report (One Page)", fontsize=20, fontweight="bold")

# 1. KPI Box
kpi_text = f"""
🩺    Total Patients: {total_patients}
🩺    Avg Age: {avg_age} yrs
🩺    Avg Hemoglobin: {avg_hb} g/dL
🩺    Mean Systolic BP: {avg_bp} mmHg
🩺    High-Risk Patients: {high_risk_pct} %
"""
axes[0,0].text(0.05, 0.5, kpi_text, fontsize=14, va="center", ha="left",
               bbox=dict(facecolor="linen", alpha=0.5))
axes[0,0].axis("off")

# 2. Bar Graph: Age Group Distribution
df['age_group'].value_counts().sort_index().plot(kind='bar', ax=axes[0,1], color="crimson", edgecolor="black")
axes[0,1].set_title("Age Group Distribution")

# 3. Pie Chart: Gender Distribution
gender_counts = df['gender'].value_counts()
axes[0,2].pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%',
              colors=['orchid','pink','lightgreen'])
axes[0,2].set_title("Gender Distribution")

# 4. Histogram: Hemoglobin Distribution
axes[1,0].hist(df['hemoglobin'], bins=10, color="maroon", edgecolor="black")
axes[1,0].set_title("Hemoglobin Distribution")
axes[1,0].set_xlabel("Hemoglobin (g/dL)")

# 5. Scatter: Hb vs Creatinine
axes[1,1].scatter(df['hemoglobin'], df['serum_creatinine'], color="brown", alpha=0.6)
axes[1,1].set_title("Hb vs Creatinine Correlation")
axes[1,1].set_xlabel("Hemoglobin (g/dL)")
axes[1,1].set_ylabel("Serum Creatinine (mg/dL)")

# 6. Histogram: Blood Sugar
axes[1,2].hist(df['random_blood_sugar'], bins=15, color="peru", edgecolor="black")
axes[1,2].set_title("Blood Sugar Distribution")

# 7. Heatmap: Condition vs Medication
im = axes[2,0].imshow(cond_med.values, cmap="YlGnBu")
axes[2,0].set_xticks(range(len(cond_med.columns)))
axes[2,0].set_yticks(range(len(cond_med.index)))
axes[2,0].set_xticklabels(cond_med.columns, rotation=90)
axes[2,0].set_yticklabels(cond_med.index)
axes[2,0].set_title("Condition vs Medication")
fig.colorbar(im, ax=axes[2,0])

# 8. Stacked Bar Chart: Doctor Workload
bottom_vals = [0] * len(doctor_condition)
colors = plt.cm.Set2.colors
for idx, col in enumerate(doctor_condition.columns):
    axes[2,1].bar(doctor_condition.index, doctor_condition[col],
                  bottom=bottom_vals, label=col, color=colors[idx % len(colors)])
    bottom_vals = [i+j for i,j in zip(bottom_vals, doctor_condition[col])]
axes[2,1].set_title("Doctor Workload by Condition")
axes[2,1].legend(fontsize=7)

# 9. Case Summary + Presenter Details
summary_text = f"""
📝    Case-based Summary:
- Patients with lowest Hb and highest 
  creatinine suggest possible renal dysfunction.
- High proportion of patients in 41-60 yrs age group.
- Risk stratification highlights {high_risk_pct}% high-risk patients.
- Workload distribution shows uneven burden across doctors.

👨‍⚕️    Presenter Details:
Name: V. HIMACHAND
Roll No: 321020
Date: {date.today().strftime('%d-%m-%Y')}
"""
axes[2,2].text(0.05, 0.5, summary_text, fontsize=12, va="center", ha="left",
               bbox=dict(facecolor="darkturquoise", alpha=0.5))
axes[2,2].axis("off")

# ---------------- Save & Show ----------------
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("week7_report.pdf")
plt.show()
