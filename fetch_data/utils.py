import requests

from typing import Dict, Any

import pandas as pd


def get_ssb_data(url: str, query: Dict[str, Any]) -> str:
    """
    :param url: URL til ssb tabell
    :param query: API spørring til ssb tabell
    :return: Respons som tekst.
    """
    resp = requests.post(url=url, json=query)
    resp.raise_for_status()
    return resp.text


def save_data_csv(csv_data: str, folder: str, name: str) -> None:
    """
    :param csv_data: CSV data som string
    :param folder: Mappe der .csv filen skal ligge
    :param name: Navn til .csv fil
    :return: None
    """
    with open(f"{folder}/{name}.csv", "w+") as file:
        file.write(csv_data)


def save_dataframe_csv(dataframe: pd.DataFrame, folder: str, name: str) -> None:
    """

    :param dataframe: panas.DataFrame som skal skrives
    :param folder: Mappe der .csv filen skal ligge
    :param name: Navn til .csv fil
    :return: None
    """
    dataframe.to_csv(f"{folder}/{name}.csv", index=False)
