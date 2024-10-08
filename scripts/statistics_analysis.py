import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger les datasets
df_sales = pd.read_csv('data/mobile_sales.csv')
df_best_selling = pd.read_csv('data/best-selling-mobile-phones.csv')
df_brands_by_country = pd.read_csv('data/mobile-phone-brands-by-country.csv')

# 1. Ventes par marque vs. Répartition géographique
# Fusionner les deux datasets sur la colonne 'Brand' (Marques)
df_combined_geo = pd.merge(df_best_selling, df_brands_by_country, on='Brand', how='left')

# Corrélation des marques les plus vendues par région
plt.figure(figsize=(12, 6))
sns.countplot(x='Brand', hue='Region', data=df_combined_geo)
plt.title('Répartition des marques vendues par région')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('reports/correlation_marques_vs_geographie.png')
plt.show()

# 2. Prix moyen vs. Unités vendues
# Regarder la relation entre le prix et les unités vendues dans 'mobile_sales'
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Price', y='UnitsSold', data=df_sales)
plt.title('Corrélation entre le prix moyen et les unités vendues')
plt.xlabel('Prix moyen (en dollars)')
plt.ylabel('Unités vendues')
plt.tight_layout()
plt.savefig('reports/correlation_prix_vs_unites_vendues.png')
plt.show()

# 3. Répartition géographique des ventes et croissance du marché
# Groupement par région pour identifier les zones de forte croissance
df_geo_sales = df_best_selling.groupby('Region')['units_sold_m'].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(x='Region', y='units_sold_m', data=df_geo_sales)
plt.title('Ventes globales par région')
plt.ylabel('Unités vendues (en millions)')
plt.tight_layout()
plt.savefig('reports/correlation_geographie_vs_croissance.png')
plt.show()

# 4. Données démographiques des clients vs. Type de téléphone
# Analyser la relation entre les données démographiques et le type de téléphone vendu
plt.figure(figsize=(12, 6))
sns.boxplot(x='CustomerAge', y='Price', hue='MobileModel', data=df_sales)
plt.title('Corrélation entre l\'âge du client et le prix des téléphones achetés')
plt.ylabel('Prix')
plt.xlabel('Âge du client')
plt.tight_layout()
plt.savefig('reports/correlation_age_vs_type_telephone.png')
plt.show()
