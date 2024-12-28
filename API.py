import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

# Configuration de l'application
st.title("Gestion de budget pour PAC")
st.subheader("Suivi des dépenses journalières, mensuelles et annuelles")

# Recette fixe mensuelle
recette_mensuelle = 75000

# Nom du fichier CSV pour sauvegarder les données
FICHIER_CSV = "budget_pac_donnees.csv"

# Fonction pour charger les données depuis un fichier CSV
def charger_donnees():
    if os.path.exists(FICHIER_CSV):
        return pd.read_csv(FICHIER_CSV)
    else:
        return pd.DataFrame(columns=["Date", "Mois", "Année", "Dépenses (FCFA)"])

# Fonction pour sauvegarder les données dans un fichier CSV
def sauvegarder_donnees(df):
    df.to_csv(FICHIER_CSV, index=False)

# Charger les données au démarrage
df = charger_donnees()

# Ajouter une dépense quotidienne
def ajouter_depense_journaliere(date, depense):
    global df
    date = pd.to_datetime(date)
    mois = date.strftime("%B %Y")
    annee = date.year
    nouvelle_donnee = pd.DataFrame({
        "Date": [date],
        "Mois": [mois],
        "Année": [annee],
        "Dépenses (FCFA)": [depense]
    })
    df = pd.concat([df, nouvelle_donnee], ignore_index=True)
    sauvegarder_donnees(df)

# Calculer les dépenses totales par mois
def calculer_depenses_totales_par_mois():
    if not df.empty:
        return df.groupby("Mois")["Dépenses (FCFA)"].sum().reset_index()
    else:
        return pd.DataFrame(columns=["Mois", "Dépenses Totales (FCFA)"])

# Calculer les dépenses totales par année
def calculer_depenses_totales_par_annee():
    if not df.empty:
        return df.groupby("Année")["Dépenses (FCFA)"].sum().reset_index()
    else:
        return pd.DataFrame(columns=["Année", "Dépenses Totales (FCFA)"])

# Graphique de suivi des dépenses
def tracer_courbe(df, niveau):
    plt.figure(figsize=(10, 6))
    if niveau == "journalier":
        plt.plot(df["Date"], df["Dépenses (FCFA)"], marker="o", linestyle="-", label="Dépenses journalières")
        plt.xlabel("Date")
        plt.ylabel("Dépenses (FCFA)")
        plt.title("Suivi des dépenses journalières")
    elif niveau == "mensuel":
        depenses_par_mois = calculer_depenses_totales_par_mois()
        plt.plot(depenses_par_mois["Mois"], depenses_par_mois["Dépenses Totales (FCFA)"], marker="o", linestyle="-", label="Dépenses mensuelles")
        plt.xlabel("Mois")
        plt.ylabel("Dépenses Totales (FCFA)")
        plt.title("Suivi des dépenses mensuelles")
    elif niveau == "annuel":
        depenses_par_annee = calculer_depenses_totales_par_annee()
        plt.plot(depenses_par_annee["Année"], depenses_par_annee["Dépenses (FCFA)"], marker="o", linestyle="-", label="Dépenses annuelles")
        plt.xlabel("Année")
        plt.ylabel("Dépenses Totales (FCFA)")
        plt.title("Suivi des dépenses annuelles")
    plt.legend()
    plt.grid()
    st.pyplot(plt)

# Interface utilisateur
st.sidebar.header("Ajouter des dépenses")
depense_date = st.sidebar.date_input("Date de la dépense")
depense_montant = st.sidebar.number_input("Montant de la dépense (FCFA)", min_value=0, step=100)

if st.sidebar.button("Ajouter une dépense quotidienne"):
    ajouter_depense_journaliere(str(depense_date), depense_montant)
    st.sidebar.success("Dépense ajoutée avec succès !")

# Affichage des dépenses journalières
st.header("Dépenses journalières")
if not df.empty:
    st.dataframe(df)
else:
    st.info("Aucune dépense journalière enregistrée pour le moment.")

# Graphique de suivi
st.header("Courbes de suivi des dépenses")
niveau = st.radio("Sélectionnez le niveau de suivi :", ["journalier", "mensuel", "annuel"])
if niveau == "journalier" and not df.empty:
    tracer_courbe(df, "journalier")
elif niveau == "mensuel" and not df.empty:
    tracer_courbe(df, "mensuel")
elif niveau == "annuel" and not df.empty:
    tracer_courbe(df, "annuel")
else:
    st.info("Aucune donnée disponible pour tracer la courbe.")

# Réinitialiser les données
if st.sidebar.button("Réinitialiser les données"):
    df = pd.DataFrame(columns=["Date", "Mois", "Année", "Dépenses (FCFA)"])
    sauvegarder_donnees(df)
    st.sidebar.success("Toutes les données ont été réinitialisées !")
import streamlit as st

# Afficher l'image en haut de l'application
st.image(r"C:\Users\DELL\OneDrive\Desktop\Api\Sans titre.jpg", use_column_width=True)

