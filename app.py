import streamlit as st
from streamlit_option_menu import option_menu
from pages import stats,index_map, case_study, about

st.set_page_config(
  page_title="Silver-Dash"
)

class MultiPage:
  def __init__(self):
    self.pages = {}

  def add_page(self, title, function):
    self.pages.append({
      "title": title,
      "function": function
    })

  def run():
    with st.sidebar:
      page = option_menu(
        menu_title="Silver-Dash",
        menu_icon="bar-chart-line-fill",
        options=["General", "Analysis", "Case Study", "About"],
        icons=["boxes", "map-fill", "trophy-fill", "info-circle-fill"],
        default_index=0,
        styles={
          "container": {"padding": "5!important","background-color":'#FFEAC5'},
          "icon": {"color": "#603F26", "font-size": "23px"}, 
          "nav-link": {"color":"#000","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#FFDBB5"},
          "nav-link-selected": {"background-color": "#FFDBB5"}
        }
      )

    if page == "General":
      stats.app()
    elif page == "Analysis":
      index_map.app()
    elif page == "Case Study":
      case_study.app()
    elif page == "About":
      about.app()
  run()