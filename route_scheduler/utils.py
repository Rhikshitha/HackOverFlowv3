import math
def haversine(coord1, coord2):
    # Radius of the Earth in meters
    earth_radius = 6371000

    # Convert latitude and longitude from degrees to radians
    lat1, lon1 = math.radians(coord1[1]), math.radians(coord1[0])
    lat2, lon2 = math.radians(coord2[1]), math.radians(coord2[0])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = earth_radius * c

    return distance

def are_coordinates_nearby(coord1, coordinates, max_distance):
    for coord2 in coordinates:
        if haversine(coord1, coord2) <= max_distance:
            return True
    return False

