import math
import requests

import requests

from haversine import haversine, Unit

def can_pickup_user(first_user_route, second_user_source, second_user_destination, max_distance_km):
    # Check if the second user's source is within max_distance_km of the route
    for point in first_user_route:
        distance_to_source = haversine(point, second_user_source, unit=Unit.KILOMETERS)
        if distance_to_source <= max_distance_km:
            return True

    # Iterate through the points in the first user's route
    for i in range(len(first_user_route) - 1):
        start_point = first_user_route[i]
        end_point = first_user_route[i + 1]

        # Check if the second user's destination is within max_distance_km of the route segment
        distance_to_destination = haversine(start_point, second_user_destination, unit=Unit.KILOMETERS)
        if distance_to_destination <= max_distance_km:
            return True

        # Check if the destination is on the line segment
        line_segment = [start_point, end_point]
        if is_point_on_line(second_user_destination, line_segment, max_distance_km):
            return True

    return False

def is_point_on_line(point, line_segment, max_distance_km):
    # Calculate the distances from the point to the endpoints of the line segment
    distance_to_start = haversine(line_segment[0], point, unit=Unit.KILOMETERS)
    distance_to_end = haversine(line_segment[1], point, unit=Unit.KILOMETERS)

    # Check if the point is within max_distance_km of the line segment
    return min(distance_to_start, distance_to_end) <= max_distance_km

# Example usage:
first_user_route = [(0.0, 0.0), (1.0, 1.0), (2.0, 2.0), (3.0, 3.0)]  # Example route
second_user_source = (1, 1)  # Example source of the second user
second_user_destination = (1.5, 1.5)  # Example destination of the second user
max_distance_km = 5.0  # Maximum distance in kilometers for pickup

if can_pickup_user(first_user_route, second_user_source, second_user_destination, max_distance_km):
    print("The first user can pick up the second user along the route.")
else:
    print("The first user cannot pick up the second user along the route.")





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

