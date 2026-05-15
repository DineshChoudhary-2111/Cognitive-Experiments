import pandas as pd
import matplotlib.pyplot as plt
import os

base_dir = os.path.dirname(__file__)
csv_path = os.path.join(base_dir, "decision_load_results.csv")

df = pd.read_csv(csv_path)

# convert numeric safely
df["Accuracy"] = pd.to_numeric(df["Accuracy"], errors="coerce")
df["Avg_RT"] = pd.to_numeric(df["Avg_RT"], errors="coerce")
df["Avg_Confidence"] = pd.to_numeric(df["Avg_Confidence"], errors="coerce")
df["Memory_Accuracy"] = pd.to_numeric(df["Memory_Accuracy"], errors="coerce")
df["Memory_RT"] = pd.to_numeric(df["Memory_RT"], errors="coerce")

graphs_dir = os.path.join(base_dir, "graphs")
os.makedirs(graphs_dir, exist_ok=True)

grouped = df.groupby(["Type", "Load"]).mean(numeric_only=True).reset_index()

participants = df["Participant"].unique()

x = range(len(participants))
width = 0.35


# =========================
# 1. ACCURACY GRAPH
# =========================
plt.figure(figsize=(8, 5))

int_load = grouped[(grouped["Type"] == "intuitive") & (grouped["Load"] == "LOAD")]["Accuracy"]
int_no = grouped[(grouped["Type"] == "intuitive") & (grouped["Load"] == "NO LOAD")]["Accuracy"]

ana_load = grouped[(grouped["Type"] == "analytical") & (grouped["Load"] == "LOAD")]["Accuracy"]
ana_no = grouped[(grouped["Type"] == "analytical") & (grouped["Load"] == "NO LOAD")]["Accuracy"]

plt.bar(x, int_load, width=width, label="Intuitive Load")
plt.bar(x, int_no, width=width, label="Intuitive No Load")

plt.xticks(x, participants)
plt.title("Decision Accuracy Comparison")
plt.xlabel("Participants")
plt.ylabel("Accuracy (%)")
plt.legend()

plt.tight_layout()
plt.savefig(os.path.join(graphs_dir, "decision_accuracy_comparison.png"))
plt.close()


# =========================
# 2. REACTION TIME GRAPH
# =========================
plt.figure(figsize=(8, 5))

int_rt_load = grouped[(grouped["Type"] == "intuitive") & (grouped["Load"] == "LOAD")]["Avg_RT"]
int_rt_no = grouped[(grouped["Type"] == "intuitive") & (grouped["Load"] == "NO LOAD")]["Avg_RT"]

plt.bar(x, int_rt_load, width=width, label="Load")
plt.bar(x, int_rt_no, width=width, label="No Load")

plt.xticks(x, participants)
plt.title("Response Time Comparison")
plt.xlabel("Participants")
plt.ylabel("Time (s)")
plt.legend()

plt.tight_layout()
plt.savefig(os.path.join(graphs_dir, "reaction_time_comparison.png"))
plt.close()


# =========================
# 3. CONFIDENCE GRAPH
# =========================
plt.figure(figsize=(8, 5))

conf_load = grouped[(grouped["Type"] == "intuitive") & (grouped["Load"] == "LOAD")]["Avg_Confidence"]
conf_no = grouped[(grouped["Type"] == "intuitive") & (grouped["Load"] == "NO LOAD")]["Avg_Confidence"]

plt.bar(x, conf_load, width=width, label="Load")
plt.bar(x, conf_no, width=width, label="No Load")

plt.xticks(x, participants)
plt.title("Confidence Comparison")
plt.xlabel("Participants")
plt.ylabel("Confidence (1-5)")
plt.legend()

plt.tight_layout()
plt.savefig(os.path.join(graphs_dir, "confidence_comparison.png"))
plt.close()


# =========================
# 4. MEMORY ACCURACY
# =========================
mem = df[df["Memory_Accuracy"].notna()]
mem_group = mem.groupby("Participant")["Memory_Accuracy"].mean()

plt.figure(figsize=(8, 5))
plt.bar(mem_group.index, mem_group.values)
plt.title("Memory Accuracy (Load Condition)")
plt.xlabel("Participants")
plt.ylabel("Accuracy (%)")

plt.tight_layout()
plt.savefig(os.path.join(graphs_dir, "memory_accuracy.png"))
plt.close()


# =========================
# 5. MEMORY RECALL TIME
# =========================
mem_rt_group = mem.groupby("Participant")["Memory_RT"].mean()

plt.figure(figsize=(8, 5))
plt.bar(mem_rt_group.index, mem_rt_group.values)
plt.title("Memory Recall Time (Load Condition)")
plt.xlabel("Participants")
plt.ylabel("Time (s)")

plt.tight_layout()
plt.savefig(os.path.join(graphs_dir, "memory_recall_time.png"))
plt.close()


# =========================
# 6. RISK CHOICES
# =========================
risk = df[df["Type"] == "risk"]
risk_a = risk.groupby("Participant")["Risk_A"].apply(lambda x: pd.to_numeric(x, errors='coerce').sum())
risk_b = risk.groupby("Participant")["Risk_B"].apply(lambda x: pd.to_numeric(x, errors='coerce').sum())

plt.figure(figsize=(8, 5))
plt.bar(risk_a.index, risk_a.values, label="A Choices")
plt.bar(risk_b.index, risk_b.values, label="B Choices")

plt.title("Risk Choice Distribution")
plt.xlabel("Participants")
plt.ylabel("Count")
plt.legend()

plt.tight_layout()
plt.savefig(os.path.join(graphs_dir, "risk_choice_distribution.png"))
plt.close()


print("All graphs generated successfully.")
print(f"Saved in: {graphs_dir}")