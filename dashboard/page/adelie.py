import streamlit as st
from data.get_data import get_species_all, get_island, get_island_all

def adelie():
    st.title("Adélie Penguin")
    st.header("Un poquito sobre mi")
    st.subheader("Este soy yo:")
    st.image('https://cdn.download.ams.birds.cornell.edu/api/v1/asset/362643231/900')
    st.subheader("Mi hogar")
    isla = st.selectbox("hola", get_island_all())
    st.write(f"En la isla {isla} hay {len(get_island(isla))} pinguinos de la especie Adélie")