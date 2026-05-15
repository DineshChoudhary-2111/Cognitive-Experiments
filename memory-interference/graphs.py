import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
import os

base_dir = os.path.dirname(__file__)
csv_path = os.path.join(base_dir, "memory_interference.csv")

df = pd.read_csv(csv_path)

graphs_dir = os.path.join(base_dir, "graphs")
os.makedirs(graphs_dir, exist_ok=True)

df["Avg Interference Accuracy (%)"] = pd.to_numeric(
    df["Avg Interference Accuracy (%)"],
    errors="coerce"
)

grouped = (
    df.groupby(["Participant", "Condition"])
    .mean(numeric_only=True)
    .reset_index()
)

participants = grouped["Participant"].unique()

x = range(len(participants))
width = 0.35

# GRAPH 1 — MEMORY ACCURACY

control_mem = grouped[grouped["Condition"] == "control"]["Avg Memory Accuracy (%)"]
interference_mem = grouped[grouped["Condition"] == "interference"]["Avg Memory Accuracy (%)"]

plt.figure(figsize=(8, 5))

plt.bar(
    [i - width / 2 for i in x],
    control_mem,
    width=width,
    label="Control"
)

plt.bar(
    [i + width / 2 for i in x],
    interference_mem,
    width=width,
    label="Interference"
)

plt.xticks(x, participants)
plt.xlabel("Participants")
plt.ylabel("Memory Accuracy (%)")
plt.title("Memory Accuracy: Control vs Interference")
plt.legend()

plt.tight_layout()

plt.savefig(os.path.join(graphs_dir, "memory_accuracy_comparison.png"))
plt.close()

# GRAPH 2 — RECALL TIME

control_rt = grouped[grouped["Condition"] == "control"]["Avg Recall Time (s)"]
interference_rt = grouped[grouped["Condition"] == "interference"]["Avg Recall Time (s)"]

plt.figure(figsize=(8, 5))

plt.bar(
    [i - width / 2 for i in x],
    control_rt,
    width=width,
    label="Control"
)

plt.bar(
    [i + width / 2 for i in x],
    interference_rt,
    width=width,
    label="Interference"
)

plt.xticks(x, participants)
plt.xlabel("Participants")
plt.ylabel("Recall Time (s)")
plt.title("Recall Time: Control vs Interference")
plt.legend()

plt.tight_layout()

plt.savefig(os.path.join(graphs_dir, "recall_time_comparison.png"))
plt.close()

# GRAPH 3 — INTERFERENCE TASK ACCURACY

interference_only = grouped[grouped["Condition"] == "interference"]

plt.figure(figsize=(8, 5))

plt.bar(
    participants,
    interference_only["Avg Interference Accuracy (%)"]
)

plt.xlabel("Participants")
plt.ylabel("Interference Task Accuracy (%)")
plt.title("Arithmetic Interference Task Accuracy")

plt.tight_layout()

plt.savefig(os.path.join(graphs_dir, "interference_accuracy.png"))
plt.close()

# GRAPH 4 — PARTICIPANT MEMORY PERFORMANCE

plt.figure(figsize=(8, 5))

for participant in participants:

    pdata = grouped[grouped["Participant"] == participant]

    plt.plot(
        pdata["Condition"],
        pdata["Avg Memory Accuracy (%)"],
        marker="o",
        label=f"Participant {participant}"
    )

plt.xlabel("Condition")
plt.ylabel("Memory Accuracy (%)")
plt.title("Participant-wise Memory Accuracy Trends")
plt.legend()

plt.tight_layout()

plt.savefig(os.path.join(graphs_dir, "participant_memory_accuracy.png"))
plt.close()

print("\nAll graphs generated successfully.")
print(f"\nGraphs saved in:\n{graphs_dir}")