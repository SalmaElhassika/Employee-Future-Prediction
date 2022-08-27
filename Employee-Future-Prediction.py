import altair as alt
from matplotlib.backends.backend_agg import RendererAgg
import pandas as pd
import numpy as np
import seaborn as sns
import requests
import streamlit as st
import scipy.stats
from scipy.stats import norm
import altair as alt
from dataclasses import dataclass
from typing import Optional
from pathlib import Path
import matplotlib
from matplotlib.figure import Figure

st.set_page_config(
    page_title="Employee_FuturPrediction", page_icon="💼", initial_sidebar_state="expanded"

)
st.write(
    """
# 💼 Employee_FuturPrediction
Hey, To begin upload your experiment results to see the significance of your Employee_Prediction👇.
"""
)
uploaded_file = st.file_uploader("Upload CSV", type=".csv")

sns.set_style('darkgrid')
row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns(
    (.1, 2, .2, 1, .1))

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.markdown("### Data preview")
    st.dataframe(df.head(10))

    ab_default = None
    result_default = None
   

    st.markdown("### Select columns for analysis")
    with st.form(key="my_form"):
        ab = st.multiselect(
            "First variable",
            options=df.columns,
            help="Select which column refers to your first variable.",
            default=ab_default,
        )
        
        result = st.multiselect(
            "Result column",
            options=df.columns,
            help="Select which column shows the result of the test.",
            default=result_default,
        )
      

        with st.expander("Adjust test parameters"):
            st.markdown("### Parameters")
            st.radio(
                "Hypothesis type",
                options=["One-sided", "Two-sided"],
                index=0,
                key="hypothesis",
                help="TBD",
            )
            st.slider(
                "Significance level (α)",
                min_value=0.01,
                max_value=0.10,
                value=0.05,
                step=0.01,
                key="alpha",
                help=" The probability of mistakenly rejecting the null hypothesis, if the null hypothesis is true. This is also called false positive and type I error. ",
            )


        submit_button = st.form_submit_button(label="Submit")
    
      # type(uploaded_file) == str, means the example file was used
    name = (
        "Upload CSV" if isinstance(uploaded_file, str) else uploaded_file.name
    )
    st.write("")
    st.write("## Results from ", name)
    st.write("")

    st.write('')
