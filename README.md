🌦️ Weather Data Fetcher
Weather Data Fetcher is a Python-based desktop application that fetches current weather data for any city using the WeatherAPI. Built with tkinter, it provides a simple, user-friendly interface to display real-time weather information.

📋 Features
City Input: Enter any city to fetch its current weather details.
Weather Details:
🌡️ Temperature (°C)
☁️ Weather Condition
💧 Humidity (%)
💨 Wind Speed (km/h)
Error Handling:
Alerts for invalid inputs or network issues.
Descriptive error messages for API failures.
Modern Design: Clean and intuitive interface with responsive layouts.
🛠️ Installation and Setup
Prerequisites
Python 3.8 or later installed.
requests library installed:
bash
Copy code
pip install requests
Setup Instructions
Clone or download this repository.
Obtain a free API key from WeatherAPI.
Replace the api_key in the script with your WeatherAPI key:
python
Copy code
api_key = "YOUR_API_KEY"
Run the script:
bash
Copy code
python weather_fetcher.py
🚀 Usage
Launch the application.
Enter a city name in the input field.
Click the "Fetch Weather" button.
View the current weather details displayed below.
🖥️ Application Preview

Sample view of the Weather Data Fetcher application

📂 File Structure
bash
Copy code
.
├── weather_fetcher.py   # Main application script
├── README.md            # Documentation file
└── requirements.txt     # Python dependencies
🤔 Troubleshooting
No API Key or Invalid Key: Ensure you've replaced the placeholder API key with a valid key from WeatherAPI.

Network Issues: Check your internet connection and try again.

Invalid City Name: Double-check the spelling or try searching for nearby major cities.

💡 Future Enhancements
Add support for multiple weather providers.
Include forecast data for the next few days.
Implement location auto-detection using IP geolocation.

❤️ Acknowledgments
WeatherAPI for providing weather data.
Python community for their amazing tools and libraries.
If you have any feedback or suggestions, feel free to reach out! 😊
