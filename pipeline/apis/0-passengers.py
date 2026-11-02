#!/usr/bin/env python3
"""Find Star Wars ships that can hold a given number of passengers."""
import requests


def availableShips(passengerCount):
    """Return the ships that can hold at least passengerCount people.

    Uses the Swapi API and follows the pagination until there is no
    next page.

    Args:
        passengerCount (int): Minimum number of passengers needed.

    Returns:
        list: Names of the ships that can hold passengerCount or more
        passengers. Empty list if no ship is available.
    """
    ships = []
    url = "https://swapi-api.hbtn.io/api/starships/"
    while url:
        response = requests.get(url)
        if response.status_code != 200:
            break
        data = response.json()
        for ship in data.get("results", []):
            passengers = ship.get("passengers", "").replace(",", "")
            try:
                capacity = int(passengers)
            except ValueError:
                continue
            if capacity >= passengerCount:
                ships.append(ship["name"])
        url = data.get("next")
    return ships
