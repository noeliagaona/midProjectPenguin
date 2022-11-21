import streamlit as st

def meet():
    st.title("Pinguinos de Palmer")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Gentoo")
        st.image('https://upload.wikimedia.org/wikipedia/commons/b/be/Pygoscelis_papua.jpg')
        st.text('''
        Reino:   Animalia
        Clase:	 Aves
        Familia: Spheniscidae
        Genero:	 Pygoscelis
        Especie: P.papua
        '''
        )


    with col2:
        st.header("Chinstrap")
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/South_Shetland-2016-Deception_Island%E2%80%93Chinstrap_penguin_%28Pygoscelis_antarctica%29_04.jpg/330px-South_Shetland-2016-Deception_Island%E2%80%93Chinstrap_penguin_%28Pygoscelis_antarctica%29_04.jpg')
        st.text('''
        Reino:   Animalia
        Clase:	 Aves
        Familia: Spheniscidae
        Genero:	 Pygoscelis
        Especie: P.adeliae
            '''
        )
     
   
   
   
    with col3:
        st.header("Adelie")
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Hope_Bay-2016-Trinity_Peninsula%E2%80%93Ad%C3%A9lie_penguin_%28Pygoscelis_adeliae%29_04.jpg/375px-Hope_Bay-2016-Trinity_Peninsula%E2%80%93Ad%C3%A9lie_penguin_%28Pygoscelis_adeliae%29_04.jpg')
        st.text('''
        Reino:   Animalia
        Classe	 Aves
        Familia: Spheniscidae
        Genero:	 Pygoscelis
        Especie: P.antarcticus
        '''
        )