import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing(as_frame=True)

df = data.frame
