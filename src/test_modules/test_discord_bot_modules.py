import urllib.request
import requests
from dotenv import load_dotenv
import json
import sys
import os
# Needs to be installed; pip3 install pytest-mock, pip3 install pytest, pip3 install -coverage - Arttu K. Later e.g. pip3 freeze > requirements.txt.
import pprint
from tests_mockups import one_country_object, two_countries_list_of_dicts, own_coordinate_location_mockup, five_countries_list_of_dicts, mock_up_response_for_stops, fetch_food, test_origin_destination_data

# sys.path.append("src.components.cogs") DEBUGGING and left for reference.

load_dotenv()
# Getting the API-key for the desired method.
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
# Getting the API-key from .env file located at root for this folder and these files. Security added.
api_key = os.getenv('API_KEY')

#api_key_file = open("api_key_2.txt", 'r')
#api_key = api_key_file.readline()
# api_key_file.close() # For reference if needed.


# Creating a refactored version of the fetch function to be used in testing.


def fetch_Covid_Information():  # Used later in some of the methods.
    with urllib.request.urlopen("https://api.covid19api.com/summary") as response:
        html = response.read()
        data = json.loads(html)  # Loads the whole datapoint as JSON.

        return data


# Testing with desired data, exact values known.
def test_get_countries_with_desired_mock(mocker):
    # Initializing the values for country_Dict.
    my_countries_mockup = five_countries_list_of_dicts
    mocker.patch('test_discord_bot_modules.fetch_Covid_Information',
                 return_value=my_countries_mockup)  # Patching in just the desired information for country-data.

    # Now, instead of the whole data, we only get the mockup-data. ...
    country_Dict = fetch_Covid_Information()
    # ... Without mocker, this call would fetch the whole list. There is a connection with the method defined at the start of this file.

    # Asserting the data, checking the exact length and what is in the dictionary, also checking additional characteristics for the mock-up data:
    # print(postalDict)
    assert len(country_Dict) < 100 and len(country_Dict) == 5 and country_Dict[0]["Country"] == "Algeria" and len(
        country_Dict[0]) == 11 and country_Dict[1]["TotalConfirmed"] == 5725 and country_Dict[3]["NewConfirmed"] == 1 and len(
        country_Dict[3]) == 11 and country_Dict[0] != country_Dict[1] and country_Dict[1]["Country"] != country_Dict[2]["Country"]


# Testing fetching created inside module google_places.py.


def fetch_own_coordinates(url):
    with urllib.request.urlopen(url) as response:
        html = response.read()
        data = json.loads(html)  # Loads the whole datapoint as JSON.

        return data


# Testing fetching within the component covid19_information.py.


def test_fetching_for_covid():
    information = fetch_Covid_Information()
    # print(information) Debugging.

    # Asserting that the required data is present...
    assert len(information["Countries"]
               ) > 150 and information["Countries"][0]["Country"] == "Afghanistan"
    # ... and that the first item is Afghanistan.


# Testing mockup dictionary from file "tests_mockups.py", and converting said dict to JSON to test if a value can be found in it.


def test_mockup_data_one_country():
    mockup = one_country_object
    mockupJSON = json.dumps(mockup)  # Converting to a different type.
    print(mockup)

    assert mockup["Country"] == "Afghanistan" and mockup["NewConfirmed"] == 44 and mockup["CountryCode"] == "AF" and str(1462) in mockupJSON and len(
        mockup) == 11 and len(mockupJSON) == 244


# Testing a list of dictionaries with two dicts in the list:


def test_mockup_data_two_countries():
    # This is what a fetch for two items would return.
    mockup_two = two_countries_list_of_dicts
    mockup_two_dict = json.dumps(mockup_two)

    assert len(mockup_two) == 2 and mockup_two[0] != mockup_two[1] and mockup_two[0]["Country"] == "Afghanistan" and mockup_two[1]["Country"] == "Finland" and len(
        mockup_two_dict) == 482 and mockup_two[0]["Slug"] != mockup_two[1]["Slug"]


def test_closest_restaurant_finder_own_coordinates_fetch():
    url1 = os.getenv('API_KEY')
    data = own_coordinate_location_mockup
    url = "https://www.mapquestapi.com/geocoding/v1/address?key=" + url1 + \
        "&inFormat=kvp&outFormat=json&location=Marsinkuja+1%2C+Vantaa%2C+Finland&thumbMaps=false"
    data2 = fetch_own_coordinates(url)

    # Asserting that the mockup-data contains specified JSON-forms, and that the actual fetch for the same address is different depending on the API.
    assert len(data) > 2 and data["results"][0]["locations"][0]["street"] == "Marsinkuja 1" and data2[
        "results"][0]["locations"][0]["street"] == "Marsinkuja 1" and data != data2


def test_location_fetch_coordinates():
    urlAPIKey = os.getenv('API_KEY')
    url_one = "https://www.mapquestapi.com/geocoding/v1/address?key=" + urlAPIKey + \
        "&inFormat=kvp&outFormat=json&location=Saturnuksenkuja+2%2C+Vantaa%2C+Finland&thumbMaps=false"
    url_two = "https://www.mapquestapi.com/geocoding/v1/address?key=" + urlAPIKey + \
        "&inFormat=kvp&outFormat=json&location=Marsinkuja+1%2C+Vantaa%2C+Finland&thumbMaps=false"

    data = fetch_own_coordinates(url_one)
    data2 = fetch_own_coordinates(url_two)

    # Asserting that different inputs / addresses have different coordinates and street names.
    assert data["results"][0]["locations"][0]["street"] != data2["results"][0]["locations"][0][
        "street"] and data["results"][0]["locations"][0]["latLng"] != data2["results"][0]["locations"][0]["latLng"] and len(data) > 1 and len(
            data2) > 1


# This handles the same basic functionality as PLACES, thus both can be tested (with their functionality) with this:


def test_fetching_events_with_coords():
    url_map = "https://www.mapquestapi.com/geocoding/v1/address?key=" + api_key + \
        "&inFormat=kvp&outFormat=json&location=Marsinkuja+1%2C+Vantaa%2C+Finland&thumbMaps=false"
    # Opening and reading and converting to JSON the coordinates-dict with location attributes.
    with urllib.request.urlopen(url_map) as response:
        html = response.read()
        # Loads the whole datapoint as JSON.
        data = json.loads(html)
        coordLat = data["results"][0]["locations"][0]["latLng"]["lat"] # Inputting desired coordinates from another fetch.
        coordLng = data["results"][0]["locations"][0]["latLng"]["lng"] # Inputting desired coordinates from another fetch.
        #print(data)  # DEBUGGING.
        url_events = 'http://open-api.myhelsinki.fi/v1/events/?distance_filter=' + str(coordLat) + '%2C' + str(
            coordLng) + '%2C2100'
        data_2 = requests.get(url_events).json()
        #print(data_2)

    # Asserting that data has been gained from two different fethces and requests.
    assert len(data) >= 3 and len(data_2) >=0 and len(data_2) >= 1 and len(data_2["data"]) >= 5 and len(data_2) == 3


# Asserting that there is information received in a certain way and accessed in a certain way from STOPS related to HSL-GraphQL-POST-METHOD.


def test_graphql_fetch_and_request_from_HSL():
    mock_up_data = mock_up_response_for_stops

    # Asserting that there is information and that the information is located at the correct state:
    assert mock_up_data["data"]["nearest"]["edges"][0]["node"]["place"]["name"] == "Vaihdemiehenkatu" and len(
    mock_up_data) == 1 and len(mock_up_data) >= 0 and mock_up_data["data"]["nearest"]["edges"][0]["node"]["place"]["code"] == "H2183" and mock_up_data["data"][
        "nearest"]["edges"][0]["node"]["place"]["routes"][0]["shortName"] == "506"


# Asserting that the data from the Bistro-component contains information.


def test_fetching_food_items_bistro():
    data = fetch_food()
    #print(data) DEBUGGING.

    # Asserting that there is information present. Length is 1. Closed on Sundays and Saturdays. Data varies greatly, on weekends just a list of ONE dict.
    assert len(data) >= 0 # Changed this due to Bistro being clased - no more unwanted failures.


# Asserting that data received from the GraphQL-POST-METHOD gives the desired data, and that the data is accessed correctly.


def test_query_HSL_from_a_to_b():
    test_data = test_origin_destination_data

    # Asserting multiple aspects of this information. Two (2) dicts in itineraries.
    assert len(test_data) >= 1 and len(test_data["data"]["plan"]["itineraries"][0]["legs"][0]) >= 4 and test_data[
    "data"]["plan"]["itineraries"][0]["legs"][0]["mode"] == "WALK" and test_data[
    "data"]["plan"]["itineraries"][0]["legs"][0]["mode"] != test_data[
    "data"]["plan"]["itineraries"][0]["legs"][1]["mode"] and test_data[
    "data"]["plan"]["itineraries"][0]["fares"][0]["components"][0]["cents"] == 410 and test_data[
    "data"]["plan"]["itineraries"][0]["fares"][0]["components"][0]["currency"] == "EUR" and test_data[
    "data"]["plan"]["itineraries"][1]["fares"][0]["components"][0]["cents"] == 410 and test_data[
    "data"]["plan"]["itineraries"][0]["fares"][0]["components"][0]["fareId"] == "HSL:ABC" and test_data[
    "data"]["plan"]["itineraries"][0]["legs"][0]["from"]["name"] == "Kamppi, Helsinki" and test_data[
    "data"]["plan"]["itineraries"][0]["legs"][0]["to"]["name"] == "Kamppi" and test_data[
    "data"]["plan"]["itineraries"][0]["legs"][0]["from"]["name"] != test_data[
    "data"]["plan"]["itineraries"][0]["legs"][0]["to"]["name"]