# Importation des bibliothèques nécessaires
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Fonction principale pour appliquer le clustering
def apply_clustering():
    # Chargement des fichiers de données
    brands_by_country = pd.read_csv('data/mobile-phone-brands-by-country.csv')
    best_selling_phones_2020 = pd.read_csv('data/Best Selling Mobile Phones 2020.csv')

    # Renommer les colonnes pour simplifier la fusion
    best_selling_phones_2020 = best_selling_phones_2020.rename(columns={"Company": "Brand", "Sold(million)": "Units_Sold"})

    # Fusion des données par marque
    merged_data = pd.merge(brands_by_country, best_selling_phones_2020, on="Brand", how="inner")
    merged_data = merged_data.drop(columns=['No', 'Phone'])  # Suppression des colonnes inutiles

    # Préparation des données pour le clustering
    region_dummies = pd.get_dummies(merged_data['Region'])
    data_for_clustering = pd.concat([region_dummies, merged_data[['Units_Sold']]], axis=1)

    # Normalisation des données
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data_for_clustering)

    # Application de k-means avec le nombre optimal de clusters (ici 3)
    optimal_clusters = 3
    kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
    clusters = kmeans.fit_predict(scaled_data)

    # Ajout des clusters aux données pour l'analyse
    merged_data['Cluster'] = clusters

    # Tracé des clusters avec les noms des marques
    plt.figure(figsize=(10, 6))
    for cluster in merged_data['Cluster'].unique():
        clustered_data = merged_data[merged_data['Cluster'] == cluster]
        plt.scatter(clustered_data['Units_Sold'], clustered_data.index, label=f'Cluster {cluster}', alpha=0.6)

    # Ajouter des annotations avec les noms des marques
    for i, row in merged_data.iterrows():
        plt.annotate(row['Brand'], (row['Units_Sold'], i), textcoords="offset points", xytext=(5, -5), ha='center')

    plt.xlabel('Ventes (en millions)')
    plt.ylabel('Index des observations')
    plt.title('Segmentation du Marché par Clusters avec les Noms des Marques')
    plt.legend()
    plt.grid(True)
    plt.show()

# Exécution de la fonction principale
if __name__ == '__main__':
    apply_clustering()
