import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def sidebar_comp(df):
    df_filtered = df
    ##FILTRO BUSQUEDA POR NOMBRE 
    search_player = st.sidebar.text_input("Buscar", placeholder='Player name')
    if search_player:
        df_filtered = df.loc[df['Jugador'].str.contains(search_player, case=False, na=False)]
    st.sidebar.header('Filtros de búsqueda')
    
    ##FILTRO BUSQUEDA POR NACIONALIDAD
    countries = df['Pais'].unique()
    selected_countries = st.sidebar.multiselect("Selecciona uno o varias paises", countries)
    if selected_countries:
        df_filtered = df_filtered[df_filtered['Pais'].isin(selected_countries)]
        
    ##FILTRO BUSQUEDA POR LIGA
    ligues = df['Comp'].unique()
    selected_ligues = st.sidebar.multiselect("Selecciona una o varias ligas", ligues)
    teams = df['Equipo'].unique()
    if selected_ligues:
        teams = df[df['Comp'].isin(selected_ligues)]['Equipo'].unique()
        df_filtered = df_filtered[df_filtered['Comp'].isin(selected_ligues)]
        
    ##FILTRO BUSQUEDA POR EQUIPO
    selected_teams = st.sidebar.multiselect("Selecciona uno o varios equipos", teams)
    if selected_teams:
        df_filtered = df_filtered[df_filtered['Equipo'].isin(selected_teams)]

    ##FILTRO BUSQUEDA POR POSICION
    positions = df['Posc'].str.split(',').explode().unique()
    selected_positions = st.sidebar.multiselect("Selecciona una o varias posiciones", positions)
    if selected_positions:
        df_filtered = df_filtered[df_filtered['Posc'].str.contains('|'.join(selected_positions))]
        
    ##FILTRO BUSQUEDA POR PIE
    feet = df['Pie'].unique()
    selected_foot = st.sidebar.multiselect("Selecciona pie dominante", feet)
    if selected_foot:
        df_filtered = df_filtered[df_filtered['Pie'].isin(selected_foot)]
    
    ##FILTRO BUSQUEDA POR EDAD
    min_age = int(df["Edad"].min())
    max_age = int(df["Edad"].max())
    age_range = st.sidebar.slider("Rango de edad", min_value=min_age, max_value=max_age, value=(min_age, max_age))
    if age_range:
        df_filtered = df_filtered[df_filtered["Edad"].between(age_range[0], age_range[1])]
        

    return df_filtered




    
def overview_comp(df):
    st.dataframe(df)
    
###################################################################
def run():
    ###CARGAR DE DATOS
    df_players_all = pd.read_json('data/players.json')
    #TRANSFORMACIONES DE DATOS PARA MOSTRAR
    df_players_overview = df_players_all[['Jugador', 'Pais', 'Posc', 'Equipo', 'Comp', 'Edad', 'Pie']]
    #PAGINA PRINICIPAL
    st.title('Análisis de rendimiento y reputación de jugadores de Fútbol ')
    df_filtered = sidebar_comp(df_players_overview)
    overview_comp(df_filtered)
run()