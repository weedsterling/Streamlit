# mes importations
import streamlit as st
import pandas as pd

st.markdown("### Welcome to Data Institute of Technology (DIT)")

# un message de bienvenue
st.write("Bonjour et bienvenue à la DIT, L'école de l'Intelligence Artificielle")



# un dataframe
df = pd.DataFrame({
  'Colonne 1': [1, 2, 3, 4],
  'Colonne 2': [10, 20, 30, 40]
})

# affichage du dataframe
st.write(df)
