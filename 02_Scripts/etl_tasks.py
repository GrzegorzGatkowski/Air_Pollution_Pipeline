import pandas as pd
import secrets_key
import requests
from datetime import datetime, timedelta
from prefect import task
from prefect.tasks import task_input_hash

@task(retries=3, log_print=True, cache_key_fn=task_input_hash, cache_expiration=timedelta(hours=3))
def get_pollution_data(start_time, end_time, lat, lon):
    """
    Retrieve air pollution data from the OpenWeatherMap API for a specified time range and location.
    Parameters:
        start_time (timestamp): The start time for the data range, SECONDS SINCE JAN 01 1970. (UTC).
        end_time (timestamp): The end time for the data range, SECONDS SINCE JAN 01 1970. (UTC).
        lat (float): The latitude of the location for which to retrieve data.
        lon (float): The longitude of the location for which to retrieve data.
    Returns:
        pandas.DataFrame: A dataframe containing the API response data.
    """

    # API endpoint and API key
    api_endpoint = "https://api.openweathermap.org/data/2.5/air_pollution/history"
    api_key = secrets_key.API_KEY

    # Send the API request
    response = requests.get(api_endpoint, params={
        "lat": lat,
        "lon": lon,
        "start": start_time,
        "end": end_time,
        "appid": api_key
    })

    # Check for errors
    if response.status_code != 200:
        print("Error: API request failed with status code", response.status_code)
        exit()

    # Parse the API response
    data = response.json()

    # Convert the data to a dataframe
    df = pd.json_normalize(data['list'])

    return df

@task(retries=3, log_print=True, cache_key_fn=task_input_hash, cache_expiration=timedelta(hours=3))
def get_current_pollution(cord_list) -> pd.DataFrame:
    """
    Retrieve current air pollution data for a list of coordinates.
    
    Parameters
    ----------
    cord_list : List[Tuple[float, float]]
        A list of (latitude, longitude) tuples for which to retrieve air pollution data.
    
    Returns
    -------
    df : pd.DataFrame
        A pandas DataFrame containing the retrieved air pollution data.
    """
    # API endpoint and API key
    api_key = secrets_key.API_KEY

    # Set up an empty pandas dataframe to store the data
    df = pd.DataFrame()

    for lon, lat in cord_list:
        # Make a request to the OpenWeatherMap API
        url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
        response = requests.get(url)
        data = response.json()
        temp = pd.json_normalize(data, "list", [["coord", "lon"], ["coord", "lat"]])
        df = df.append(temp, ignore_index=True)
    return df

@task(retries=3, log_print=True, cache_key_fn=task_input_hash, cache_expiration=timedelta(hours=3))
def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rename the columns of a pandas DataFrame.
    
    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to rename the columns of.
    
    Returns
    -------
    df : pd.DataFrame
        The DataFrame with renamed columns.
    """
    df = df.rename(columns={'components.co': 'Carbon Monoxide_(CO)', 'components.no': 'Nitric oxide_(NO)', 'components.no2': 'Nitrogen Dioxide_(NO2)',
                        'components.o3': 'Ozone_(O3)', 'components.so2': 'Sulfur Dioxide_(SO2)', 'components.pm2_5': 'PM2_5',
                        'components.pm10': 'PM10', 'components.nh3': 'NH3'})
    return df

@task(retries=3, log_print=True, cache_key_fn=task_input_hash, cache_expiration=timedelta(hours=3))
def cleaning_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform the columns of a pandas DataFrame.
    
    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to clean and transform.
    
    Returns
    -------
    df : pd.DataFrame
        The cleaned and transformed DataFrame.
    """
    df.drop(columns='main.aqi', inplace=True)
    df['dt'] = pd.to_datetime(df['dt'], unit='s')
    df.set_index('dt', inplace = True)
    return df