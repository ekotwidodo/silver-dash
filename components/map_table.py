import pandas as pd
import streamlit as st
import os

def get_path(path_file):
    return os.path.join(os.getcwd() + '/datasets/' + path_file)

def show_table():
    df = pd.read_excel(get_path("index_category.xlsx"))
    # Display the dataframe as a table in Streamlit
    df['KODE_KAB'] = df['KODE_KAB'].astype(str).str.zfill(2)
    df["IDKAB"] = df["KODE_PROV"].astype(str) + df["KODE_KAB"].astype(str)
    df_selected = df[["NAMA_KAB","health","economy","education","index","category"]]
    df_selected = df_selected.sort_values(by='index', ascending=True)
    df_selected.columns = ["NAMA", "DIM_HEALTH", "DIM_ECONOMY", "DIM_EDUCATION", "INDEKS", "KATEGORI"]
    st.dataframe(df_selected)  # You can use st.table(df) for a static table