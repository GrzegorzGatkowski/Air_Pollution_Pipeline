import pandas as pd
from prefect import flow
from etl_tasks import (
    write_bq,
    rename_columns,
    cleaning_columns,
    get_current_pollution,
)


@flow()
def fetch_current_data(lat: float, lon: float) -> pd.DataFrame:
    """Fetches current pollution data for a given latitude and longitude.

    Args:
        lat (float): The latitude of the location.
        lon (float): The longitude of the location.

    Returns:
        pd.DataFrame: The current pollution data for the specified location.
    """

    df = get_current_pollution(lat, lon)
    df_clean = cleaning_columns(df, columns=["main.aqi", "coord.lon", "coord.lat"])
    df_renamed = rename_columns(df_clean)
    return df_renamed


@flow()
def etl_current_parent_flow(locations_path: str) -> None:
    """Extract, transform and load (ETL) workflow for fetching and processing current pollution data
    for a list of cities.

    Args:
        locations_path (str): A string representing the file path of the JSON file containing information
                              about the cities to fetch data for.

    Returns:
        None.
    """
    cities = pd.read_json(locations_path)
    for index, city in cities.iterrows():
        try:
            df_pollution = fetch_current_data(city["Latitude"], city["Longitude"])
            df_pollution["City_index"] = index
            write_bq(df_pollution, "raw.airpollution")
        except Exception as e:
            print(f"Failed to process city {city['City']}: {str(e)}")


if __name__ == "__main__":
    etl_current_parent_flow("./data/locations.json")
