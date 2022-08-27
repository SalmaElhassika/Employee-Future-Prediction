import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as matplot
import seaborn as sns
import streamlit as st
st.set_page_config(layout="wide")
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
  lottie_book = load_lottieurl('https://assets4.lottiefiles.com/temp/lf20_aKAfIn.json')
st_lottie(lottie_book, speed=1, height=200, key="initial")


matplotlib.use("agg")

_lock = RendererAgg.lock


sns.set_style('darkgrid')
row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns(
    (.1, 2, .2, 1, .1))

row0_1.title('Employee Future Prediction')
with row0_2:
    st.write('')

row0_2.subheader(
    'A company s HR department wants to predict whether some customers would leave the company in next 2 years,to reach out for the [Data](https://www.kaggle.com/datasets/tejashvi14/employee-future-prediction), for my notebook click [here!](https://github.com/SalmaElhassika/Employee-Future-Prediction/blob/main/Project.ipynb)')

row1_spacer1, row1_1, row1_spacer2 = st.columns((.1, 3.2, .1))

with row1_1:
    st.markdown("Hey there! Welcome to Tyler's Goodreads Analysis App. This app scrapes")
    st.markdown(
        "**To begin, please enter the link to your [Goodreads profile](https://www.goodreads.com/) (or just use mine!).** 👇")
