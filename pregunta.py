"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd



def ingest_data():

    file = "clusters_report.txt"
    data = pd.read_fwf(file, 
                     header=None, 
                     widths=[9, 16, 16, 77], 
                     names=
                     ["cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "principales_palabras_clave" ],
                     ).drop(range(0,3), axis=0).ffill()

    df = data.copy()
    df = df.groupby(['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave'])['principales_palabras_clave'].apply(' '.join).reset_index()
    df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].apply(lambda x: x.replace(',','.').strip(' %'))
    df['principales_palabras_clave'] = df['principales_palabras_clave'].apply(lambda x: x.replace('.',''))
    df['principales_palabras_clave'] = df['principales_palabras_clave'].apply(lambda x:' '.join(x.split()))
    df['cluster'] = df['cluster'].astype(int)
    df['cantidad_de_palabras_clave'] = df['cantidad_de_palabras_clave'].astype(int)
    df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].astype(float)
    df = df.sort_values(by=['cluster'], ascending=True)

    return df

