import streamlit as st
from data.get_data import get_species_all
from page.adelie import adelie


columna = st.sidebar.selectbox("Escoge la página", ["Inicio", "Adélie", "Gentoo", "Chinstrap", 'Meet the penguins'])

if columna == "Inicio":
    st.title("Bienvenido al inicio")
    st.header('Palmers Penguins')
    st.image('https://miro.medium.com/max/1248/1*xJ6_zgmEEfI2BT0sRXP5cw.png')
    st.subheader("Mi hogar")
    st.text('El archipiélago Palmer es un archipiélago del \nocéano Glacial Antártico que se encuentra en la Antártida,\nadyacente y muy próximo a la costa noroeste de la península Antártica.')

if columna == "Adélie":
    adelie()


if columna == "Chinstrap":
    st.title("Chinstrap Penguin")
    st.header("Un poquito sobre mi")
    st.image('https://cdn.download.ams.birds.cornell.edu/api/v1/asset/362646391/1800')
    st.subheader("Mi hogar")

if columna == "Gentoo":
    st.title("Gentoo Penguin")
    st.header("Un poquito sobre mi")
    st.image('https://cdn.download.ams.birds.cornell.edu/api/v1/asset/115369831/1800')
    st.subheader("Mi hogar")


if columna== 'Meet the penguins':
    st.title("Palmer`s Penguins")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header(list(specie_penguins().keys())[2])
        st.image('https://upload.wikimedia.org/wikipedia/commons/b/be/Pygoscelis_papua.jpg')
        st.text('''
        Kingdom: Animalia
        Phylum:	 Chordata
        Class:	 Aves
        Order:	 Sphenisciformes
        Family:  Spheniscidae
        Genus:	 Pygoscelis
        Species: P. papua
        '''
        )


    with col2:
        st.header(list(specie_penguins().keys())[1])
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/South_Shetland-2016-Deception_Island%E2%80%93Chinstrap_penguin_%28Pygoscelis_antarctica%29_04.jpg/330px-South_Shetland-2016-Deception_Island%E2%80%93Chinstrap_penguin_%28Pygoscelis_antarctica%29_04.jpg')
        st.text('''
        Kingdom: Animalia
        Phylum:	Chordata
        Class:	Aves
        Order:  Sphenisciformes
        Family: Spheniscidae
        Genus:	Pygoscelis
        Species: P. adeliae
            '''
        )
     
   
   
   
    with col3:
        st.header(list(specie_penguins().keys())[0])
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Hope_Bay-2016-Trinity_Peninsula%E2%80%93Ad%C3%A9lie_penguin_%28Pygoscelis_adeliae%29_04.jpg/375px-Hope_Bay-2016-Trinity_Peninsula%E2%80%93Ad%C3%A9lie_penguin_%28Pygoscelis_adeliae%29_04.jpg')
        st.text('''
        Kingdom:  Animalia
        Phylum:	  Chordata
        Class:	  Aves
        Order:	  Sphenisciformes
        Family:	  Spheniscidae
        Genus:	  Pygoscelis
        Species:  P. antarcticus
        '''
        )