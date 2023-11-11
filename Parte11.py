import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("./resultado_limpieza.csv")

data = data.drop(columns=["Grupo de Edad"])

plt.figure()
grafico = data["DEATH_EVENT"].value_counts().plot(kind="bar", color=["blue", "orange"])  # Cambiar colores
plt.title("Distribución de Eventos de Fallecimiento")
plt.xlabel("Fallecimientos")
plt.ylabel("Frecuencia")
plt.xticks([0, 1], labels=["Vivos", "Muertos"])
plt.show()

X_train, X_test, y_train, y_test = train_test_split(
    data.drop(columns=["DEATH_EVENT"]),
    data["DEATH_EVENT"],
    test_size=0.2,
    stratify=data["DEATH_EVENT"],
    random_state=42
)

clf = DecisionTreeClassifier(max_depth=5, min_samples_split=60, random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {accuracy:.2f}")

