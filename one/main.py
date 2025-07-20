import streamlit as st
import pandas as pd
from sklearn.datasets import fetch_california_housing
import plotly.express as px

# Load the California Housing dataset
california = fetch_california_housing(as_frame=True)
df = california.frame


pages = {
    "Main Dashboard": [st.Page("test.py", title="Main Projects"),
    st.Page("dua.py", title="Page two")],
    "Pages": [
        st.Page("dua.py", title="Manage your account"),
    ],

}

pg = st.navigation(pages)
pg.run()
