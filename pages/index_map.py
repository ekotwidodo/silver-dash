import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from components import map_table, map_chloropleth
import os

def get_path(path_file):
    return os.path.join(os.getcwd() + '/datasets/' + path_file)

def app():
    st.markdown("## Analysis of Elderly Vulnerability")

    st.markdown("Description")

    st.markdown("### Distribution of Elderly Vulnerability Index")
    st.markdown("Description here")

    """
    MAP
    """
    map_chloropleth.load_map()

    """
    TABLE
    """
    st.markdown("**Table of Elderly Vulnerability Index**")
    map_table.show_table()