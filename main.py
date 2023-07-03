import requests
from turtle import Screen
from iss import Station, Information
import time

FONT = ('Courier', 12, 'bold')

# TODO: Setup the screen.
screen = Screen()
screen.title("ISS Monitoring")
screen.bgpic("images/world_map.png")
screen.tracer(0)
screen.setup(width=1080, height=540)

station = Station()
long_info = Information()
lat_info = Information()

long_info.goto(x=-530, y=-190)
lat_info.goto(x=-530, y=-210)


def get_location(website_url):
    try:
        return requests.get(url=website_url).json()
    except requests.exceptions.ConnectionError:
        pass


is_on = True
while is_on:
    time.sleep(0.7)
    screen.update()
    station.showturtle()

    api_data = get_location(website_url="http://api.open-notify.org/iss-now.json")
    longitude = float(api_data["iss_position"]["longitude"])
    latitude = float(api_data["iss_position"]["latitude"])

    # TODO: Update latitude & longitude info.
    long_info.clear()
    long_info.write(f"longitude: {longitude}", font=FONT)
    lat_info.clear()
    lat_info.write(f"latitude: {latitude}", font=FONT)

    # TODO: Debugging the output from api.
    iss_position = (longitude, latitude)
    print(iss_position)

    station.goto(x=longitude * 3, y=latitude * 3)

screen.exitonclick()
