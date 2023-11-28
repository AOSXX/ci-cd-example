import streamlit as st

from api.fast import root

st.write(root())

st.write('TEST TEST TEST. This is obviously very simple, in reality one would rather use this page to display API results more nicely! :)')
