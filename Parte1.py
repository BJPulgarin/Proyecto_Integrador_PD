from datasets import load_dataset
import numpy as np

dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

listaEdades = data["age"]
edadesArray = np.array(listaEdades)

edadPromedio = int(round(np.average(edadesArray)))
print(edadPromedio)
print(dataset)
