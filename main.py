import streamlit as st
import pandas as pd
from sklearn.datasets import fetch_california_housing
import plotly.express as px

# Load the California Housing dataset
california = fetch_california_housing(as_frame=True)
df = california.frame


pages = {
    "Main Dashboard": [
    st.Page("one/test.py", title="Main Projects"),
    st.Page("one/dua.py", title="Page two")
    ],
    "Penguin": [
        st.Page("penguin/main-app.py", title="Penguin Dataset"),
    ],

}

pg = st.navigation(pages)
pg.run()
