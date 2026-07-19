import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# 1. Page Configuration & Setup
st.set_page_config(page_title="Fleet Diagnostics Dashboard", layout="wide")
st.title("🚚 Fleet Performance & Fuel Optimization Dashboard")

# Load Datasets from specific tabs
@st.cache_data
def load_data():
    # 1. Get the directory where this script is running in the cloud
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Build the absolute file path dynamically based on the directory
    filename = "TechScoutLabs_DataAnalyst_Practical_Dataset_Enhanced.xlsx"
    file_path = os.path.join(current_dir, filename)
    
    # 3. Double check case-insensitive match if it still struggles
    if not os.path.exists(file_path):
        # Look for the file in the current working directory as a fallback
        file_path = filename 

    # Load the core fleet records and fuel anomaly logs
    fleet_df = pd.read_excel(file_path, sheet_name="Fleet_Data")
    fuel_df = pd.read_excel(file_path, sheet_name="Fuel_Events")
    return fleet_df, fuel_df

df, fuel_df = load_data()

# Clean up date objects for continuity
df["Date"] = pd.to_datetime(df["Date"])

# 2. Interactive Slicer (Sidebar)
st.sidebar.header("Dashboard Filters")
selected_vehicle = st.sidebar.multiselect(
    "Select Vehicle ID:", 
    options=sorted(df["Vehicle_ID"].unique()), 
    default=df["Vehicle_ID"].unique()
)

# Apply dynamic filtering to datasets
filtered_df = df[df["Vehicle_ID"].isin(selected_vehicle)]
filtered_fuel_df = fuel_df[fuel_df["Vehicle_ID"].isin(selected_vehicle)]

# 3. Top Row: Fleet KPIs
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
with kpi1:
    st.metric("Total Distance (KM)", f"{filtered_df['Distance_KM'].sum():,.2f}")
with kpi2:
    st.metric("Total Fuel Consumed (L)", f"{filtered_df['Fuel_Consumed_L'].sum():,.2f}")
with kpi3:
    # Average path discipline across the selection
    avg_compliance = filtered_df['Route_Compliance_Pct'].mean()
    st.metric("Avg Route Compliance", f"{avg_compliance:.2f}%")
with kpi4:
    # Custom efficiency measure matching DAX logic
    if filtered_df['Fuel_Consumed_L'].sum() > 0:
        efficiency = filtered_df['Distance_KM'].sum() / filtered_df['Fuel_Consumed_L'].sum()
    else:
        efficiency = 0
    st.metric("Fleet Efficiency (KM/L)", f"{efficiency:.2f}")

st.markdown("---")

# 4. Middle Row: Trends & Vehicle Analytics
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Daily Fleet Fuel Consumption Trend")
    daily_trend = filtered_df.groupby("Date")["Fuel_Consumed_L"].sum().reset_index()
    fig_trend = px.line(daily_trend, x="Date", y="Fuel_Consumed_L")
    fig_trend.update_traces(line_shape="spline", line_color="#d65f5f") # Smooth line formatting
    st.plotly_chart(fig_trend, width="stretch")

with col2:
    st.subheader("🎯 Vehicle Performance Comparison")
    # Aggregate to match the scatter point per unique asset
    vehicle_perf = filtered_df.groupby("Vehicle_ID").agg({
        "Distance_KM": "sum",
        "Fuel_Consumed_L": "sum"
    }).reset_index()
    
    fig_scatter = px.scatter(
        vehicle_perf, x="Distance_KM", y="Fuel_Consumed_L", 
        hover_data=["Vehicle_ID"], color_discrete_sequence=["#7a7a52"]
    )
    st.plotly_chart(fig_scatter, width="stretch")

# 5. Bottom Row: Behavioral Analytics & Gauge
col3, col4 = st.columns(2)

with col3:
    st.subheader("⏱️ Idle Time Analysis by Driver")
    idle_driver = filtered_df.groupby("Driver_Name")["Idle_Time_Hrs"].sum().reset_index()
    idle_driver = idle_driver.sort_values(by="Idle_Time_Hrs", ascending=False)
    fig_bar = px.bar(idle_driver, x="Driver_Name", y="Idle_Time_Hrs", color_discrete_sequence=["#e07a5f"])
    st.plotly_chart(fig_bar, width="stretch")

with col4:
    st.subheader("🗺️ Overall Route Compliance Benchmark")
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=avg_compliance,
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [0, 100], 'ticksuffix': "%"},
            'bar': {'color': "#3b4cc0"},
            'steps': [
                {'range': [0, 92.53], 'color': "#f4f4f4"},
                {'range': [92.53, 100], 'color': "#e2eafc"}
            ],
        }
    ))
    st.plotly_chart(fig_gauge, width="stretch")