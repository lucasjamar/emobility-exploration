import streamlit as st
import streamlit.components.v1 as components
from pivottablejs import pivot_ui
import pandas as pd


st.set_page_config(layout="wide", page_title="E Mobility")
st.title("E Mobility Exploration")

df = pd.read_parquet("aggregated_data.parquet")

print(df)
t = pivot_ui(df)

with open(t.src) as t:
    components.html(t.read(), width=900, height=1000, scrolling=True)
