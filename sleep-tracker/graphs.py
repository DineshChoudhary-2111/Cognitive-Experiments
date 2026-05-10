import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("final_data.csv")

plt.style.use("seaborn-v0_8")


# =====================================================
# GROUP 1 — SLEEP → COGNITIVE SPEED (REACTION TIME)
# =====================================================
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
plt.title("1. Sleep Hours → Reaction Speed")

print("Corr (Sleep Hours vs Reaction):", x.corr(y))


# 2. Sleep Quality vs Reaction Time
plt.subplot(1, 3, 2)
x = data["Sleep Quality"].astype(float)

plt.scatter(x, y)
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b)

plt.xlabel("Sleep Quality (1–10)")
plt.title("2. Sleep Quality → Reaction Speed")

print("Corr (Quality vs Reaction):", x.corr(y))


# 3. Screen Time vs Reaction Time
plt.subplot(1, 3, 3)
x = data["Screen Time"].astype(float)

plt.scatter(x, y)
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b)

plt.xlabel("Screen Time (min)")
plt.title("3. Screen Time → Reaction Speed")

print("Corr (Screen vs Reaction):", x.corr(y))

plt.tight_layout()
plt.show()


# =====================================================
# GROUP 2 — SLEEP → MEMORY PERFORMANCE
# =====================================================
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
plt.title("1. Sleep → Memory Retention")

print("Corr (Sleep Hours vs Memory):", x.corr(y))


# 2. Sleep Quality vs Memory
plt.subplot(1, 3, 2)
x = data["Sleep Quality"].astype(float)

plt.scatter(x, y)
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b)

plt.xlabel("Sleep Quality")
plt.title("2. Quality → Memory")

print("Corr (Quality vs Memory):", x.corr(y))


# 3. Sleep Latency vs Memory
plt.subplot(1, 3, 3)
x = data["Time to fall asleep"].astype(float)

plt.scatter(x, y)
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b)

plt.xlabel("Sleep Latency (min)")
plt.title("3. Sleep Latency → Memory")

print("Corr (Latency vs Memory):", x.corr(y))

plt.tight_layout()
plt.show()


# =====================================================
# GROUP 3 — MEMORY ↔ REACTION (COGNITIVE LINK)
# =====================================================
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
plt.title("1. Memory ↔ Speed")

print("Corr (Memory vs Reaction):", x.corr(y))


# 2. Memory vs Focus
plt.subplot(1, 3, 2)
y2 = data["Focus"].astype(float)

plt.scatter(x, y2)
m, b = np.polyfit(x, y2, 1)
plt.plot(x, m*x + b)

plt.xlabel("Memory Score")
plt.title("2. Memory ↔ Focus")

print("Corr (Memory vs Focus):", x.corr(y2))


# 3. Memory vs Mood
plt.subplot(1, 3, 3)
y3 = data["Mood"].astype(float)

plt.scatter(x, y3)
m, b = np.polyfit(x, y3, 1)
plt.plot(x, m*x + b)

plt.xlabel("Memory Score")
plt.title("3. Memory ↔ Mood")

print("Corr (Memory vs Mood):", x.corr(y3))

plt.tight_layout()
plt.show()


# =====================================================
# GROUP 4 — OVERALL BRAIN PERFORMANCE MODEL
# =====================================================
plt.figure(figsize=(6, 4))

# Sleep Quality vs Combined Cognition (Memory + Reaction avg concept)
x = data["Sleep Quality"].astype(float)
y = (data["Memory Score"] + data["Reaction Time Avg"]) / 2

plt.scatter(x, y)
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b)

plt.xlabel("Sleep Quality")
plt.ylabel("Combined Cognitive Score")
plt.title("1. Sleep → Overall Brain Performance")

print("Overall Correlation:", x.corr(y))

plt.show()