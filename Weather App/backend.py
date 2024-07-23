import requests

API_KEY = "141710af2113bab9f55ef73e1bcd33d5"

def get_data(place, days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    req = requests.get(url)
    data = req.json()
    filtered_data = data ["list"]
    n = 8*days
    filtered_data = filtered_data[:n]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Tokyo",days=3))