import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv("./resultado_limpieza.csv")

columnas = ["Anemia", "Diabetes", "Fumador", "Muerto"]
datos = datos.rename(columns={"anaemia": columnas[0], "diabetes": columnas[1], "smoking": columnas[2], "DEATH_EVENT": columnas[3]})

plt.style.use('ggplot')

fig, axes = plt.subplots(nrows=1, ncols=len(columnas), figsize=(12, 4))

for index, columna in enumerate(columnas):
    cuentas_columna = datos[columna].map({1: "Sí", 0: "No"}).value_counts()
    axes[index].pie(cuentas_columna, labels=cuentas_columna.index, autopct="%1.1f%%", startangle=90)
    axes[index].set_title(columna)

plt.tight_layout()
plt.show()
