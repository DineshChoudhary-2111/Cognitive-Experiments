import random
import time
import os
import csv

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


intuitive_qs = [
    ("Bat and ball cost 110. Bat costs 100 more. Ball?", "5"),
    ("5 machines make 5 items in 5 min. 100 machines?", "5"),
    ("Lily pads double daily. Full in 48 days. Half?", "47"),
    ("Pen + pencil = 30. Pen costs 20 more. Pencil?", "5"),
    ("You pass 2nd place. Your position?", "2"),
    ("17 sheep, all but 9 die. Left?", "9"),
]

analytical_qs = [
    ("12 machines → 12 items in 12 min. 6 machines?", "12"),
    ("Train 60 km/hr. Distance in 30 min?", "30"),
    ("x+x+x=18. x?", "6"),
    ("3 pencils = 15. 10 pencils?", "50"),
    ("A:2 hr, B:3 hr. Together?", "1.2"),
    ("20% of 150?", "30"),
]

risk_qs = [
    ("A: 50 sure | B: 50% chance 120", None),
    ("A: 30 sure | B: 30% chance 100", None),
    ("A: 80 sure | B: 70% chance 150", None),
    ("A: 40 sure | B: 25% chance 200", None),
    ("A: 60 sure | B: 60% chance 110", None),
    ("A: 20 sure | B: 10% chance 300", None),
]

def memory_phase():
    digits = [str(random.randint(0, 9)) for _ in range(4)]

    print("\nMEMORIZE:")
    print(" ".join(digits))

    time.sleep(2)
    clear()

    return digits


def memory_recall(correct):
    start = time.time()

    ans = input("Recall sequence: ").split()

    rt = round(time.time() - start, 2)

    score = sum(
        1 for i in range(min(4, len(ans)))
        if ans[i] == correct[i]
    )

    acc = (score / 4) * 100

    return acc, rt



def avg(lst, idx):
    vals = [x[idx] for x in lst if x[idx] is not None]

    return sum(vals) / len(vals) if vals else 0



def main():

    clear()

    print("DECISION MAKING UNDER COGNITIVE LOAD\n")

    while True:
        participant = input("Participant (A/B/C): ").strip().upper()

        if participant in ["A", "B","C"]:
            break

        print("Enter valid participant (A/B/C)\n")

    random.shuffle(intuitive_qs)
    random.shuffle(analytical_qs)
    random.shuffle(risk_qs)

    intuitive_selected = intuitive_qs[:4]
    analytical_selected = analytical_qs[:4]
    risk_selected = risk_qs[:4]

    trials = []

    for i in range(4):
        trials.append(("intuitive", i < 2))
        trials.append(("analytical", i < 2))
        trials.append(("risk", i < 2))

    random.shuffle(trials)

    int_i = 0
    ana_i = 0
    risk_i = 0

    results = []


    for i, (qtype, load) in enumerate(trials):

        clear()

        print(f"{participant}")
        print(f"TRIAL {i+1}/12 | {qtype.upper()} | {'LOAD' if load else 'NO LOAD'}\n")

        if load:
            digits = memory_phase()


        if qtype == "intuitive":
            q, ans = intuitive_selected[int_i]
            int_i += 1

        elif qtype == "analytical":
            q, ans = analytical_selected[ana_i]
            ana_i += 1

        else:
            q, ans = risk_selected[risk_i]
            risk_i += 1

        print(q)

        start = time.time()

        user_ans = input("Answer: ").strip()

        rt = round(time.time() - start, 2)


        if qtype == "risk":
            correct = None
        else:
            correct = (user_ans == ans)

        while True:
            try:
                conf = int(input("Confidence (1-5): "))

                if 1 <= conf <= 5:
                    break

            except:
                pass

            print("Enter value between 1 and 5")


        mem_acc = None
        mem_rt = None

        if load:
            mem_acc, mem_rt = memory_recall(digits)


        results.append((
            qtype,
            load,
            correct,
            rt,
            conf,
            user_ans,
            mem_acc,
            mem_rt
        ))

        input("\nPress Enter...")

    clear()

    print("===== FINAL RESULTS =====\n")


    for t in ["intuitive", "analytical"]:

        for l in [True, False]:

            subset = [r for r in results if r[0] == t and r[1] == l]

            if subset:

                acc = sum(
                    1 for r in subset if r[2]
                ) / len(subset) * 100

                rt = avg(subset, 3)

                conf = avg(subset, 4)

                label = "LOAD" if l else "NO LOAD"

                print(f"{t.upper()} ({label})")
                print(f"Accuracy: {acc:.2f}%")
                print(f"Response Time: {rt:.2f}s")
                print(f"Confidence: {conf:.2f}\n")

    for l in [True, False]:

        subset = [r for r in results if r[0] == "risk" and r[1] == l]

        if subset:

            a = sum(
                1 for r in subset if r[5].upper() == "A"
            )

            b = sum(
                1 for r in subset if r[5].upper() == "B"
            )

            conf = avg(subset, 4)

            label = "LOAD" if l else "NO LOAD"

            print(f"RISK ({label})")
            print(f"A Choices: {a}")
            print(f"B Choices: {b}")
            print(f"Confidence: {conf:.2f}\n")


    mem = [r for r in results if r[6] is not None]

    if mem:

        print("MEMORY PERFORMANCE (LOAD ONLY)")
        print(f"Memory Accuracy: {avg(mem,6):.2f}%")
        print(f"Recall Time: {avg(mem,7):.2f}s\n")


    file_exists = os.path.isfile("decision_load_results.csv")

    with open("decision_load_results.csv", "a", newline="") as f:

        writer = csv.writer(f)

        if not file_exists:

            writer.writerow([
                "Participant",
                "Type",
                "Load",
                "Accuracy",
                "Avg_RT",
                "Avg_Confidence",
                "Risk_A",
                "Risk_B",
                "Memory_Accuracy",
                "Memory_RT"
            ])


        for t in ["intuitive", "analytical"]:

            for l in [True, False]:

                subset = [r for r in results if r[0] == t and r[1] == l]

                if subset:

                    acc = sum(
                        1 for r in subset if r[2]
                    ) / len(subset) * 100

                    rt = avg(subset, 3)

                    conf = avg(subset, 4)

                    mem_subset = [
                        r for r in subset if r[6] is not None
                    ]

                    mem_acc = avg(mem_subset, 6) if mem_subset else "NIL"
                    mem_rt = avg(mem_subset, 7) if mem_subset else "NIL"

                    writer.writerow([
                        participant,
                        t,
                        "LOAD" if l else "NO LOAD",
                        round(acc, 2),
                        round(rt, 2),
                        round(conf, 2),
                        "NIL",
                        "NIL",
                        mem_acc if mem_acc == "NIL" else round(mem_acc, 2),
                        mem_rt if mem_rt == "NIL" else round(mem_rt, 2)
                    ])


        for l in [True, False]:

            subset = [r for r in results if r[0] == "risk" and r[1] == l]

            if subset:

                a = sum(
                    1 for r in subset if r[5].upper() == "A"
                )

                b = sum(
                    1 for r in subset if r[5].upper() == "B"
                )

                conf = avg(subset, 4)

                mem_subset = [
                    r for r in subset if r[6] is not None
                ]

                mem_acc = avg(mem_subset, 6) if mem_subset else "NIL"
                mem_rt = avg(mem_subset, 7) if mem_subset else "NIL"

                writer.writerow([
                    participant,
                    "risk",
                    "LOAD" if l else "NO LOAD",
                    "NIL",
                    "NIL",
                    round(conf, 2),
                    a,
                    b,
                    mem_acc if mem_acc == "NIL" else round(mem_acc, 2),
                    mem_rt if mem_rt == "NIL" else round(mem_rt, 2)
                ])

    print("Session complete.")
    print("CSV saved as: decision_load_results.csv")


if __name__ == "__main__":
    main()