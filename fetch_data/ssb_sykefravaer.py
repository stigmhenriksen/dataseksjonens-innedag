from utils import get_ssb_data, save_data_csv

FOLDER = "data"

URL = "https://data.ssb.no/api/v0/no/table/12439/"

QUERY = {
  "query": [
    {
      "code": "Kjonn",
      "selection": {
        "filter": "item",
        "values": [
          "0"
        ]
      }
    },
    {
      "code": "Sykefraver2",
      "selection": {
        "filter": "item",
        "values": [
          "Alt"
        ]
      }
    },
    {
      "code": "ContentsCode",
      "selection": {
        "filter": "item",
        "values": [
          "SykefravProsent"
        ]
      }
    }
  ],
  "response": {
    "format": "csv2"
  }
}


if __name__ == "__main__":
    data = get_ssb_data(url=URL, query=QUERY)
    save_data_csv(csv_data=data, folder=FOLDER, name="ssb_sykefravaer")
