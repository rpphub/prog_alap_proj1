import streamlit as st

st.set_page_config(
  page_title="Programozási alapok beadandó",
  page_icon=":bar_chart:",
)

with st.sidebar:
    st.page_link('main.py', label='Project', icon=':material/bar_chart:')
    st.page_link('pages/about.py', label='Készítők', icon=':material/handshake:')

st.markdown(
    """
    ### A projektett készítették
    - Pollák Róbert Patrik - **LJOKYT**
    - Váraljai Levente - **C4MKGQ**
    - Katona Milán - **L6FLWO**
    - Varga Zoltán Péter - **Z70FTG**
    """
)
