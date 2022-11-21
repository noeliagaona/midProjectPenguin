import streamlit as st
from data.get_data import get_species_all, get_island, get_island_all, get_island_by_penguin

def chinstrap():
    st.title("Pinguino Chinstrap")
    st.subheader("Este soy yo:")
    st.image('https://cdn.download.ams.birds.cornell.edu/api/v1/asset/362646391/900')
    st.subheader("Tengo muchos amigos repartidos por estas islas tan bonitas que pertenecen al Archipiélago Palmer que es un archipiélago del océano Glacial Antártico que se encuentra en la Antártida.")
    isla = st.selectbox("", get_island_all())
    if isla == "Dream":
        st.image('https://i.ytimg.com/vi/6w7QEeVHTJQ/maxresdefault.jpg')
        st.subheader(f"En la isla {isla} hay {len(get_island_by_penguin('Chinstrap', isla))} pinguinos como yo!")
    elif isla == "Biscoe":
        st.image("https://media.sciencephoto.com/e2/25/00/27/e2250027-800px-wm.jpg")
        st.subheader(f"En la isla {isla} hay {len(get_island_by_penguin('Chinstrap', isla))} pinguinos como yo!")
    elif isla == "Torgersen":
        st.image("https://media.venturatravel.org/unsafe/800x600/smart/b5faac46-3550-4d92-9112-a95474cd7ca8-drawimage.jpeg")
        st.subheader(f"En la isla {isla} hay {len(get_island_by_penguin('Chinstrap', isla))} pinguinos como yo!")
