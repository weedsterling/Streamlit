# mes importations
import streamlit as st
import pandas as pd

st.markdown("### Welcome to Data Institute of Technology (DIT)")

# un message de bienvenue
st.write("Bonjour et bienvenue à la DIT, L'ecole de l'Intelligence Artificielle")



# un dataframe
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

# affichage du dataframe
st.write(df)