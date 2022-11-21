import streamlit as st
def quiz():
    st.title("Let see what have you learned")
   
    st.subheader('PREGUNTA 1')
    question_one = st.radio(
     "Dónde podemos encontrar la isla Dream?",
     ('Escoge uno','Islas Canarias', 'Archipielago Indonesia', 'Archipielago Palmer')) 

    if st.button('SOLUCIÓN'):
        if question_one == 'Archipielago Palmer':
            st.write('Buen trabajo!')
        
        elif question_one=='Escoge uno':
            st.write('Escoge una opción')
        else:
            st.write('Respuesta equivocada, prueba otra vez!')
  

    st.subheader('PREGUNTA 2')
    question_two = st.radio(
    "De que tres especies de pinguinos hemos hablado en este proyecto?",
    ('Escoge uno','Gentoo, Chinstrap, Adelie', 'Snares, Gentoo, Adelie', 'Macaroni, Emperor, African')) 

    if st.button('SOLUCIÓN',key=1):
        if question_two == 'Gentoo, Chinstrap, Adelie':
            st.write('Buen trabajo!')
        
        elif question_two=='Escoge uno':
            st.write('Escoge una opción')
        else:
            st.write('Respuesta equivocada, prueba otra vez!')


    st.subheader('PREGUNTA 3')
    question_three = st.radio(
    "Que pinguino pesa más de media?",
    ('Escoge uno','Gentoo','Chinstrap','Adelie')) 

    if st.button('SOLUCIÓN',key=2):
        if question_three == 'Gentoo':
            st.write('Buen trabajo!')
        
        elif question_three=='Escoge uno':
            st.write('Escoge una opción')
        else:
            st.write('Respuesta equivocada, prueba otra vez!')