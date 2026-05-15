import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

base_dir = os.path.dirname(__file__)
csv_path = os.path.join(base_dir, "final_data.csv")

data = pd.read_csv(csv_path)

graphs_dir = os.path.join(base_dir, "graphs")
os.makedirs(graphs_dir, exist_ok=True)

plt.style.use("seaborn-v0_8")


# GROUP 1 — SLEEP → REACTION TIME

plt.figure(figsize=(12, 4))

# 1. Sleep Hours vs Reaction Time
plt.subplot(1, 3, 1)
x = data["Sleep Hours"].astype(float)
y = data["Reaction Time Avg"].astype(float)

plt.scatter(x, y)
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b)

plt.xlabel("Sleep Hours")
plt.ylabel("Reaction Time (sec)")
plt.title("Sleep Hours → Reaction Time")

# 2. Sleep Quality vs Reaction Time
plt.subplot(1, 3, 2)
x = data["Sleep Quality"].astype(float)

plt.scatter(x, y)
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b)

plt.xlabel("Sleep Quality")
plt.title("Sleep Quality → Reaction Time")

# 3. Screen Time vs Reaction Time
plt.subplot(1, 3, 3)
x = data["Screen Time"].astype(float)

plt.scatter(x, y)
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b)

plt.xlabel("Screen Time (min)")
plt.title("Screen Time → Reaction Time")

plt.tight_layout()

path1 = os.path.join(graphs_dir, "reaction_time_sleep.png")
plt.savefig(path1)
plt.close()


# GROUP 2 — SLEEP → MEMORY PERFORMANCE

plt.figure(figsize=(12, 4))

# 1. Sleep Hours vs Memory
plt.subplot(1, 3, 1)
x = data["Sleep Hours"].astype(float)
y = data["Memory Score"].astype(float)

plt.scatter(x, y)
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b)

plt.xlabel("Sleep Hours")
plt.ylabel("Memory Score (%)")
plt.title("Sleep → Memory")

# 2. Sleep Quality vs Memory
plt.subplot(1, 3, 2)
x = data["Sleep Quality"].astype(float)

plt.scatter(x, y)
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b)

plt.xlabel("Sleep Quality")
plt.title("Quality → Memory")

# 3. Sleep Latency vs Memory
plt.subplot(1, 3, 3)
x = data["Time to fall asleep"].astype(float)

plt.scatter(x, y)
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b)

plt.xlabel("Sleep Latency (min)")
plt.title("Latency → Memory")

plt.tight_layout()

path2 = os.path.join(graphs_dir, "memory_sleep.png")
plt.savefig(path2)
plt.close()


# GROUP 3 — MEMORY ↔ COGNITIVE STATE

plt.figure(figsize=(12, 4))

# 1. Memory vs Reaction Time
plt.subplot(1, 3, 1)
x = data["Memory Score"].astype(float)
y = data["Reaction Time Avg"].astype(float)

plt.scatter(x, y)
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b)

plt.xlabel("Memory Score")
plt.ylabel("Reaction Time")
plt.title("Memory ↔ Speed")

# 2. Memory vs Focus
plt.subplot(1, 3, 2)
y2 = data["Focus"].astype(float)

plt.scatter(x, y2)
m, b = np.polyfit(x, y2, 1)
plt.plot(x, m*x + b)

plt.xlabel("Memory Score")
plt.title("Memory ↔ Focus")

# 3. Memory vs Mood
plt.subplot(1, 3, 3)
y3 = data["Mood"].astype(float)

plt.scatter(x, y3)
m, b = np.polyfit(x, y3, 1)
plt.plot(x, m*x + b)

plt.xlabel("Memory Score")
plt.title("Memory ↔ Mood")

plt.tight_layout()

path3 = os.path.join(graphs_dir, "memory_cognition.png")
plt.savefig(path3)
plt.close()


# GROUP 4 — OVERALL COGNITIVE SCORE MODEL

plt.figure(figsize=(6, 4))

x = data["Sleep Quality"].astype(float)
y = (data["Memory Score"] + data["Reaction Time Avg"]) / 2

plt.scatter(x, y)
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b)

plt.xlabel("Sleep Quality")
plt.ylabel("Combined Cognitive Score")
plt.title("Sleep Quality → Overall Performance")

path4 = os.path.join(graphs_dir, "overall_cognitive.png")
plt.savefig(path4)
plt.close()


print("\nALL GRAPHS GENERATED SUCCESSFULLY")
print(f"Saved in: {graphs_dir}")