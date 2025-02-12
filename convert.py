import pandas as pd

def convert_prn_to_xlsx(prn_file_path, xlsx_file_path, delimiter='\\s+'):
    try:
        # Lecture du fichier .prn en considérant que les colonnes sont séparées par des espaces multiples
        df = pd.read_csv(prn_file_path, delimiter=delimiter, engine='python')
        
        # Export du DataFrame dans un fichier Excel
        df.to_excel(xlsx_file_path, index=False)
        
        print(f"Conversion réussie : {xlsx_file_path}")
    except Exception as e:
        print(f"Erreur lors de la conversion : {e}")

# Exemple d'utilisation
prn_file = 'Tests_amplitude  protocole1 Piston 1 joints-0.05µl-a.PRNn'   # Remplacez par le chemin de votre fichier .prn
xlsx_file = 'resultat.xlsx'      # Chemin de sortie pour le fichier Excel

convert_prn_to_xlsx(prn_file, xlsx_file)

