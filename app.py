import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import plotly.express as px

# Charger les données RFM et les résultats du clustering
# Assurez-vous d'avoir calculé les métriques RFM et les clusters K-means comme expliqué précédemment
# Chargez votre propre fichier CSV ici
rfm_with_demographics = pd.read_csv('rfm_with_demographics.csv')

# Titre de l'application Streamlit
st.title('Tableau de Bord RFM Clustering')

# Sélection du cluster avec un menu déroulant
selected_cluster_name = st.selectbox('Sélectionner un nom de cluster :', sorted(
    rfm_with_demographics['Cluster Name'].unique()))

# Filtrer les données pour le nom de cluster sélectionné
cluster_data = rfm_with_demographics[rfm_with_demographics['Cluster Name']
                                     == selected_cluster_name]

# Afficher le graphique interactif avec Plotly Express
fig = px.scatter(cluster_data, x='Recency', y='Monetary', color='Cluster Name',
                 title=f'Données RFM pour {selected_cluster_name}',
                 labels={'Recency': 'Récence', 'Monetary': 'Montant'})

st.plotly_chart(fig)

# Calculer et afficher les statistiques du cluster sélectionné
st.subheader("Analyse du Cluster")
cluster_stats = cluster_data.groupby('Cluster Name').agg({
    'Recency': 'mean',
    'Frequency': 'mean',
    'Monetary': 'mean'
}).reset_index()

st.write(cluster_stats)

# Affichage supplémentaire si nécessaire
st.subheader("Détails Supplémentaires")
st.write("Ajoutez ici des détails ou des analyses supplémentaires selon vos besoins.")
