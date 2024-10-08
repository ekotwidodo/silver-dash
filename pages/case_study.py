import pandas as pd
import geopandas as gpd
import folium
from folium.plugins import MarkerCluster
import streamlit as st
from streamlit_folium import folium_static
import os

def get_path(path_file):
    return os.path.join(os.getcwd() + '/datasets/' + path_file)

def get_kode_kab(row):
    prov = row[["KODE_PROV"]]
    str_kab = str(row[["KODE_KAB"]])
    kab = f"0{str_kab}" if len(str()) < 2 else str_kab
    return int(f"{prov}{kab}")

def app():
    st.markdown("## Case Study: DI YOGYAKARTA")
    st.markdown("Description")

    faskes_bpjs_df = pd.read_csv(get_path("faskes_bpjs_kako_bps.csv"))
    map_diy = gpd.read_file(get_path("map/diy.geo.json"))
    indeks_diy = pd.read_excel(get_path("index_category.xlsx"))

    new_df = faskes_bpjs_df[['kode_bps','propname', 'kab_bps','kabname', 'kdppk', 'nmppk', 'nmjlnppk', 'jnsppk', 'telpppk', 'lat', 'lng', 'jmldokter', 'jmldoktergigi', 'jmlperawat', 'jmlbidan']]

    # Filter data faskes_bpjs_df untuk mendapatkan kode_bps = "34"
    filtered_faskes_df = new_df[(new_df['kode_bps'] == 34) & (new_df["kab_bps"].notnull())]
    filtered_indeks_df = indeks_diy[indeks_diy['KODE_PROV'] == 34]

    filtered_indeks_df['KODE_KAB'] = filtered_indeks_df['KODE_KAB'].astype(str).str.zfill(2)
    filtered_indeks_df["IDKAB"] = filtered_indeks_df["KODE_PROV"].astype(str) + filtered_indeks_df["KODE_KAB"].astype(str)
    filtered_indeks_df["IDKAB"] = filtered_indeks_df["IDKAB"].astype('int64')

    # merged_data = map_diy.merge(filtered_indeks_df, on='IDKAB')
    merged_data = pd.concat([map_diy, filtered_indeks_df])

    # Konversi dataframe faskes_bpjs_df menjadi GeoDataFrame
    # Pastikan kolom 'latitude' dan 'longitude' ada di dataset
    gdf_faskes = gpd.GeoDataFrame(
        filtered_faskes_df, 
        geometry=gpd.points_from_xy(filtered_faskes_df.lng, filtered_faskes_df.lat),
        crs="EPSG:4326"
    )

    # Membuat peta dengan folium
    m = folium.Map(location=[-7.7956, 110.3695], zoom_start=10)  # Lokasi peta DIY

    # Tambahkan layer choropleth untuk indeks
    folium.Choropleth(
        geo_data=merged_data,
        name='Indeks per KabKota',
        data=merged_data,
        columns=['IDKAB', 'index'],
        key_on='feature.properties.IDKAB',
        fill_color='YlGn',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Indeks per Kabupaten/Kota'
    ).add_to(m)

    # Tambahkan GeoJSON dari map_diy ke peta
    folium.GeoJson(map_diy).add_to(m)

    # Tambahkan marker dari filtered_faskes_df
    marker_cluster = MarkerCluster().add_to(m)
    # Iterasi melalui setiap fasilitas kesehatan dalam dataframe terfilter
    for idx, row in gdf_faskes.iterrows():
        folium.Marker(
            location=[row.geometry.y, row.geometry.x],  # Latitude dan Longitude
            popup=f"Name: {row['nmppk']}\nAlamat: {row['nmjlnppk']}\nCategory: {row['jnsppk']}\nDoctors: {row['jmldokter']}\nDentists: {row['jmldoktergigi']}\nNurse: {row['jmlperawat']}\nPediatric: {row['jmlbidan']}",  # Menggunakan kolom nama_faskes sebagai popup
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(marker_cluster)

    # Tambahkan control untuk menyalakan atau mematikan layer
    folium.LayerControl().add_to(m)

    # Tampilkan peta menggunakan folium_static di Streamlit
    st.markdown("**Mapping Health Facilities in DI YOGYAKARTA**")
    folium_static(m)

    st.markdown("**Table Elderly Vulnerability Index in DI YOGYAKARTA**")
    df = pd.read_excel(get_path("index_category.xlsx"))
    df = df[df["KODE_PROV"] == 34]
    df['KODE_KAB'] = df['KODE_KAB'].astype(str).str.zfill(2)
    df["IDKAB"] = df["KODE_PROV"].astype(str) + df["KODE_KAB"].astype(str)
    df_selected = df[["NAMA_KAB","health","economy","education","index","category"]]
    df_selected = df_selected.sort_values(by='index', ascending=True)
    df_selected.columns = ["NAMA", "DIM_HEALTH", "DIM_ECONOMY", "DIM_EDUCATION", "INDEKS", "KATEGORI"]
    st.dataframe(df_selected)  # You can use st.table(df) for a static table

    st.markdown("**Table Health Facilities in DI YOGYAKARTA**")
    st.dataframe(filtered_faskes_df.head())