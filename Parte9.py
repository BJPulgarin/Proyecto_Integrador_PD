import pandas as pd
import plotly.graph_objects as go
from sklearn.manifold import TSNE

data = pd.read_csv("./resultado_limpieza.csv")

data_array = data.drop(columns=["DEATH_EVENT", "Grupo de Edad"]).values
death_array = data["DEATH_EVENT"].values

# Aplicar t-SNE
X_embedded = TSNE(
    n_components=3,
    learning_rate="auto",
    init="random",
    perplexity=3
).fit_transform(data_array)

fig = go.Figure()

fig.add_trace(go.Scatter3d(
    x=X_embedded[:, 0], y=X_embedded[:, 1], z=X_embedded[:, 2],
    mode="markers",
    marker=dict(
        size=5,
        color=death_array,
        colorscale="Viridis",
        opacity=0.8
    )
))

fig.update_layout(
    title="Dispersión 3D de personas vivas y muertas"
)

fig.show()

