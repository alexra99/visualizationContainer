import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
df_passing = pd.read_json('data/passing.json')
df_creation = pd.read_json('data/creation.json')
df_possesion = pd.read_json('data/possesion.json')
df_discipline = pd.read_json('data/discipline.json')
df_defense = pd.read_json('data/defense.json')
df_shooting = pd.read_json('data/shooting.json')

st.title("Temporada 2022/2023")
left, right = st.columns([5,9])
with left:
    components.html(
        """    
                <iframe width="100%" height="710" frameborder="0" scrolling="no" src="https://www.sofascore.com/es/embed/jugador/karim-benzema/3306" id="sofa-player-embed-3306">
                </iframe><script>
                (function (el) {
                window.addEventListener("message", (event) => {
                    if (event.origin.startsWith("https://www.sofascore")) {
                    if (el.id === event.data.id) {
                        el.style.height = event.data.height + "px";
                    }
                    }
                });
                })(document.getElementById("sofa-player-embed-3306"));
                </script>
    
                """,
                    height=500
                )
with right:
    st.empty()
x = 710
st.subheader("Areas de influencia")
st.image("img/players/heatmap/Karim Benzema.png", width=710)
st.subheader("Participación")
col1, col2 = st.columns([2,7])
with col1:
    st.markdown("**Partidos jugados:** 22")
    st.markdown("**Minutos jugados:** 1914")
with col2:
    st.markdown("**Partidos como titular:** 22/22")
    st.markdown("**Partidos como suplente:** 0/22")
st.subheader("Estadísticas avanzadas")
st.markdown("<h5>Pase</h5>", unsafe_allow_html=True)
st.dataframe(df_passing,x)
st.markdown("<h5>Posesión</h5>", unsafe_allow_html=True)
st.dataframe(df_possesion,x)
st.markdown("<h5>Tiros</h5>", unsafe_allow_html=True)
st.dataframe(df_possesion,x)
st.markdown("<h5>Creación de goles</h5>", unsafe_allow_html=True)
st.dataframe(df_creation,x)
st.markdown("<h5>Defensa</h5>", unsafe_allow_html=True)
st.dataframe(df_defense,x)
st.markdown("<h5>Disciplina</h5>", unsafe_allow_html=True)
st.dataframe(df_discipline,x)


