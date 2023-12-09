import pandas as pd 
import streamlit as st 
import webbrowser as wb
from datetime import datetime
import datetime as dt
import numpy as np


## terminal > streamlit run 1_home.py

st.write('# FIFA23 DATASET ')

df_data = pd.read_csv("C:\\Users\\rafael.massaru\\Desktop\\PYTHON\\FIFA\\data\\FIFA23_official_data.csv", index_col=0)
df_data["Contract Valid Until"] = pd.to_datetime(df_data["Contract Valid Until"])
df_filtered = df_data[df_data["Contract Valid Until"].dt.year >= dt.datetime.today().year]
df_data["Value(£)"] = pd.to_numeric(df_data["Value"], errors='coerce')
df_data = df_data.sort_values(by="Overall", ascending=False)

    
df_data

st.sidebar.write("© Rafael Tanikawa")
btn = st.button("Acesse os dados no Kaggle!")
if btn: 
    wb.open_new_tab("https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database")