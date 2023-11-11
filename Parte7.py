import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos desde el archivo procesado
datos = pd.read_csv("resultado_limpieza.csv")

# Gráfico de distribución de edades
datos['age'].plot(kind='hist', edgecolor='black', title='Distribución de Edades', xlabel='Edades', ylabel='Frecuencia')
plt.show()

# Gráficos agrupados por sexo
datosAnemiaPorSexo = datos[datos["anaemia"] == 1].groupby("sex").size()
datosDiabetesPorSexo = datos[datos["diabetes"] == 1].groupby("sex").size()
datosFumadorPorSexo = datos[datos["smoking"] == 1].groupby("sex").size()
datosMuertoPorSexo = datos[datos["DEATH_EVENT"] == 1].groupby("sex").size()
datosAgrupadosPorSexo = pd.DataFrame({"Anémicos": datosAnemiaPorSexo, "Diabéticos": datosDiabetesPorSexo, "Fumadores": datosFumadorPorSexo, "Muertos": datosMuertoPorSexo})
datosAgrupadosPorSexo.index = datosAgrupadosPorSexo.index.map({0: "Mujeres", 1: "Hombres"})
datosAgrupadosPorSexo = datosAgrupadosPorSexo.T

# Gráfico de barras agrupado por sexo
datosAgrupadosPorSexo.plot(kind="bar", title="Histograma Agrupado por Sexo", rot=0, ylabel="Cantidad", xlabel="Categorías", color=['blue', 'green', 'orange', 'red'])
plt.show()
