import streamlit as st
 
with st.form("my_form"):
# Champ de texte obligatoire
    nom = st.text_input(
    label="Nom",
    placeholder="Entrez votre nom",
    key="nom",
    
)

# Bouton de soumission
    submit = st.form_submit_button("Soumettre")

# Afficher les résultatsif submit:

if submit:
    if not nom:
        st.error("Le champ Nom est requis!")
    else:
        st.success(f"Nom saisi : {nom}")

# Afficher les résultatsif submit:
