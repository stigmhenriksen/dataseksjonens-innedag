from utils import get_ssb_data, save_data_csv

FOLDER = "data"

URL = "https://data.ssb.no/api/v0/no/table/11587/"

QUERY = {
    "query": [
        {
            "code": "NACE2007",
            "selection": {
                "filter": "vs:NACE2007ledstillNN3",
                "values": [
                    "01-96"
                ]
            }
        },
        {
            "code": "ContentsCode",
            "selection": {
                "filter": "item",
                "values": [
                    "LedigeStillinger"
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
    save_data_csv(csv_data=data, folder=FOLDER, name="ssb_ledige_stillinger")
