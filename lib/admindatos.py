from pathlib import Path

import pandas as pd
import numpy  as np

DIR_SCRIPT = Path(__file__).parent.resolve()
PATH_DATOS = DIR_SCRIPT.parent.resolve() / "datos_tecate.csv"

MESES = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",   
]

def mes2index(mes:str):
    "Transforma del nombre del mes a su número"
    return MESES.index(mes) + 1

def index2mes(index:int):
    "Transforma del número del mes a su nombre"
    return MESES[index-1]

def cargar_datos(año=None, mes=None, fill_value=0) -> pd.DataFrame:
    """
    Carga los datos del .csv se excluye los dias biciestos para
    mantener consistencia en la longitud de los años.

    Si se indica un año o una fecha en particular se filtran esos
    datos.

    año (int): Año o años que se quieren filtrar
    mes (int): Número del mes que se quiere filtrar
    """

    if año is not None:
        
        if not isinstance(año, list):
            año = [año]
    
    if mes is not None:

        if not isinstance(mes, list):
            mes = [mes]

        # mes (str) -> mes (index)
        for i in range(len(mes)):
            m = mes[i]
            if isinstance(m, str):
                mes[i] = mes2index(m)


    df = pd.read_csv(PATH_DATOS)
    index_biciestos = df[ (df["MO"] == 2) & (df["DY"] == 29) ].index
    df.drop(index_biciestos,inplace = True)


    if mes is not None:
        df = df[df["MO"].isin(mes)]

    if año is not None:
        df = df[df["YEAR"].isin(año)]
    
    ws = df["WS50M"].values

    # Hacemos a 0 los datos faltantes
    ws[ws < 0] = fill_value

    assert len(ws) > 0, f"No se encontraron datos con el año {año}, y mes {mes}"

    return ws


if __name__ == "__main__":

    ws = cargar_datos(año=2001, mes=2)
    print(ws.shape)
    
