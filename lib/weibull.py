import numpy as np
from scipy import stats

def fit_weibull(data) -> tuple[float]:
    return stats.exponweib.fit(data,f0=1,floc=0)

def generar_curva(x:np.ndarray, fit:tuple[float]):
    return  stats.exponweib.pdf(x,*fit)

def generar_curva_parametros(x:np.ndarray, k, l):
    return  stats.exponweib.pdf(x,(1,k,0,l))


def ajustar_weibull(data):
    """
    Ajusta los datos de la weibull y retorna
    los valores de x,y del PDF más los valores
    del ajuste de k y lambda.
    """

    fit = fit_weibull(data)

    x = np.linspace(0,20,1000)
    y = generar_curva(x, fit)

    k, lambda_o = fit[1], fit[3]

    return x, y, k, lambda_o






