from FlightRadar24 import FlightRadar24API
import pyautogui
from dotenv import load_dotenv
import os
import time

load_dotenv()

fr_api = FlightRadar24API()
print("Connected to api")
bounds = fr_api.get_bounds_by_point(float(os.getenv("LONG")), float(os.getenv("LAT")), int(os.getenv("RADIUS")))

found_flights = False
while True:
    flights = fr_api.get_flights(bounds=bounds)
    if len(flights) > 0 and not found_flights:
        found_flights = True
        print(f"Found flights {flights}")
        print("Muting...")
        pyautogui.hotkey("alt", "m")
    elif len(flights) == 0 and found_flights: 
        found_flights = False
        print("No flights found. Unmuting...")
        pyautogui.hotkey("alt", "m")
    time.sleep(5)