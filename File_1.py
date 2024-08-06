# mes importations
import streamlit as st
import pandas as pd

st.markdown("### Ceci est un titre énorme")

# un message de bienvenue
st.write("Bonjour DIT, comment allez vous ? Ici tout va bien")



# un dataframe
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

# affichage du dataframe
st.write(df)