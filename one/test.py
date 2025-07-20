import streamlit as st
import pandas as pd
from sklearn.datasets import fetch_california_housing
import plotly.express as px

# Load the California Housing dataset
california = fetch_california_housing(as_frame=True)
df = california.frame

# Dashboard title
st.title("California Housing Data Dashboard")

# --- Sidebar ---
st.sidebar.header("Dashboard Controls")
feature_choice = st.sidebar.radio(
    "Select Feature for Row 1, Column 1",
    ["Total Records", "Another Feature"],
)

# --- First Row ---
st.subheader("Row 1")
col1_row1, col2_row1, col3_row1 = st.columns(3)

with col1_row1:
    if feature_choice == "Total Records":
        st.metric("Total Records", len(df))
    else:
        st.subheader("Another Feature")
        st.write("This section can be customized to display different information or visualizations based on user selection.")
        # You can add any other Streamlit elements here for the "Another Feature" option
        st.write(f"For example, you could show the average of another column: ${df['HouseAge'].mean():.2f} Average House Age")

with col2_row1:
    median_house_value = df['MedHouseVal'].median()
    st.metric("Median House Value", f"${median_house_value:,.2f}")

with col3_row1:
    average_income = df['MedInc'].mean()
    st.metric("Average Income", f"${average_income:.2f}")

# --- Second Row ---
st.subheader("Row 2")
col1_row2, col2_row2, col3_row2 = st.columns(3)

with col1_row2:
    # Available categories for grouping
    categorical_features = ['HouseAge', 'HousingMedianAge']
    selected_category = st.selectbox("Select Category for Grouping", categorical_features)

    st.subheader(f"Grouped Data by {selected_category}")
    grouped_data = df.groupby(selected_category)['MedHouseVal'].mean().reset_index()
    st.dataframe(grouped_data)

with col2_row2:
    st.subheader(f"Average House Value by {selected_category}")
    if selected_category:
        fig = px.bar(grouped_data, x=selected_category, y='MedHouseVal',
                     title=f'Average Median House Value by {selected_category}')
        st.plotly_chart(fig)
    else:
        st.warning("Please select a category for the chart.")

with col3_row2:
    st.subheader("Distribution of Housing Median Age")
    fig_hist = px.histogram(df, x='HouseAge', title='Distribution of Housing Median Age')
    st.plotly_chart(fig_hist)
