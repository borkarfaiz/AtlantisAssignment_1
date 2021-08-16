import re

from geopy import distance 


def get_distance(coords_1, coords_2):
    return f"City 1 and City 2 are {round(distance.distance(coords_1, coords_2).km, 2)} km apart"


if __name__ == '__main__':
    city_1_coords = input("City 1: ").strip()
    group_pattern = re.compile(r"(\d+\.\d+).*(\d+\.\d+).*")
    city_1_coords = re.search(group_pattern, city_1_coords)
    while not city_1_coords:
        city_1_coords = input("City 1: ").strip()
        city_1_coords = re.search(group_pattern, city_1_coords)
    city_1_coords = float(city_1_coords.group(1)), float(city_1_coords.group(2))
    city_2_coords = input("City 2: ").strip()
    city_2_coords = re.search(group_pattern, city_2_coords)
    while not city_2_coords:
        city_2_coords = input("City 2: ").strip()
        city_2_coords = re.search(group_pattern, city_2_coords)
    city_2_coords = float(city_2_coords.group(1)), float(city_2_coords.group(2))
    
    print(get_distance(city_1_coords, city_2_coords))
