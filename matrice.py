import pandas as pd
import os

# Chemin du dossier contenant les fichiers Excel
folder_path = r"C:\Users\fresn\PythonProject\Matrice teclis\Document excel"

# Liste pour stocker les résultats
results = []

# Parcourir tous les fichiers Excel dans le dossier
for file_name in os.listdir(folder_path):
    if file_name.endswith('.XLSX'):
        file_path = os.path.join(folder_path, file_name)
        
        # Lire le fichier Excel
        df = pd.read_excel(file_path)
        
        # Calculer la valeur crête à crête pour la colonne 'Volume' entre les lignes 151 et 191
        volume_values = pd.to_numeric(df.iloc[151:191].iloc[:, 5], errors='coerce')  # Convertir en valeurs numériques
        if not volume_values.empty:
            valeur_crete_a_crete = volume_values.max() - volume_values.min()
        else:
            valeur_crete_a_crete = None
        
        # Ajouter le résultat à la liste
        results.append({'Nom du fichier': file_name, 'Valeur crête à crête': valeur_crete_a_crete})

# Créer un DataFrame avec tous les résultats
results_df = pd.DataFrame(results)
#print(results_df)

# Enregistrer les résultats dans un fichier Excel
results_df.to_excel('resultats_crete_a_crete.xlsx', index=False)
