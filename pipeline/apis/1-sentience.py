#!/usr/bin/env python3
"""Find the home planets of all sentient species in Star Wars."""
import requests


def sentientPlanets():
    """Return the names of the home planets of all sentient species.

    Uses the Swapi API and follows the pagination until there is no
    next page. A species is sentient if its classification or its
    designation is "sentient".

    Returns:
        list: Names of the home planets of the sentient species.
    """
    planets = []
    url = "https://swapi-api.hbtn.io/api/species/"
    while url:
        response = requests.get(url)
        if response.status_code != 200:
            break
        data = response.json()
        for species in data.get("results", []):
            classification = species.get("classification", "")
            designation = species.get("designation", "")
            if "sentient" not in (classification, designation):
                continue
            homeworld = species.get("homeworld")
            if not homeworld:
                continue
            planet = requests.get(homeworld)
            if planet.status_code == 200:
                planets.append(planet.json().get("name"))
        url = data.get("next")
    return planets
