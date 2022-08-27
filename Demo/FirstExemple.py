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
import plotly.express as px
from matplotlib import pyplot as plt

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

use_example_file = st.checkbox(
    "Use example file", False ,help="Use in-built example file to demo the app"
)

st.markdown("### Data preview")  
if use_example_file:
        data_path = Path() / r"C:\Users\Lilly\Desktop\exemple.csv"
        data = pd.read_csv(data_path)
        st.dataframe(data.head())
        st.subheader("ExperienceInCurrentDomain Vs LeaveOrNot::")    
        df= pd.DataFrame(data.groupby(['LeaveOrNot','ExperienceInCurrentDomain'], sort=True).mean()).reset_index()
        fig1 = px.bar(df, x='LeaveOrNot', y='ExperienceInCurrentDomain', height=400)
        barplot_chart = st.write(fig1)
        st.write("Conclusion : "
                "-24.9% of employees have degre 2 of experience leave the company"
                "-18.7% of employees have degre 3 and4 of experience leave the company "
                "-18 % of employees have degre 5 of experience leave the company") 

        st.subheader("ExperienceInCurrentDomain Vs LeaveOrNot:")
        df= pd.DataFrame(data.groupby(['ExperienceInCurrentDomain'], sort=True)["LeaveOrNot"].mean()).reset_index()
        fig1 = px.pie(df, values='LeaveOrNot',height=400)
        barplot_chart = st.write(fig1)


        
       

      
elif uploaded_file:
        data = pd.read_csv(uploaded_file)
        st.dataframe(data.head())
        st.subheader("ExperienceInCurrentDomain Vs LeaveOrNot::")    
        df= pd.DataFrame(data.groupby(['LeaveOrNot','Gender'], sort=True)['ExperienceInCurrentDomain'].mean()).reset_index()
        fig1 = px.bar(df, x='LeaveOrNot', y='ExperienceInCurrentDomain', color="Gender",height=400)
        barplot_chart = st.write(fig1)
        st.write("Conclusion : "
                "-24.9% of employees have degre 2 of experience leave the company"
                "-18.7% of employees have degre 3 and4 of experience leave the company "
                "-18 % of employees have degre 5 of experience leave the company")   

        st.subheader("ExperienceInCurrentDomain Vs LeaveOrNot:")
        df= pd.DataFrame(data.groupby(['ExperienceInCurrentDomain'], sort=True)["LeaveOrNot"].mean()).reset_index()
        fig1 = px.pie(df, values='LeaveOrNot',height=400)
        barplot_chart = st.write(fig1)



          

       