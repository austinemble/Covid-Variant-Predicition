import streamlit as st
from dash import dcc
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
allCountry = pd.read_csv("Datasets/By Country/India--CovidData.csv")
df = px.data.gapminder()
fig = px.line(allCountry, x="date", y="perc_sequences",  line_group="variant", hover_name="perc_sequences",color='variant', line_shape="spline", render_mode="svg")
st.plotly_chart(fig) 
