import os
import pandas as pd

def nombre_output(lat,lon):
    " Establece el nombre de salida del csv."
    lat = str(round(lat,3))
    lon = str(round(lon,3))
    output_name = lat + "__" + lon + ".csv"
    return output_name


def descargar_lugar(latitud,longitud,directorio):
    """
    Descarga datos horarios del 2001/01/01 al 2022/12/31
    de viento y dirección.
    """
    nombre_archivo =   directorio + nombre_output(latitud,longitud)
    if not os.path.exists(nombre_archivo):
        url =  f"https://power.larc.nasa.gov/api/temporal/hourly/point?start=20010101&end=20221231&latitude={latitud}&longitude={longitud}&community=re&parameters=WS10M,WS50M,WD50M&format=csv&user=felos&header=false&time-standard=utc"
        df_datos = pd.read_csv(url)
        df_datos.to_csv(nombre_archivo)



def descargar_temperatura(latitud, longitud, directorio):
    nombre_archivo = directorio + nombre_output(latitud, longitud)
    if not os.path.exists(nombre_archivo):
        url =  f"https://power.larc.nasa.gov/api/temporal/hourly/point?start=20220101&end=20221231&latitude={latitud}&longitude={longitud}&community=re&parameters=WS50M,WD50M,T2M&format=csv&user=felos&header=false&time-standard=utc"
        df_datos = pd.read_csv(url)
        df_datos.to_csv(nombre_archivo)