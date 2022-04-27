import pandas as pd
import plotly.graph_objects as go

FOLDER = "data"
DATASET = "nav_sykemeldte_alle_diagnoser.csv"


if __name__ == "__main__":
    # Gjør noen enkle transformasjoner
    df = pd.read_csv(f"{FOLDER}/{DATASET}").replace("*", 0)
    df["2019"] = df["2019"].astype(int)

    # Lager figur
    fig = go.Figure()
    bar_graph = go.Bar(x=df["Uke"], y=df["2022"], marker={"color": "#d7dbdb"})
    fig.add_trace(bar_graph)

    # Styler figuren
    fig.update_layout(paper_bgcolor="#526175",
                      plot_bgcolor="#526175",
                      yaxis={"color": "#d7dbdb", "tickfont": {"size": 20}},
                      xaxis={"color": "#d7dbdb", "tickfont": {"size": 20}})

    # Viser figuren i nettleseren
    fig.show()
