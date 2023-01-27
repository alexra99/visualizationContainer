import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit.components.v1 as components


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
    st.subheader("Resultados:")
    player, country, position, team, comp, age = st.columns([5,2.5,3,5,5,2])
    
    with player:
        st.markdown("<h5>Jugador</h5>", unsafe_allow_html=True)
        for index, row in df.iterrows():
            st.button(row["Jugador"], key=f'button_{index}')
    with country:
        st.markdown("<h5>Pais</h5>", unsafe_allow_html=True)
        for index, row in df.iterrows():
            st.button(row["Pais"], key=f'button_{index+10}')
    with position:
        st.markdown("<h5>Posición</h5>", unsafe_allow_html=True)
        for index, row in df.iterrows():
            st.button(row["Posc"], key=f'button_{index+23}')
    with team:
        st.markdown("<h5>Equipo</h5>", unsafe_allow_html=True)
        for index, row in df.iterrows():
            st.button(row["Equipo"], key=f'button_{index+55}')  
    with comp:
        st.markdown("<h5>Liga</h5>", unsafe_allow_html=True)
        for index, row in df.iterrows():
           st.button(row["Comp"], key=f'button_{index+77}')
    with age:
        st.markdown("<h5>Edad</h5>", unsafe_allow_html=True)
        for index, row in df.iterrows():
            st.button(str(row["Edad"]), key=f'button_{index+83}')

###################################################################
def run():
    ###CARGAR DE DATOS
    df_players_all = pd.read_json('data/players.json')
    #TRANSFORMACIONES DE DATOS PARA MOSTRAR
    df_players_overview = df_players_all[['Jugador', 'Pais', 'Posc', 'Equipo', 'Comp', 'Edad', 'Pie']]
    #PAGINA PRINICIPAL
    df_filtered = sidebar_comp(df_players_overview)
    overview_comp(df_filtered)
run()