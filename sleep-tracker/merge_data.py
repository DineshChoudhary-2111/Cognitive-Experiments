import pandas as pd
import os

if not os.path.exists("sleep_data.csv"):
    print("Missing sleep_data.csv (run tracker first)")
    exit()

if not os.path.exists("reaction_data.csv"):
    print("Missing reaction_data.csv")
    exit()

if not os.path.exists("memory_data.csv"):
    print("Missing memory_data.csv (run memory task first)")
    exit()

sleep = pd.read_csv("sleep_data.csv")
reaction = pd.read_csv("reaction_data.csv")
memory = pd.read_csv("memory_data.csv")

sleep.columns = sleep.columns.str.strip()
reaction.columns = reaction.columns.str.strip()
memory.columns = memory.columns.str.strip()

reaction["Reaction Time Avg"] = pd.to_numeric(reaction["Reaction Time Avg"], errors="coerce")
memory["Memory Score"] = pd.to_numeric(memory["Memory Score"], errors="coerce")

sleep["Sleep Hours"] = pd.to_numeric(sleep["Sleep Hours"], errors="coerce")
sleep["Sleep Quality"] = pd.to_numeric(sleep["Sleep Quality"], errors="coerce")

reaction_avg = reaction.groupby("Date", as_index=False).mean()
memory_avg = memory.groupby("Date", as_index=False).mean()

merged = pd.merge(sleep, reaction_avg, on="Date", how="inner")
merged = pd.merge(merged, memory_avg, on="Date", how="inner")

merged.to_csv("final_data.csv", index=False)

print("\nMERGE COMPLETE")
print(merged)