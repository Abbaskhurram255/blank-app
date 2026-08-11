import pandas as pd
import plotly.express as px
import streamlit as st

gapm = px.data.gapminder()

st.title("🎈 My new app")
st.write(
    gapm
)
