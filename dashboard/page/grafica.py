import streamlit as st
from data.get_data import get_penguins_by_isla, get_island_all,get_media_peso, get_species_all
import plotly.express as px

def grafica():
    op1 = st.selectbox('Seleccione el grafico que desea mostrar', ["Población por islas", "Distribción por peso medio"])
    if op1 == "Población por islas":
        info = get_penguins_by_isla()
        isla = get_island_all()
        valores = []
        for i in isla:
            valores.append(info[i])
            
        fig = px.pie(values=valores, names=isla, title='Población por islas')
        st.plotly_chart(fig)
    if op1 == "Distribción por peso medio":
        info = get_media_peso()
        pinguin = get_species_all()
        valores = []
        for i in pinguin:
            valores.append(info[i])
            
        fig = px.pie(values=valores, names=pinguin, title='Distribución por peso medio')
        st.plotly_chart(fig)