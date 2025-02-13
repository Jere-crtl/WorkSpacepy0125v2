import pandas as pd

# Ruta donde se guardó el reporte
path = "/workspaces/Workspacepy0125v2/proyecto/files/data-08-02.csv"

# Cargar y mostrar el archivo
df = pd.read_csv(path)
print(df)

