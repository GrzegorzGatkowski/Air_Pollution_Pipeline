import pandas as pd
from prefect import flow
from datetime import datetime, timedelta
from etl_tasks import (
    write_bq,
    get_pollution_data,
    rename_columns,
    cleaning_columns,
    write_gcs,
    extract_from_gcs,
)


@flow()
def fetch_history_data(
    start_date: int, end_date: int, lat: float, lon: float
) -> pd.DataFrame:
    """
    A Prefect flow that fetches historical air pollution data from an API.

    Args:
        start_date (int): The start date for the data to fetch.
        end_date (int): The end date for the data to fetch.
        lat (float): The latitude of the location to fetch data for.
        lon (float): The longitude of the location to fetch data for.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the fetched air pollution data.
    """
    df = get_pollution_data(start_date, end_date, lat, lon)
    df_clean = cleaning_columns(df, columns=["main.aqi"])
    df_renamed = rename_columns(df_clean)
    return df_renamed


@flow()
def etl_to_gcs(df, city) -> None:
    """
    A Prefect flow that writes a pandas DataFrame to a GCS bucket.

    Args:
        df (pd.DataFrame): The DataFrame to write.
        city (str): The name of the city associated with the DataFrame.
    """
    path = f"data/air_pollution/{city}.parquet"
    write_gcs(df, path)


@flow()
def etl_to_gcs_parent_flow(start_date: int, end_date: int, locations_path: str):
    """
    A Prefect flow that processes historical air pollution data for a list of cities.

    Parameters
    ----------
    start_date : int
        The start time for the data range, SECONDS SINCE JAN 01 1970. (UTC).
    end_date : int
        The end time for the data range, SECONDS SINCE JAN 01 1970. (UTC).
    locations_path : str
        The path to the JSON file containing the list of cities to extract data for.

    Raises
    ------
    Exception
        If there is an error processing any of the cities.

    Returns
    -------
    None

    Notes
    -----
    This function reads in the list of cities from a JSON file at `locations_path` using pandas,
    and then iterates over each city to fetch historical air pollution data using the `fetch_history_data`
    function. The resulting data is then transformed using the `etl_to_gcs` function and written to
    Google Cloud Storage (GCS). If an exception is raised during the processing of a city, an error message
    is printed to the console.

    """
    cities = pd.read_json(locations_path)
    for index, city in cities.iterrows():
        try:
            df_pollution = fetch_history_data(
                start_date, end_date, city["Latitude"], city["Longitude"]
            )
            df_pollution["City_index"] = index
            etl_to_gcs(df_pollution, city["City"])
        except Exception as e:
            print(f"Failed to process city {city['City']}: {str(e)}")


@flow()
def etl_gcs_to_bq(locations_path: str) -> None:
    """
    Extracts data from Google Cloud Storage (GCS), processes it, and loads it into BigQuery (BQ).

    Parameters
    ----------
    locations_path : str
        The path to the JSON file containing the list of cities to extract data for.

    Returns
    -------
    None

    Raises
    ------
    Any exceptions raised during the execution of the function are propagated to the caller.

    Notes
    -----
    This function iterates over the list of cities contained in the JSON file at `locations_path`.
    For each city, it extracts data from GCS using the `extract_from_gcs` context manager,
    and loads it into the `raw.airpollution` table in BQ using the `write_bq` function.
    If an exception is raised during the processing of a city, an error message is printed
    to the console and processing continues with the next city.
    """
    cities = pd.read_json(locations_path)
    for index, city in cities.iterrows():
        try:
            df = extract_from_gcs(city["City"])
            write_bq(df, "raw.airpollution")
        except Exception as e:
            print(f"Failed to process city {city.City}: {str(e)}")


@flow()
def etl_cities_flow(locations_path: str):
    """
    A Prefect flow that processes a pandas DataFrame containing information about cities.

    Parameters
    ----------
    locations_path : str
        The path to the JSON file containing the list of cities to extract data for.

    Raises
    ------
    Exception
        If there is an error processing the cities table.

    Returns
    -------
    None

    Notes
    -----
    This function reads in the city information from a JSON file at `locations_path` using pandas,
    and then writes the data to the `raw.cities` table in BigQuery using the `write_bq` function.
    If an exception is raised during the processing of the cities table, an error message is printed
    to the console.

    """
    cities = pd.read_json(locations_path)
    try:
        write_bq(cities, "raw.cities")
    except Exception as e:
        print(f"Failed to process cities table: {str(e)}")


if __name__ == "__main__":
    cities = pd.read_json("./data/locations.json")
    end = int((datetime.now() - timedelta(minutes=1)).timestamp())
    start = int((datetime.strptime("2020-11-28", "%Y-%m-%d").timestamp()))
    etl_to_gcs_parent_flow(
        start_date=start, end_date=end, locations_path="./data/locations.json"
    )
    etl_cities_flow(locations_path="./data/locations.json")
    etl_gcs_to_bq(locations_path="./data/locations.json")
