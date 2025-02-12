import pandas as pd
import os

folder_path = r"C:\Users\fresn\PythonProject\Matrice teclis\Document excel"

# Liste tous les fichiers dans le dossier spécifié
files = os.listdir(folder_path)

# Filtre les fichiers .prn
prn_files = [f for f in files if f.lower().endswith('.prn')]

# Affiche les fichiers .prn trouvés
for prn_file in prn_files:
    print(f"Fichier trouvé : {prn_file}")



