import tkinter as tk
from tkinter import messagebox

import requests


# Function to fetch weather data
def fetch_weather():
    api_key = "7e455cbd3a2e4004bfc135437241711"  # Replace with your WeatherAPI key
    city = city_entry.get().strip()
    if not city:
        messagebox.showerror("Input Error", "Please enter a city name!")
        return

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            city_name = data["location"]["name"]
            country = data["location"]["country"]
            temperature = data["current"]["temp_c"]
            condition = data["current"]["condition"]["text"]
            humidity = data["current"]["humidity"]
            wind_speed = data["current"]["wind_kph"]

            weather_output.set(
                f"🌍 City: {city_name}, {country}\n"
                f"🌡️ Temperature: {temperature}°C\n"
                f"☁️ Condition: {condition}\n"
                f"💧 Humidity: {humidity}%\n"
                f"💨 Wind Speed: {wind_speed} km/h"
            )
        else:
            weather_output.set(
                f"Error: {data.get('error', {}).get('message', 'Unknown error occurred')}"
            )
    except Exception as e:
        weather_output.set(f"Error: Unable to fetch data.\nDetails: {e}")


# GUI setup
root = tk.Tk()
root.title("🌦️ Weather Data Fetcher")
root.geometry("450x400")
root.configure(bg="#f0f8ff")

# Title
title_label = tk.Label(
    root,
    text="Weather Data Fetcher",
    font=("Arial", 18, "bold"),
    bg="#f0f8ff",
    fg="#1e3d59",
)
title_label.pack(pady=10)

# City Input
city_frame = tk.Frame(root, bg="#f0f8ff")
city_frame.pack(pady=10)
city_label = tk.Label(
    city_frame, text="Enter City Name:", font=("Arial", 12), bg="#f0f8ff", fg="#333333"
)
city_label.pack(side=tk.LEFT, padx=5)
city_entry = tk.Entry(city_frame, font=("Arial", 12), width=25)
city_entry.pack(side=tk.LEFT, padx=5)

# Fetch Button
fetch_button = tk.Button(
    root,
    text="Fetch Weather",
    command=fetch_weather,
    font=("Arial", 12, "bold"),
    bg="#0073e6",
    fg="white",
    relief="flat",
)
fetch_button.pack(pady=10)

# Weather Output
weather_output = tk.StringVar(
    value="Enter a city name and click 'Fetch Weather' to view the details."
)
output_label = tk.Label(
    root,
    textvariable=weather_output,
    font=("Arial", 12),
    bg="#f0f8ff",
    fg="#333333",
    wraplength=400,
    justify="left",
)
output_label.pack(pady=20)

# Footer
footer_label = tk.Label(
    root,
    text="Powered by WeatherAPI",
    font=("Arial", 10),
    bg="#f0f8ff",
    fg="#555555",
)
footer_label.pack(side=tk.BOTTOM, pady=10)

# Start GUI
root.mainloop()
