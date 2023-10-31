import lib
import numpy as np

class ObjMes:
    def __init__(self, mes):

        if isinstance(mes, int):
            self.index_mes = mes
            self.nombre_mes = lib.index2mes(mes)
        else:
            self.nombre_mes = mes
            self.index_mes = lib.mes2index(mes)

        # Fit de los meses para cada uno de los años
        self.fit_por_mes = []
        for año in range(2001,2023):
            ws = lib.cargar_datos(año=año, mes=self.index_mes)
            self.fit_por_mes.append( lib.fit_weibull(ws) )


    def encontrar_mes_tipico(self, hasta_año=2022)->int:
        """Devuelve el año que contiene el més típico según nuestras métricas"""

        idx_f = hasta_año - 2001
        x = np.linspace(0,20,1000)

        fit_all_data = self.parametros_weibull_representativos(hasta_año,return_fit_tuple=True)

        y_all_data = lib.generar_curva(x, fit_all_data)

        scores = []
        for i in range(idx_f+1):
             y_tipico = lib.generar_curva(x, self.fit_por_mes[i])
             s = np.mean( ( (y_tipico - y_all_data)*y_all_data )**2 )
             scores.append(s)

        return np.argmin(scores) + 2001
    

    def parametros_weibull_tipicos(self, año:int):
        " Si no se indica ningun valor devuelve el de todos los datos."
        " Devulve k y lambda del mes de ese año.                      "

        idx = año - 2001
        return self.fit_por_mes[idx][1], self.fit_por_mes[idx][3]
    

    def parametros_weibull_representativos(self, hasta_año, return_fit_tuple=False):
        años = list(np.arange(2001,hasta_año+1)) # Incluimos año de "hasta año"
        ws = lib.cargar_datos(año=años, mes=self.index_mes)
        fit = lib.fit_weibull(ws)

        if return_fit_tuple:
            return fit

        return fit[1], fit[3]




            
        





