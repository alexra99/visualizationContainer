import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("Impacto mediático")

twitter_tab, news_tab,  = st.tabs(["Twitter", "Noticias"])
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
        
    st.subheader('Análisis de sentimiento')
    st.image('news/benzemaGraph.png', width=1500)
    st.dataframe(df_news)

        
with twitter_tab:
    df_tweets = pd.read_json("tweets/analysis.json")
    st.subheader("Tweets relacionados con el jugador Karim Benzema")
    st.markdown("\n")
    col10, col20 = st.columns([7,15])
    with col10:
        components.html(
            """
            <rssapp-carousel id="RPJF30ANICGSysLY"></rssapp-carousel><script src="https://widget.rss.app/v1/carousel.js" type="text/javascript" async></script>
            """,
            height=730
    )
    with col20:
        st.subheader("Tweets analizados")
        accounts =["@OptaJoe","@OptaJohan","@OptaJoao","@OptaFranz","@OptaJack","@OptaPaolo","@OptaJean","@GaryLineker","@GuillemBalague","@sidlowe","@WhoScored""@GregLeaFootball","@SamMcGuire90","@Ciaran_Mc_1","@LaurensJulien","@MatchoftheDave","@BenDinnery","@Carra23","@SkySportsPL","@SkyFootball","@JamesPearceLFC","@MARCAinENGLISH","@emctear","@mattcannon97","@TheAthleticFC","@TheSunFootball","@TimesSport","@btsportfootball","@JackRosser_","@AroundTGrounds","@SandraBrobbey78"]
        st.multiselect("CUENTAS", accounts)
        st.markdown(f"**Total:** {df_tweets.shape[0]}")
        #st.dataframe(df_tweets, height=210)
        # Registro con más Me gusta
        max_likes_index = df_tweets['Likes'].idxmax()
        max_likes_df = df_tweets.loc[max_likes_index:max_likes_index]

        # Registro con más Retweets
        max_retweets_index = df_tweets['Retweets'].idxmax()
        max_retweets_df = df_tweets.loc[max_retweets_index:max_retweets_index]
        st.markdown("**Tweet con más me gusta**:")
        df1 = st.dataframe(max_likes_df)
        st.markdown('**Análisis de sentimiento:** Muy positivo')
        st.markdown(f"**Tweet con más retweets:**")
        df2 = st.dataframe(max_retweets_df)
        st.markdown('**Análisis de sentimiento:** Muy positivo')
    
    st.subheader("Palabras más utilizadas:")
    st.image("tweets/tweets_words.png")
    
    st.subheader("Analísis general de sentimiento en tweets")
    st.image("tweets/sentiment_graph.png")
    st.dataframe(df_tweets)
       

        
  
   
 
 

 