import pandas as pd
import numpy as np
from datasets import load_dataset

dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

dfData = pd.DataFrame(data)

muertos = dfData[dfData["is_dead"] == 1]
vivos = dfData[dfData["is_dead"] == 0]

'''
def edadPromedio(df):
    edades = np.array(df["age"])
    promedio = int(round(np.average(edades)))
    return promedio
    
print(edadPromedio(vivos))
print(edadPromedio(muertos))
'''

edadPromedioVivos = int(round(vivos["age"].mean()))
edadPromedioMuertos = int(round(muertos["age"].mean()))

print(edadPromedioVivos)
print(edadPromedioMuertos)
