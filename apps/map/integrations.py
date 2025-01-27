
import requests

def get_route_from_google(start, end, waypoints=None):
    api_key = "AIzaSyDYo7qzywWRdDoRS11XgGYzQ26uxKfqhv0"
    url = "https://maps.googleapis.com/maps/api/directions/json"

    params = {
        "origin": start,
        "destination": end,
        "key": api_key,
    }
    if waypoints:
        params["waypoints"] = "|".join(waypoints)

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return None
