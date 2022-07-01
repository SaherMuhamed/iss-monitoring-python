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

is_on = True
while is_on:
    time.sleep(0.3)
    screen.update()
    station.showturtle()
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    api_data = response.json()

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

    station.goto(x=longitude*3, y=latitude*3)

screen.exitonclick()
