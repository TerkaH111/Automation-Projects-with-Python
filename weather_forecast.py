import requests

API_KEY = ""
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = round(data["main"]["temp"] - 273.15, 2)

        print("Weather:", weather)
        print("Temperature: ", temperature, "Celcius")


    else:
        print("Sorry. An error occurred")


if __name__ == "__main__":
    city = input("Enter a city name: ")
    get_weather(city)
