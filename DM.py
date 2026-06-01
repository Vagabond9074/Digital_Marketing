import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Clients & Calls Dashboard", layout="wide")

st.title("Clients and Call Lists Dashboard")

# Load data
@st.cache_data
def load_data():
    df_clients = pd.read_csv("clients.csv")
    df_calls = pd.read_csv("call_lists.csv")
    return df_clients, df_calls

df_clients, df_calls = load_data()

st.header("Clients Data")

st.subheader("Dataset Preview")
st.dataframe(df_clients, use_container_width=True)

st.subheader("Clients Dataset Information")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Rows", df_clients.shape[0])

with col2:
    st.metric("Columns", df_clients.shape[1])

with col3:
    st.metric("Missing Values", df_clients.isna().sum().sum())

st.subheader("Clients Columns")
st.write(df_clients.dtypes)

st.subheader("First Client Row")
st.write(df_clients.loc[0])

st.divider()

st.header("Call Lists Data")

st.subheader("Dataset Preview")
st.dataframe(df_calls, use_container_width=True)

st.subheader("Calls Dataset Information")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Rows", df_calls.shape[0])

with col2:
    st.metric("Columns", df_calls.shape[1])

with col3:
    st.metric("Missing Values", df_calls.isna().sum().sum())

st.subheader("Calls Columns")
st.write(df_calls.dtypes)

st.subheader("First Call Row")
st.write(df_calls.loc[0])
