import pandas as pd 
import streamlit as st 
import webbrowser as wb
from datetime import datetime
import datetime as dt
import numpy as np

st.set_page_config (
        page_title="Players",
        page_icon="⚽🏃",
        layout="wide" 
)

df_data = pd.read_csv("C:\\Users\\rafael.massaru\\Desktop\\PYTHON\\FIFA\\data\\FIFA23_official_data.csv", index_col=0)
df_data["Contract Valid Until"] = pd.to_datetime(df_data["Contract Valid Until"])
df_filtered = df_data[df_data["Contract Valid Until"].dt.year >= dt.datetime.today().year]
df_data["Value(£)"] = pd.to_numeric(df_data["Value"], errors='coerce')
df_data = df_data.sort_values(by="Overall", ascending=False)


clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube" , clubes)

df_players = df_data[df_data["Club"] == club]
players = df_players["Name"].value_counts().index
player = st.sidebar.selectbox("Jogador" , players)

player_stats = df_data[df_data["Name"] == player].iloc[0]

st.image(player_stats["Photo"])
st.title(f"{player_stats['Name']}")

st.markdown(f"Clube: {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

col1.markdown(f"Idade: {player_stats['Age']}")
col2.markdown(f"Altura: {player_stats['Height']}")
col3.markdown(f"Peso: {player_stats['Weight']}")

st.divider()
st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

col1, col2, col3, col4 = st.columns(4)












