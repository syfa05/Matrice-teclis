import pandas as pd
import os

# Chemin du dossier contenant les fichiers Excel
folder_path = r"C:\Users\fresn\PythonProject\Matrice teclis\Document format prn"

def convert_prn_to_xlsx(prn_file_path, xlsx_file_path, delimiter='\\s+'):
    try:
        # Lecture du fichier .prn en considérant que les colonnes sont séparées par des espaces multiples
        df = pd.read_csv(prn_file_path, delimiter=delimiter, engine='python')
        
        # Export du DataFrame dans un fichier Excel
        df.to_excel(xlsx_file_path, index=False)
        
        print(f"Conversion réussie : {xlsx_file_path}")
    except Exception as e:
        print(f"Erreur lors de la conversion : {e}")
        

# Parcours de tous les fichiers dans le dossier
for filename in os.listdir(folder_path):
    if filename.endswith(".PRN"):
        prn_file_path = os.path.join(folder_path, filename)
        xlsx_file_path = os.path.join(folder_path, filename.replace(".PRN", ".xlsx"))
        
        # Nettoyage des deux premières lignes du fichier .prn
        with open(prn_file_path, 'r') as file:
            lines = file.readlines()[2:]  # Ignorer les deux premières lignes
        
        with open(prn_file_path, 'w') as file:
            file.writelines(lines)
        
        # Conversion du fichier nettoyé
        convert_prn_to_xlsx(prn_file_path, xlsx_file_path)




