import lib
import numpy as np

def curva_de_potencia(ws):
    potencia = 2190.0 - 1170.0*ws + 194.6*(ws**2) - 7.48*(ws**3)
    potencia[ws > 12 ]  = 3300.0
    potencia[ws < 3.5]  = 0.0
    potencia[ws > 25.0] = 0.0
    return potencia

def calcular_energia(ws):
    """
    Calcula la enería esperada en MWh
    """
    
    x   = np.linspace(0,20,1000)
    fit = lib.fit_weibull(ws)
    probabilidad = lib.generar_curva(x, fit)
    potencia = curva_de_potencia(x)
    potencia_esperada = np.trapz(potencia*probabilidad,x=x)
    energía_esperada  = len(ws.reshape((-1)))*potencia_esperada
    return energía_esperada / 1_000 


"""
if __name__ == "__main__":
    vel1 = 6.842306
    vel2 = 6.842080

    potencia1 = curva_de_potencia(np.array([vel1]))
    potencia2 = curva_de_potencia(np.array([vel2]))
    print(potencia1*8760 / 1000)
    print(potencia2*8760 / 1000)
"""