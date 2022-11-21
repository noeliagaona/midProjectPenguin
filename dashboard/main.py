import streamlit as st
from data.get_data import get_species_all
from page.adelie import adelie
from page.chinstrap import chinstrap
from page.gentoo import gentoo
from page.conoce_a_los_pinguinos import meet
from page.inicio import inicio
from page.grafica import grafica
from page.quiz import quiz


columna = st.sidebar.selectbox("Escoge la página", ["Inicio", 'Conoce a los pinguinos', "Adélie", "Gentoo", "Chinstrap", 'Gráficas', 'Quiz'])

if columna == "Inicio":
    inicio()

if columna == "Adélie":
    adelie()

if columna == "Chinstrap":
    chinstrap()
    
if columna == "Gentoo":
    gentoo()  

if columna== 'Conoce a los pinguinos':
    meet()

if columna== "Gráficas":
    grafica()

if columna== "Quiz":
    quiz()