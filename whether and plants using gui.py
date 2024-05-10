import random
import threading
import time
import tkinter as tk

class WeatherSimulatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Weather Simulator")

        self.weather_label = tk.Label(master, text="")
        self.weather_label.pack()

        self.alert_label = tk.Label(master, text="", fg="red")
        self.alert_label.pack()

        self.plant_location_label = tk.Label(master, text="")
        self.plant_location_label.pack()

        self.latitude = 37.7749  # Example latitude (San Francisco)
        self.longitude = -122.4194  # Example longitude (San Francisco)

        self.weather_thread = threading.Thread(target=self.weather_check_scheduler)
        self.weather_thread.daemon = True
        self.weather_thread.start()

    def simulate_weather(self):
        weather_conditions = ["sunny", "cloudy", "rainy", "stormy"]
        weather = random.choice(weather_conditions)
        temperature = random.randint(-10, 40)

        return weather, temperature

    def check_for_frost(self, temperature):
        if temperature < 0:
            self.alert_label.config(text="Frost Alert: Move your plants indoors!")
            self.plant_location_label.config(text="Keep plants indoors.")
        else:
            self.alert_label.config(text="")
            if "rain" in self.weather.lower() or "storm" in self.weather.lower():
                self.plant_location_label.config(text="Keep plants indoors.")
            else:
                self.plant_location_label.config(text="Keep plants outdoors.")

    def weather_check_scheduler(self):
        while True:
            self.weather, temperature = self.simulate_weather()
            simulated_weather = f"Simulated Weather: {self.weather}, Temperature: {temperature}°C"
            self.update_weather_label(simulated_weather)
            self.check_for_frost(temperature)
            time.sleep(5)  # Update weather every 5 seconds

    def update_weather_label(self, weather_info):
        self.weather_label.config(text=weather_info)

def main():
    root = tk.Tk()
    app = WeatherSimulatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
