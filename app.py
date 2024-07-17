import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import plotly.express as px

# Charger les données RFM et les résultats du clustering
# Assurez-vous d'avoir calculé les métriques RFM et les clusters K-means comme expliqué précédemment
# Chargez votre propre fichier CSV ici
rfm = pd.read_csv('rfm_online_retail.csv')

# Titre de l'application Streamlit
st.title('Tableau de Bord RFM Clustering')

st.subheader("Cluster")

# Afficher le graphique interactif avec Plotly Express pour tous les clusters
fig2 = px.scatter(rfm, x='Frequency', y='Monetary', color='Cluster Name',
                  title='Données RFM pour tous les clusters',
                  labels={'Recency': 'Récence', 'Monetary': 'Montant'},
                  hover_data=['Recency'])  # Ajoutez des données supplémentaires au survol si nécessaire

st.plotly_chart(fig2)

st.subheader("Filtrer par Cluster")

# Sélection du cluster avec un menu déroulant
selected_cluster_name = st.selectbox('Sélectionner un nom de cluster :', sorted(
    rfm['Cluster Name'].unique()))

# Filtrer les données pour le nom de cluster sélectionné
cluster_data = rfm[rfm['Cluster Name'] == selected_cluster_name]

# Afficher le graphique interactif avec Plotly Express
fig = px.scatter(cluster_data, x='Frequency', y='Monetary', color='Cluster Name',
                 title=f'Données RFM pour {selected_cluster_name}',
                 labels={'Recency': 'Récence', 'Monetary': 'Montant'})

st.plotly_chart(fig)

# Calculer et afficher les statistiques du cluster sélectionné
st.subheader("Analyse du Cluster")
cluster_stats = rfm.groupby('Cluster Name').agg({
    'Recency': 'mean',
    'Frequency': 'mean',
    'Monetary': 'mean'
}).reset_index()

st.write(cluster_stats)

# Affichage supplémentaire si nécessaire
st.subheader("Détails Supplémentaires")

st.subheader("Distribution des clients par cluster")

# Calcul de la distribution des clients par cluster
cluster_distribution = rfm['Cluster Name'].value_counts().reset_index()
cluster_distribution.columns = ['Cluster Name', 'Numbre de clients']

fig3 = px.bar(cluster_distribution, x='Cluster Name', y='Numbre de clients', title='Distribution des clients par cluster', labels={
              'Cluster Name': 'Nom du cluster', 'Numbre de clients': 'Nombre de clients'})
st.plotly_chart(fig3)
