import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connexion à la base de données SQLite
conn = sqlite3.connect('students.db')
c = conn.cursor()

# Création de la table si elle n'existe pas
c.execute('''CREATE TABLE IF NOT EXISTS students
             (name TEXT, age INTEGER, major TEXT)''')
conn.commit()

# Navigation
st.sidebar.title("Menu")
page = st.sidebar.radio("Go to", ["Liste des personnes", "Ajout de personne", "Graphique des âges"])

# Page Liste des personnes
if page == "Liste des personnes":
    st.title("Liste des personnes")
    st.write("Voici la liste des personnes.")

    # Sélection de tous les étudiants
    c.execute("SELECT * FROM students")
    students = c.fetchall()

    # Affichage des étudiants dans une table avec en-têtes
    st.write("Liste des étudiants :")
    st.table(pd.DataFrame(students, columns=["Nom", "Âge", "Spécialité"]))

# Page Ajout de personne
elif page == "Ajout de personne":
    st.title("Ajout d'une nouvelle personne")
    st.write("Veuillez entrer les détails sur cette personne:")

    # Formulaire d'ajout
    with st.form(key='add_student_form'):
        name = st.text_input(label='Nom')
        age = st.number_input(label='Âge', min_value=1, max_value=100)
        major = st.text_input(label='Spécialité')
        submit = st.form_submit_button(label="Ajouter")

        if submit:
            c.execute("INSERT INTO students (name, age, major) VALUES (?, ?, ?)",
                      (name, age, major))
            conn.commit()
            st.success(f"Ajouté {name} à la base de données!")

# Page Graphique des âges
elif page == "Graphique des âges":
    st.title("Graphique des âges des étudiants")
    st.write("Voici le graphique représentant les âges des étudiants.")

    # Sélection de tous les étudiants
    c.execute("SELECT name, age FROM students")
    students = c.fetchall()

    # Préparation des données pour le graphique
    names = [student[0] for student in students]
    ages = [student[1] for student in students]

    # Création du graphique
    plt.figure(figsize=(10, 6))
    plt.bar(names, ages, color='skyblue')
    plt.xlabel('Nom')
    plt.ylabel('Âge')
    plt.title('Âge des étudiants')
    plt.xticks(rotation=45, ha='right')

    # Affichage du graphique dans Streamlit
    st.pyplot(plt)

    # Page Statistiques
elif page == "Statistiques":
    st.title("Statistiques des étudiants")
    st.write("Voici quelques statistiques sur les âges des étudiants.")
    
    # Sélection des âges
    c.execute("SELECT age FROM students")
    ages = [row[0] for row in c.fetchall()]
    
    # Calcul des statistiques
    if ages:
        mean_age = pd.Series(ages).mean()
        std_dev_age = pd.Series(ages).std()
        st.write(f"Moyenne des âges: {mean_age:.2f}")
        st.write(f"Écart-type des âges: {std_dev_age:.2f}")
    else:
        st.write("Aucune donnée disponible pour les statistiques.")

conn.close()
