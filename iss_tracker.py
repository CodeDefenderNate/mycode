#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime
import reverse_geocoder as rq

URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()

    lat= resp["iss_position"]["latitude"]
    lon= resp["iss_position"]["longitude"]

    ts= resp["timestamp"]
    ts = datetime.datetime.fromtimestamp(ts)

    locator_resp= rq.search((lat, lon))

    city= locator_resp[0]["name"]
    country= locator_resp[0]["cc"]

    print(f"""
    CURRENT LOCATION OF THE ISS:
    Timstamp: {ts}
    Lat: {lat}
    Lon: {lon}
    City/Country: {city}, {country}
    """)

if __name__ == "__main__":
    main()

