import random
import time
import csv
from datetime import datetime

file_name = "memory_data.csv"

print("Working Memory Task")
input("Press Enter to start...")

trials = 5

for t in range(trials):
    print(f"\n--- Trial {t+1} ---")

    sequence_length = random.randint(4, 7)
    sequence = [random.randint(1, 30) for _ in range(sequence_length)]

    print("Memorize this sequence:")
    print(sequence)

    time.sleep(4)
    print("\n" * 40)

    print("INTERFERENCE PHASE")

    end_time = time.time() + 5
    while time.time() < end_time:
        a = random.randint(10, 99)
        b = random.randint(10, 99)
        print(f"{a} + {b}")
        time.sleep(0.5)

    start_time = time.time()
    user_input = input("\nEnter sequence (space-separated): ")
    end_time = time.time()

    response_time = end_time - start_time

    try:
        user_sequence = list(map(int, user_input.split()))
    except:
        user_sequence = []

    correct = 0
    for i in range(min(len(sequence), len(user_sequence))):
        if sequence[i] == user_sequence[i]:
            correct += 1

    score = (correct / sequence_length) * 100

    date = datetime.now().strftime("%Y-%m-%d")

    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow([
                "Date",
                "Trial",
                "Sequence Length",
                "Memory Score",
                "Response Time"
            ])

        writer.writerow([
            date,
            t + 1,
            sequence_length,
            round(score, 2),
            round(response_time, 3)
        ])

    print(f"Score: {score:.2f}% | Time: {response_time:.2f}s")