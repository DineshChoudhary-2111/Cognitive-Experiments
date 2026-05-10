import time
import random
import csv
from datetime import datetime

file_name = "reaction_data.csv"

print("Reaction Time Test (5 rounds)")
input("Press Enter to start...")

trials = []
n = 5

for i in range(n):
    print(f"\nRound {i+1}")
    
    delay = random.uniform(1, 3)
    time.sleep(delay)

    print("NOW!")

    start = time.time()
    input()
    end = time.time()

    reaction = end - start
    trials.append(reaction)

    print(f"Reaction time: {reaction:.3f} seconds")

avg = sum(trials) / len(trials)

date = datetime.now().strftime("%Y-%m-%d")

with open(file_name, "a", newline="") as file:
    writer = csv.writer(file)

    if file.tell() == 0:
        writer.writerow(["Date", "Reaction Time Avg"])

    writer.writerow([date, avg])

print("\n--- RESULTS ---")
print("All trials:", [round(t, 3) for t in trials])
print(f"Average reaction time: {avg:.3f} seconds")