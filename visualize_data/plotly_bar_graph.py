
import pandas as pd
import plotly.graph_objects as go

FOLDER = "data"
DATASET = "nav_sykemeldte_alle_diagnoser.csv"


if __name__ == "__main__":
    df = pd.read_csv(f"{FOLDER}/{DATASET}")
    fig = go.Figure()
    bar_graph = go.Bar(x=df["Uke"], y=df["2019"])
    fig.add_trace(bar_graph)

    fig.show()
