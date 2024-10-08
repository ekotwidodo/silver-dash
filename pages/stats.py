import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from components import stats_stacked_bar_chart, stats_pyramid_plot, stats_projection_plot, stats_box_plot
import os

def get_path(path_file):
    return os.path.join(os.getcwd() + '/datasets/' + path_file)

def app():
    st.markdown("## General Information of Elderly Population")

    st.markdown("We provide general information about the elderly population.")

    """
    PYRAMID PLOT
    """
    st.markdown("### 1. Distribution of the Elderly Population")
    st.markdown("Description here")
    # Convert the dictionary to a DataFrame
    df_pyramid = pd.read_excel(get_path("Population_Projection_2050.xlsx"))
    df_pyramid2024 = df_pyramid[["Age Group", "Male_2024", "Female_2024"]]
    df_pyramid2024.columns = ["Age Group", "Male", "Female"]
    df_pyramid2050 = df_pyramid[["Age Group", "Male_2050", "Female_2050"]]
    df_pyramid2050.columns = ["Age Group", "Male", "Female"]
    
    first_pyramid, second_pyramid =  st.columns(2)
    with first_pyramid:
        st.plotly_chart(stats_pyramid_plot.plot_pyramid(df_pyramid2024, 2024))

    with second_pyramid:
        st.plotly_chart(stats_pyramid_plot.plot_pyramid(df_pyramid2050, 2050))
    
    """
    LINE CHART
    """
    st.markdown("### 2. Projection of the Elderly Population")
    st.markdown("Description here")

    df_line = pd.read_excel(get_path("proyeksi penduduk.xlsx"))
    st.plotly_chart(stats_projection_plot.plot_population_projection(df_line))
    
    """
    STACKED BAR CHART
    """
    st.markdown("### 3. Elderly by Household Structure")
    st.markdown("Description here")
    df_stacked_bar = pd.read_excel(get_path("klasifikasi struktur ruta lansia by provinsi.xlsx"))
    # Display the stacked bar chart in Streamlit
    st.plotly_chart(stats_stacked_bar_chart.plot_stacked_bar_chart(df_stacked_bar))

    """
    BOX PLOT
    """
    st.markdown("### 4. Health Expenditure over Non-Food Expenditure")
    st.markdown("Description here")
    df_box = pd.read_excel(get_path("untuk boxplot perbandingan biaya kesehatan.xlsx"))
    st.plotly_chart(stats_box_plot.box_plot(df_box))
    
    st.markdown("Source: Socio-economic Survey (SUSENAS), (BPS-Statistics Indonesia, 2023)")