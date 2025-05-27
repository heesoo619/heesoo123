import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

st.title("배달 지점 시각화")

df = pd.read_csv("Delivery.csv")

center_lat = df["Latitude"].mean()
center_lon = df["Longitude"].mean()

m = folium.Map(location=[center_lat, center_lon], zoom_start=12)

for i, row in df.iterrows():
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=f"Num: {row['Num']}",
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

folium_static(m)
