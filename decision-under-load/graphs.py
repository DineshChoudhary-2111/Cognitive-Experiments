import pandas as pd
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "decision_load_results.csv")

df = pd.read_csv(csv_path)

graphs_dir = os.path.join(BASE_DIR, "graphs")

if not os.path.exists(graphs_dir):
    os.makedirs(graphs_dir)

decision_df = df[df["Type"].isin(["intuitive", "analytical"])].copy()

decision_df["Accuracy"] = pd.to_numeric(
    decision_df["Accuracy"],
    errors="coerce"
)

decision_df["Avg_RT"] = pd.to_numeric(
    decision_df["Avg_RT"],
    errors="coerce"
)

decision_df["Avg_Confidence"] = pd.to_numeric(
    decision_df["Avg_Confidence"],
    errors="coerce"
)

decision_df["Memory_Accuracy"] = pd.to_numeric(
    decision_df["Memory_Accuracy"],
    errors="coerce"
)

risk_df = df[df["Type"] == "risk"].copy()

risk_df["Risk_A"] = pd.to_numeric(
    risk_df["Risk_A"],
    errors="coerce"
)

risk_df["Risk_B"] = pd.to_numeric(
    risk_df["Risk_B"],
    errors="coerce"
)
# GRAPH 1
# Accuracy under load

acc = decision_df.groupby(
    ["Type", "Load"]
)["Accuracy"].mean().unstack()

plt.figure(figsize=(8, 5))

for condition in acc.index:
    plt.plot(
        acc.columns,
        acc.loc[condition],
        marker='o',
        label=condition.capitalize()
    )

plt.title("Decision Accuracy Under Cognitive Load")
plt.ylabel("Accuracy (%)")
plt.xlabel("Condition")
plt.grid(True)
plt.legend()

plt.savefig(
    os.path.join(graphs_dir, "accuracy_under_load.png"),
    bbox_inches="tight"
)

plt.close()

# GRAPH 2
# Response time comparison

rt = decision_df.groupby(
    ["Type", "Load"]
)["Avg_RT"].mean().unstack()

plt.figure(figsize=(8, 5))

for condition in rt.index:
    plt.plot(
        rt.columns,
        rt.loc[condition],
        marker='o',
        label=condition.capitalize()
    )

plt.title("Response Time Under Cognitive Load")
plt.ylabel("Average Response Time (s)")
plt.xlabel("Condition")
plt.grid(True)
plt.legend()

plt.savefig(
    os.path.join(graphs_dir, "response_time_under_load.png"),
    bbox_inches="tight"
)

plt.close()

# GRAPH 3
# Confidence levels

conf = decision_df.groupby(
    ["Type", "Load"]
)["Avg_Confidence"].mean().unstack()

plt.figure(figsize=(8, 5))

for condition in conf.index:
    plt.plot(
        conf.columns,
        conf.loc[condition],
        marker='o',
        label=condition.capitalize()
    )

plt.title("Confidence Levels Under Cognitive Load")
plt.ylabel("Average Confidence")
plt.xlabel("Condition")
plt.grid(True)
plt.legend()

plt.savefig(
    os.path.join(graphs_dir, "confidence_levels.png"),
    bbox_inches="tight"
)

plt.close()

# GRAPH 4
# Risk choice distribution

risk_choices = risk_df.groupby("Load")[["Risk_A", "Risk_B"]].mean()

risk_choices.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Risk Preference Under Load")
plt.ylabel("Average Choices")
plt.xlabel("Condition")
plt.xticks(rotation=0)

plt.savefig(
    os.path.join(graphs_dir, "risk_preferences.png"),
    bbox_inches="tight"
)

plt.close()

# GRAPH 5
# Memory performance

memory = decision_df[
    decision_df["Load"] == "LOAD"
]

mem_acc = memory.groupby(
    "Type"
)["Memory_Accuracy"].mean()

plt.figure(figsize=(8, 5))

plt.bar(
    mem_acc.index,
    mem_acc.values
)

plt.title("Memory Recall Accuracy During Cognitive Load")
plt.ylabel("Memory Accuracy (%)")
plt.xlabel("Decision Type")

plt.savefig(
    os.path.join(graphs_dir, "memory_accuracy.png"),
    bbox_inches="tight"
)

plt.close()

print("All graphs generated successfully.")
print(f"Graphs saved in: {graphs_dir}")