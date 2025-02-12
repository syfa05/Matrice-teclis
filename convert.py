import pandas as pd
import os

folder_path = r"C:\Users\fresn\PythonProject\Matrice teclis\Document format prn"

# Liste tous les fichiers dans le dossier spécifié
files = os.listdir(folder_path)

# Filtre les fichiers .prn
prn_files = [f for f in files if f.lower().endswith('.PRN')]

# Affiche les fichiers .prn trouvés
for prn_file in prn_files:
    print(f"Fichier trouvé : {prn_file}")

def convert_prn_to_xlsx(prn_file_path, xlsx_file_path, delimiter='\\s+'):
    try:
        # Lecture du fichier .prn en considérant que les colonnes sont séparées par des espaces multiples
        df = pd.read_csv(prn_file_path, delimiter=delimiter, engine='python')
        
        # Export du DataFrame dans un fichier Excel
        df.to_excel(xlsx_file_path, index=False)
        
        print(f"Conversion réussie : {xlsx_file_path}")
    except Exception as e:
        print(f"Erreur lors de la conversion : {e}")

# Conversion de tous les fichiers .prn trouvés
for prn_file in prn_files:
    prn_file_path = os.path.join(folder_path, prn_file)
    xlsx_file_path = os.path.join(folder_path, os.path.splitext(prn_file)[0] + '.xlsx')
    
    # Vérifiez si le fichier existe
    if os.path.exists(prn_file_path):
        convert_prn_to_xlsx(prn_file_path, xlsx_file_path)
    else:
        print(f"Le fichier {prn_file_path} n'existe pas.")

