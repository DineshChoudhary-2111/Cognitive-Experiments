import random
import time
import csv
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_for_enter(timeout):
    start = time.time()
    while time.time() - start < timeout:
        if os.name == 'nt':
            import msvcrt
            if msvcrt.kbhit():
                if msvcrt.getch() == b'\r':
                    return True, time.time() - start
        time.sleep(0.01)
    return False, None

def generate_stream(length):
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    similar = ["K", "Y", "V", "W"]

    stream = []
    targets = []

    for i in range(length):
        if random.random() < 0.25:
            stream.append("X")
            targets.append(i)
        else:
            if random.random() < 0.3:
                stream.append(random.choice(similar))
            else:
                stream.append(random.choice(letters))

    return stream, targets

def apply_distraction(char):
    symbols = "!@#$%^&*"

    # lowercase trap
    if char != "X" and random.random() < 0.2:
        char = "x"

    pattern = random.choice(["2-2", "1-1", "left", "right"])

    if pattern == "2-2":
        return f"{random.choice(symbols)}{random.choice(symbols)} {char} {random.choice(symbols)}{random.choice(symbols)}"
    elif pattern == "1-1":
        return f"{random.choice(symbols)} {char} {random.choice(symbols)}"
    elif pattern == "left":
        return f"{random.choice(symbols)}{random.choice(symbols)} {char}"
    else:
        return f"{char} {random.choice(symbols)}{random.choice(symbols)}"

def burst_noise():
    print("!@#$%^&*()_+")
    time.sleep(0.3)

def run_trial(condition):
    length = random.randint(15, 20)
    stream, targets = generate_stream(length)

    responses = []
    rts = []

    for i, char in enumerate(stream):

        display_char = char

        if condition == "distraction":
            display_char = apply_distraction(char)

            if random.random() < 0.1:
                burst_noise()

        print(display_char, end="  ", flush=True)

        start = time.time()
        pressed, _ = wait_for_enter(0.75)  # slower + realistic

        if pressed:
            rt = time.time() - start
            responses.append(i)
            rts.append(rt)

            if char == "X":
                print("✓")
            else:
                print("✗")
        else:
            print()

        time.sleep(0.15)

    return targets, responses, rts

def analyze(targets, responses, rts):
    correct = len(set(targets) & set(responses))
    missed = len(set(targets) - set(responses))
    false = len(set(responses) - set(targets))

    accuracy = correct / len(targets) if targets else 0
    precision = correct / len(responses) if responses else 0
    avg_rt = sum(rts) / len(rts) if rts else 0

    return accuracy, precision, false, avg_rt

def init_csv(file):
    if not os.path.exists(file):
        with open(file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "Participant",
                "Session",
                "Condition",
                "Accuracy (%)",
                "Precision (%)",
                "False Positives",
                "Avg RT (s)"
            ])

def save_summary(file, participant, session, condition, acc, prec, false, rt):
    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            participant,
            session,
            condition,
            round(acc * 100, 2),
            round(prec * 100, 2),
            false,
            round(rt, 2)
        ])

def main():
    clear()
    print("ATTENTION & DISTRACTION TEST\n")

    participant = input("Participant (A/B/C): ").strip().upper()
    session = input("Session (1/2/3): ").strip()

    filename = "attention_data.csv"
    init_csv(filename)

    conditions = ["control"] * 3 + ["distraction"] * 3
    random.shuffle(conditions)

    control_stats = []
    distract_stats = []

    for i, cond in enumerate(conditions):
        clear()
        print(f"{participant} | Session {session}")
        print(f"TRIAL {i+1} / 6 | {cond.upper()}")
        print("Press ENTER only when you see X\n")

        targets, responses, rts = run_trial(cond)
        acc, prec, false, avg_rt = analyze(targets, responses, rts)

        if cond == "control":
            control_stats.append((acc, prec, false, avg_rt))
        else:
            distract_stats.append((acc, prec, false, avg_rt))

        input("\nPress Enter for next trial...")

    clear()
    print("===== FINAL RESULTS =====\n")
    print(f"Participant: {participant}")
    print(f"Session: {session}\n")

    def avg(lst, idx):
        return sum(x[idx] for x in lst) / len(lst) if lst else 0

    print("CONTROL:")
    print(f"Accuracy: {avg(control_stats,0)*100:.2f}%")
    print(f"Precision: {avg(control_stats,1)*100:.2f}%")
    print(f"False Positives: {int(avg(control_stats,2))}")
    print(f"Avg RT: {avg(control_stats,3):.2f}s\n")

    print("DISTRACTION:")
    print(f"Accuracy: {avg(distract_stats,0)*100:.2f}%")
    print(f"Precision: {avg(distract_stats,1)*100:.2f}%")
    print(f"False Positives: {int(avg(distract_stats,2))}")
    print(f"Avg RT: {avg(distract_stats,3):.2f}s\n")

    save_summary(filename, participant, session, "control",
                 avg(control_stats,0), avg(control_stats,1),
                 int(avg(control_stats,2)), avg(control_stats,3))

    save_summary(filename, participant, session, "distraction",
                 avg(distract_stats,0), avg(distract_stats,1),
                 int(avg(distract_stats,2)), avg(distract_stats,3))

    print("Final data saved.")

if __name__ == "__main__":
    main()