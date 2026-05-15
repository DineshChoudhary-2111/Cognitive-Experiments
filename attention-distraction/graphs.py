import pandas as pd
import matplotlib.pyplot as plt
import os

base_dir = os.path.dirname(__file__)
csv_path = os.path.join(base_dir, "attention_data.csv")

df = pd.read_csv(csv_path)

graphs_dir = os.path.join(base_dir, "graphs")
os.makedirs(graphs_dir, exist_ok=True)

grouped = (
    df.groupby(["Participant", "Condition"])
    .mean(numeric_only=True)
    .reset_index()
)

participants = grouped["Participant"].unique()

x = range(len(participants))
width = 0.35

# ACCURACY GRAPH

control_acc = grouped[grouped["Condition"] == "control"]["Accuracy (%)"]
distraction_acc = grouped[grouped["Condition"] == "distraction"]["Accuracy (%)"]

plt.figure(figsize=(8, 5))

plt.bar(
    [i - width / 2 for i in x],
    control_acc,
    width=width,
    label="Control"
)

plt.bar(
    [i + width / 2 for i in x],
    distraction_acc,
    width=width,
    label="Distraction"
)

plt.xticks(x, participants)
plt.xlabel("Participants")
plt.ylabel("Accuracy (%)")
plt.title("Accuracy Comparison: Control vs Distraction")
plt.legend()

plt.tight_layout()

accuracy_path = os.path.join(graphs_dir, "accuracy_comparison.png")
plt.savefig(accuracy_path)

plt.close()

# PRECISION GRAPH

control_prec = grouped[grouped["Condition"] == "control"]["Precision (%)"]
distraction_prec = grouped[grouped["Condition"] == "distraction"]["Precision (%)"]

plt.figure(figsize=(8, 5))

plt.bar(
    [i - width / 2 for i in x],
    control_prec,
    width=width,
    label="Control"
)

plt.bar(
    [i + width / 2 for i in x],
    distraction_prec,
    width=width,
    label="Distraction"
)

plt.xticks(x, participants)
plt.xlabel("Participants")
plt.ylabel("Precision (%)")
plt.title("Precision Comparison: Control vs Distraction")
plt.legend()

plt.tight_layout()

precision_path = os.path.join(graphs_dir, "precision_comparison.png")
plt.savefig(precision_path)

plt.close()

# REACTION TIME GRAPH

control_rt = grouped[grouped["Condition"] == "control"]["Avg RT (s)"]
distraction_rt = grouped[grouped["Condition"] == "distraction"]["Avg RT (s)"]

plt.figure(figsize=(8, 5))

plt.bar(
    [i - width / 2 for i in x],
    control_rt,
    width=width,
    label="Control"
)

plt.bar(
    [i + width / 2 for i in x],
    distraction_rt,
    width=width,
    label="Distraction"
)

plt.xticks(x, participants)
plt.xlabel("Participants")
plt.ylabel("Reaction Time (s)")
plt.title("Reaction Time Comparison: Control vs Distraction")
plt.legend()

plt.tight_layout()

rt_path = os.path.join(graphs_dir, "reaction_time_comparison.png")
plt.savefig(rt_path)

plt.close()

# FALSE POSITIVES GRAPH

control_false = grouped[grouped["Condition"] == "control"]["False Positives"]
distraction_false = grouped[grouped["Condition"] == "distraction"]["False Positives"]

plt.figure(figsize=(8, 5))

plt.bar(
    [i - width / 2 for i in x],
    control_false,
    width=width,
    label="Control"
)

plt.bar(
    [i + width / 2 for i in x],
    distraction_false,
    width=width,
    label="Distraction"
)

plt.xticks(x, participants)
plt.xlabel("Participants")
plt.ylabel("False Positives")
plt.title("False Positive Comparison: Control vs Distraction")
plt.legend()

plt.tight_layout()

false_path = os.path.join(graphs_dir, "false_positive_comparison.png")
plt.savefig(false_path)

plt.close()

print("\nAll graphs generated successfully.")
print(f"\nGraphs saved in:\n{graphs_dir}")