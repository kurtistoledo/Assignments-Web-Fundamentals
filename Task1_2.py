# Lesson 1: Assignments | Web Fundamentals
# 2. Exploring the Digital Cosmos with Python and the Web

import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    planet_info = []
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']['massValue'] * (10 ** planet['mass']['massExponent']) if planet['mass'] else 'Unknown'
            orbit_period = planet['sideralOrbit'] if planet['sideralOrbit'] else 'Unknown'
            planet_info.append({
                'name': name,
                'mass': mass,
                'orbit_period': orbit_period
            })

    return planet_info

def find_heaviest_planet(planets):
    heaviest_planet = max(planets, key=lambda x: x['mass'] if x['mass'] != 'Unknown' else 0)
    return heaviest_planet

# Fetch and display planet data
planet_data = fetch_planet_data()
for planet in planet_data:
    print(f"Planet: {planet['name']}, Mass: {planet['mass']}, Orbit Period: {planet['orbit_period']} days")

# Identify and display the heaviest planet
heaviest_planet = find_heaviest_planet(planet_data)
print("\nHeaviest Planet:")
print(f"Planet: {heaviest_planet['name']}, Mass: {heaviest_planet['mass']}")
