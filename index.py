from importlib import import_module
from pydoc import importfile
import streamlit as st
import navbar
with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

navbar.navBar();