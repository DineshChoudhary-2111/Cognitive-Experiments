import random
import time
import csv
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def generate_sequence():
    return [random.randint(0, 20) for _ in range(4)]

def show_sequence(seq):
    print("\nMEMORIZE:")
    print(" ".join(map(str, seq)))
    time.sleep(4)
    clear()

def generate_tasks():
    tasks = []
    num_tasks = random.randint(2, 4)

    for _ in range(num_tasks):
        if random.random() < 0.5:
            a, b = random.randint(1, 30), random.randint(1, 30)
            tasks.append((f"{a} + {b}", a + b))
        else:
            a, b = random.randint(1, 30), random.randint(1, 30)
            if a < b:
                a, b = b, a
            tasks.append((f"{a} - {b}", a - b))

    return tasks

def run_interference(tasks):
    print("\nSolve quickly (10 seconds total):")

    start_time = time.time()
    correct = 0
    total = len(tasks)

    for q, ans in tasks:
        if time.time() - start_time > 10:
            print("⏱ Time up!")
            break

        try:
            user = input(f"{q} = ")
            if int(user.strip()) == ans:
                correct += 1
        except:
            pass

    return correct / total

def recall_phase(seq):
    print("\nRECALL:")
    input("Press Enter to start typing...")

    start = time.time()
    user = input("Enter sequence: ").strip().split()
    end = time.time()

    rt = round(end - start, 2)

    correct = [str(x) for x in seq]
    matches = sum(1 for i in range(min(len(user), 4)) if user[i] == correct[i])
    accuracy = matches / 4

    return accuracy, rt

def init_csv(file):
    if not os.path.exists(file):
        with open(file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "Participant",
                "Session",
                "Condition",
                "Avg Memory Accuracy (%)",
                "Avg Recall Time (s)",
                "Avg Interference Accuracy (%)"
            ])

def save_summary(file, participant, session, condition, mem_acc, rt, inter_acc):
    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            participant,
            session,
            condition,
            round(mem_acc * 100, 2),
            round(rt, 2),
            round(inter_acc * 100, 2) if inter_acc is not None else "nil"
        ])

def main():
    clear()
    print("MEMORY INTERFERENCE TEST\n")

    participant = input("Participant (A/B/C): ").strip().upper()
    session = input("Session (1/2/3): ").strip()

    filename = "memory_interference.csv"
    init_csv(filename)

    conditions = ["control"] * 4 + ["interference"] * 4
    random.shuffle(conditions)

    control_mem, control_rt = [], []
    inter_mem, inter_rt, inter_acc_all = [], [], []

    for i, cond in enumerate(conditions):
        clear()
        print(f"{participant} | Session {session}")
        print(f"TRIAL {i+1} / 8 | {cond.upper()}")

        seq = generate_sequence()
        show_sequence(seq)

        inter_acc = None

        if cond == "interference":
            tasks = generate_tasks()
            inter_acc = run_interference(tasks)

        mem_acc, rt = recall_phase(seq)

        if cond == "control":
            control_mem.append(mem_acc)
            control_rt.append(rt)
        else:
            inter_mem.append(mem_acc)
            inter_rt.append(rt)
            inter_acc_all.append(inter_acc)

        input("\nPress Enter for next trial...")

    clear()
    print("===== FINAL RESULTS =====\n")
    print(f"Participant: {participant}")
    print(f"Session: {session}\n")

    def avg(lst):
        return sum(lst)/len(lst) if lst else 0

    control_mem_avg = avg(control_mem)
    control_rt_avg = avg(control_rt)

    inter_mem_avg = avg(inter_mem)
    inter_rt_avg = avg(inter_rt)
    inter_acc_avg = avg(inter_acc_all)

    print("CONTROL:")
    print(f"Memory Accuracy: {control_mem_avg*100:.2f}%")
    print(f"Recall Time: {control_rt_avg:.2f}s\n")

    print("INTERFERENCE:")
    print(f"Memory Accuracy: {inter_mem_avg*100:.2f}%")
    print(f"Recall Time: {inter_rt_avg:.2f}s")
    print(f"Interference Accuracy: {inter_acc_avg*100:.2f}%\n")

    save_summary(filename, participant, session, "control",
                 control_mem_avg, control_rt_avg, None)

    save_summary(filename, participant, session, "interference",
                 inter_mem_avg, inter_rt_avg, inter_acc_avg)

    print("Final data saved.")

if __name__ == "__main__":
    main()