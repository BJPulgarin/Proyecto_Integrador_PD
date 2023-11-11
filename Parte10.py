import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = pd.read_csv("./resultado_limpieza.csv")
X = data.drop(columns=["DEATH_EVENT", "age", "Grupo de Edad"])
y = data["age"]

regression = LinearRegression()
regression.fit(X, y)

y_predict = regression.predict(X)
mse = mean_squared_error(y, y_predict)
print(mse)
