import csv
import os
from datetime import datetime

file_name = "sleep_data.csv"

def add_entry():
    date = datetime.now().strftime("%Y-%m-%d")

    sleep_hours = input("Sleep hours: ")
    sleep_time = input("Sleep time: ")
    wake_time = input("Wake time: ")
    screen_time = input("Screen time before sleep (mins): ")
    sleep_quality = input("Sleep Quality (1-10): ")
    wake_ups = input("Wake-ups (count): ")
    time_to_fall_asleep = input("Time to fall asleep (mins): ")
    mood = input("Mood (1-10): ")
    focus = input("Focus (1-10): ")

    row = [date, sleep_hours, sleep_time, wake_time, screen_time, sleep_quality, wake_ups, time_to_fall_asleep, mood, focus]

    file_exists = os.path.isfile(file_name)

    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        
        if not file_exists:
            writer.writerow(["Date", "Sleep Hours", "Sleep Time", "Wake Time", "Screen Time", "Sleep Quality", "Wake-ups", "Time to fall asleep", "Mood", "Focus"])
        
        writer.writerow(row)

    print("Sleep Data saved.")

add_entry()