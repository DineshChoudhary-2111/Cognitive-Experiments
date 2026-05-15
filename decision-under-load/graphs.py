import pandas as pd
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import os

# -----------------------------
# LOAD CSV
# -----------------------------
base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, "decision_load_results.csv")

df = pd.read_csv(csv_path)

# -----------------------------
# CLEAN DATA
# -----------------------------
df["Accuracy"] = pd.to_numeric(df["Accuracy"], errors="coerce")
df["Avg_RT"] = pd.to_numeric(df["Avg_RT"], errors="coerce")
df["Avg_Confidence"] = pd.to_numeric(df["Avg_Confidence"], errors="coerce")
df["Memory_Accuracy"] = pd.to_numeric(df["Memory_Accuracy"], errors="coerce")

# -----------------------------
# CREATE GRAPHS FOLDER
# -----------------------------
graphs_dir = os.path.join(base_dir, "graphs")

if not os.path.exists(graphs_dir):
    os.makedirs(graphs_dir)

# =====================================================
# GRAPH 1 — ANALYTICAL ACCURACY
# =====================================================

analytical = df[df["Type"] == "analytical"]

analytical_acc = analytical.groupby("Load")["Accuracy"].mean()

plt.figure(figsize=(8, 5))
analytical_acc.plot(kind="bar")

plt.title("Analytical Accuracy Under Load")
plt.ylabel("Accuracy (%)")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig(os.path.join(graphs_dir, "analytical_accuracy.png"))
plt.close()

# =====================================================
# GRAPH 2 — INTUITIVE ACCURACY
# =====================================================

intuitive = df[df["Type"] == "intuitive"]

intuitive_acc = intuitive.groupby("Load")["Accuracy"].mean()

plt.figure(figsize=(8, 5))
intuitive_acc.plot(kind="bar")

plt.title("Intuitive Accuracy Under Load")
plt.ylabel("Accuracy (%)")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig(os.path.join(graphs_dir, "intuitive_accuracy.png"))
plt.close()

# =====================================================
# GRAPH 3 — ANALYTICAL RESPONSE TIME
# =====================================================

analytical_rt = analytical.groupby("Load")["Avg_RT"].mean()

plt.figure(figsize=(8, 5))
analytical_rt.plot(kind="bar")

plt.title("Analytical Response Time")
plt.ylabel("Response Time (s)")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig(os.path.join(graphs_dir, "analytical_rt.png"))
plt.close()

# =====================================================
# GRAPH 4 — MEMORY ACCURACY
# =====================================================

memory = df[df["Memory_Accuracy"].notna()]

memory_acc = memory.groupby("Type")["Memory_Accuracy"].mean()

plt.figure(figsize=(8, 5))
memory_acc.plot(kind="bar")

plt.title("Memory Recall Accuracy")
plt.ylabel("Memory Accuracy (%)")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig(os.path.join(graphs_dir, "memory_accuracy.png"))
plt.close()

# =====================================================
# GRAPH 5 — RISK CHOICE DISTRIBUTION
# =====================================================

risk = df[df["Type"] == "risk"]

risk_a = pd.to_numeric(risk["Risk_A"], errors="coerce").fillna(0)
risk_b = pd.to_numeric(risk["Risk_B"], errors="coerce").fillna(0)

risk_grouped = pd.DataFrame({
    "A Choices": risk.groupby("Load")["Risk_A"].apply(
        lambda x: pd.to_numeric(x, errors="coerce").sum()
    ),
    "B Choices": risk.groupby("Load")["Risk_B"].apply(
        lambda x: pd.to_numeric(x, errors="coerce").sum()
    )
})

plt.figure(figsize=(8, 5))
risk_grouped.plot(kind="bar")

plt.title("Risk Choice Distribution")
plt.ylabel("Total Choices")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig(os.path.join(graphs_dir, "risk_choices.png"))
plt.close()

print("All graphs generated successfully.")