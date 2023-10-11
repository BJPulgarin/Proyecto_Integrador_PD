import pandas as pd
from datasets import load_dataset

dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

dfData = pd.DataFrame(data)

# verificando integridad de los datos
'''
print(dfData.dtypes)
print(dfData[["is_male", "is_smoker"]])
nulos = dfData["is_male"].isnull()
contarNulos = nulos.sum()
print(contarNulos)
'''

grupos = dfData.groupby(["is_male", "is_smoker"]).count()

hombres_fumadores = dfData[(dfData["is_male"] == True) & (dfData["is_smoker"] == True)]
num_hombres_fumadores = hombres_fumadores.shape[0]
mujeres_fumadoras = dfData[(dfData["is_male"] == False) & (dfData["is_smoker"] == True)]
num_mujeres_fumadoras = mujeres_fumadoras.shape[0]

print(num_hombres_fumadores)
print(num_mujeres_fumadoras)
