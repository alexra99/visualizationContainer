import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("Impacto mediático")

news_tab, twitter_tab = st.tabs(["Noticias", "Twitter"])
with news_tab:
    df_news = pd.read_json("news/analysisBenzema.json")
    with open("news/resumeBenzema.txt", "r") as file:
        textResume = file.read()
    st.subheader("Noticias relacionadas con el jugador Karim Benzema")
    col1, col2 = st.columns([5,15])
    with col1:
        components.html(
            """
            <rssapp-carousel id="sAZs63Z7WyBXj7Ld"></rssapp-carousel><script src="https://widget.rss.app/v1/carousel.js" type="text/javascript" async></script>
            """,
            height=440
    )
    with col2:
        st.empty()
        st.subheader('Texto Analizado:')
        st.write(df_news.loc[0, 'Text'])
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.subheader("Resumen generado:")
        st.write(textResume)
    col3, col4 = st.columns(2)
    with col3:       
        st.subheader('Análisis de sentimiento')
        st.image('news/analysisGraph.png', width=500)
    with col4:
        st.subheader('WordCloud')
        st.image('news/wordcloud.png', width=400)
        
 