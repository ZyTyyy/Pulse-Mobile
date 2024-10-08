import pandas as pd

# Charger tous les fichiers CSV
df_mobile_sales = pd.read_csv('data/mobile_sales.csv')
df_best_selling_2020 = pd.read_csv('data/Best Selling Mobile Phones 2020.csv')
df_best_selling = pd.read_csv('data/best-selling-mobile-phones.csv')
df_brands_by_country = pd.read_csv('data/mobile-phone-brands-by-country.csv')
df_total_devices_by_company = pd.read_csv('data/total-phone-devices-by-company-2021.csv')

# Fonction de nettoyage de base pour chaque dataset
def clean_data(df, file_name):
    print(f"\nNettoyage des données pour : {file_name}")
    
    # Remplir les valeurs manquantes de manière appropriée pour chaque type de colonne
    for col in df.columns:
        if df[col].dtype == 'object':  # Colonnes texte
            df[col].fillna('Inconnu', inplace=True)
        elif df[col].dtype in ['int64', 'float64']:  # Colonnes numériques
            df[col].fillna(0, inplace=True)
    
    # Conversion de types si nécessaire
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    
    # Suppression des doublons si nécessaire
    df.drop_duplicates(inplace=True)
    
    # Aperçu des données nettoyées
    print(df.info())
    print(df.head())
    
    return df

# Appliquer le nettoyage à chaque dataset
df_mobile_sales_cleaned = clean_data(df_mobile_sales, 'mobile_sales.csv')
df_best_selling_2020_cleaned = clean_data(df_best_selling_2020, 'Best Selling Mobile Phones 2020.csv')
df_best_selling_cleaned = clean_data(df_best_selling, 'best-selling-mobile-phones.csv')
df_brands_by_country_cleaned = clean_data(df_brands_by_country, 'mobile-phone-brands-by-country.csv')
df_total_devices_cleaned = clean_data(df_total_devices_by_company, 'total-phone-devices-by-company-2021.csv')

# Sauvegarder les datasets nettoyés (facultatif)
df_mobile_sales_cleaned.to_csv('data/cleaned_mobile_sales.csv', index=False)
df_best_selling_2020_cleaned.to_csv('data/cleaned_best_selling_2020.csv', index=False)
df_best_selling_cleaned.to_csv('data/cleaned_best_selling.csv', index=False)
df_brands_by_country_cleaned.to_csv('data/cleaned_brands_by_country.csv', index=False)
df_total_devices_cleaned.to_csv('data/cleaned_total_devices.csv', index=False)
