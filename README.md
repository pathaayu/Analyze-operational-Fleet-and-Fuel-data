# Analyze-operational-Fleet-and-Fuel-data\
# 🚚 Operational Fleet Diagnostics & Fuel Optimization Dashboard

A dual-framework (Power BI & Python Streamlit) engineering solution designed to monitor fleet efficiency, analyze driver idling behavior, track route compliance benchmarks, and identify vehicle cost outliers.

---

## 📊 Project Overview
This project delivers an executive-ready business intelligence layer mapped directly to fleet operational metrics. The solution is presented in two distinct formats to satisfy both corporate business requirements and technical software scalability:
1. **Power BI Dashboard (`.pbix`):** The primary corporate reporting artifact optimized for enterprise cross-filtering and executive reviews.
2. **Streamlit Web Application (`.py`):** A custom, standalone programmatic alternative built using Python and Plotly Express to showcase how the pipeline can be scaled out into production web systems.

---

## 🚀 Live Cloud Deployment
The Python implementation of this interactive dashboard has been successfully compiled and deployed to the cloud environment:
🔗 **[Click Here to Access the Live Dashboard]([https://share.streamlit.io/](https://analyze-operational-fleet-and-fuel-data-xxhaucpv5xfup2geznqixq.streamlit.app/))**

---

## 🛠️ Local Python Application Setup
If you prefer to audit or execute the interactive Python app environment locally on your machine, follow these steps:

### 1. Prerequisites
Ensure you have Python 3.10+ installed on your system. 

### 2. Installation
Navigate to your project root folder via your terminal or PowerShell and run the following command to download all required dependencies:
```bash
pip install streamlit pandas plotly openpyxl

python -m streamlit run "Task 5 - Dashboard.py"

📈 Key Visuals Engineered & Analytics Logic
Executive KPI Cards: Tracking core operational health indicators: Total Distance (KM), Total Fuel Consumed (L), Fleet Efficiency (KM/L), and a DAX/Python calculated Average Route Compliance Percentage formatted gracefully to a standard baseline.

Daily Fleet Fuel Consumption Trend: A smoothed line chart tracking daily fleet fuel drawdowns, embedded with an analytics trend baseline to quickly highlight supply variations and anomalies.

Driver Idle Time Rank: A sorted column breakdown mapping total engine idling hours against driver IDs, immediately highlighting top resource targets (e.g., Driver R and Driver K).

Vehicle Performance Scatter Plot: An efficiency quadrant visualization mapping asset distance against asset consumption to locate specific underperforming outliers.

Dynamic Route Compliance Gauge: A fixed-axis benchmark gauge monitoring path adherence accuracy against target milestones.

🗃️ Repository Blueprint
Task 5 - Dashboard.py — Complete core application script utilizing dynamic Plotly metrics.

TechScoutLabs_DataAnalyst_Practical_Dataset_Enhanced.xlsx — Multi-tab underlying data workbook (Fleet_Data & Fuel_Events).

requirements.txt — Cloud system deployment specifications.

README.md — Setup, blueprint, and architectural overview documentation.


***

### 💡 Final Tip for Submission:
Create a new file in your GitHub repository, name it exactly **`README.md`**, paste the text block above insi
