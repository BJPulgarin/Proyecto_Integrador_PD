import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.model_selection import train_test_split

# Cargar datos y eliminar columna no deseada
data = pd.read_csv("./resultado_limpieza.csv")
data = data.drop(columns=["Grupo de Edad"])

# Dividir el conjunto de datos
X_train, X_test, y_train, y_test = train_test_split(
    data.drop(columns=["DEATH_EVENT"]),
    data["DEATH_EVENT"],
    test_size=0.2,
    stratify=data["DEATH_EVENT"],
    random_state=42
)

# Entrenar el RandomForest
rfc = RandomForestClassifier(n_estimators=55, max_depth=8, random_state=42)
rfc.fit(X_train, y_train)

# Evaluar el rendimiento del RandomForest
y_pred_random_forest = rfc.predict(X_test)
accuracy_random_forest = accuracy_score(y_test, y_pred_random_forest)
score_F1_random_forest = f1_score(y_test, y_pred_random_forest, average=None)

# Mostrar resultados
print(f"Accuracy del RandomForest: {accuracy_random_forest:.2f}")
print(f"F1 Score del RandomForest: {score_F1_random_forest}")
confusion_matrix_random_forest = confusion_matrix(y_test, y_pred_random_forest)
print("Matriz de confusión del RandomForest:\n", confusion_matrix_random_forest)

# Conclusión:
'''Aunque es cierto que al RandomForest muestra
   buena precisión en general, al observar más a
   a detalle la clasificación, nos damos cuenta que
   el modelo no es tan bueno para identificar a los muertos,
   esto se debe a la diferencia que hay entre los vivos
   y muertos; el modelo tiene mucha más información para
   entrenar e identificar a los vivios, pero no la suficiente
   para clasificar correctamente a los muertos. Esto puede
   tratarse modificando el modelo, y enfocarlo más a la clase
   Muertos, y asi mejorar la precisión específica del modelo.
'''