import requests

from io import BytesIO

import pandas as pd

from utils import save_dataframe_csv

FOLDER = "data"
URL = "https://www.nav.no/_/attachment/download/2dedd6e4-f22d-4761-9d7a-07f046c8e889" \
      ":e92019f464edcea591425463f13094374bac443c/Nye_sykmeldte_per_uke._Tidsserie_Uke%2013%202022.xlsx"


def get_nav_xlsx(url: str) -> bytes:
    resp = requests.get(url=url)
    resp.raise_for_status()
    return resp.content


def load_xlsx_data(nav_data: bytes, sheet_name: str) -> pd.DataFrame:
    with BytesIO(nav_data) as file:
        _df = pd.read_excel(file, sheet_name=sheet_name, header=5)
        _df.drop(columns=[column for column in _df.columns if "Unnamed:" in column.split()], inplace=True)

        return _df


if __name__ == "__main__":
    data = get_nav_xlsx(url=URL)
    df_alle_diagnoser = load_xlsx_data(nav_data=data, sheet_name="Alle diagnoser",)
    df_koronarelaterte_diagnoser = load_xlsx_data(nav_data=data, sheet_name="Koronarelaterte diagnoser")

    save_dataframe_csv(dataframe=df_alle_diagnoser, folder=FOLDER, name="nav_sykemeldte_alle_diagnoser")
    save_dataframe_csv(dataframe=df_koronarelaterte_diagnoser, folder=FOLDER, name="nav_sykemeldte_korona")
