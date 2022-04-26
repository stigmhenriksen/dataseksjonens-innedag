import pandas as pd
import plotly.graph_objects as go

FOLDER = "data"
DATASET = "nav_sykemeldte_alle_diagnoser.csv"


if __name__ == "__main__":
    # Gjør noen enkle transformasjoner
    df = pd.read_csv(f"{FOLDER}/{DATASET}").replace("*", 0)
    df["2019"] = df["2019"].astype(int)
    df["2020"] = df["2020"].astype(int)

    # Lager figur
    fig = go.Figure()
    line_graph_2019 = go.Scatter(x=df["Uke"],
                                 y=df["2019"],
                                 marker={"color": "#d7dbdb"},
                                 line={"width": 10},
                                 name="2019")

    line_graph_2020 = go.Scatter(x=df["Uke"],
                                 y=df["2020"],
                                 marker={"color": "#cca39b"},
                                 line={"width": 10},
                                 name="2020")

    fig.add_trace(line_graph_2019)
    fig.add_trace(line_graph_2020)

    # Styler figuren
    fig.update_layout(paper_bgcolor="#526175",
                      plot_bgcolor="#526175",
                      yaxis={"color": "#d7dbdb", "tickfont": {"size": 20}},
                      xaxis={"color": "#d7dbdb", "tickfont": {"size": 20}},
                      legend={"font": {"color": "#d7dbdb", "size": 20}})

    # Viser figuren i nettleseren
    fig.show()
