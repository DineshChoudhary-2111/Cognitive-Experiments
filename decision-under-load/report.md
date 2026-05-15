# Decision Making Under Cognitive Load

## Abstract

This experiment investigates how cognitive load influences human decision-making, analytical reasoning, confidence, and risk preference. Participants completed intuitive, analytical, and risk-based decision tasks under both normal and memory-load conditions. The study aimed to observe whether simultaneous memory demands reduce reasoning efficiency and alter behavioral choices.

---

## Objective

To study the effect of cognitive load on:

- Decision accuracy
- Analytical reasoning performance
- Response time
- Confidence levels
- Risk preference
- Working memory performance

---

## Experimental Design

Participants completed three categories of tasks:

1. **Intuitive Questions**
   - Fast-response cognitive reflection style problems.

2. **Analytical Questions**
   - Calculation and reasoning-based problems requiring deliberate thinking.

3. **Risk-Based Decisions**
   - Choice between safe and probabilistic reward options.

Each category was tested under:

- **NO LOAD** condition
- **LOAD** condition

During load trials, participants first memorized a 4-digit sequence and later recalled it after answering the question.

---

## Cognitive Load Mechanism

The memory-load condition was designed to simulate divided attention and working-memory stress.

Participants:

1. Memorized a random 4-digit sequence.
2. Solved a reasoning or risk question.
3. Recalled the original sequence.

This created interference between memory maintenance and decision processing.

---

## Variables Measured

### Primary Variables

- Decision Accuracy
- Response Time
- Confidence Rating (1–5)

### Secondary Variables

- Memory Recall Accuracy
- Memory Recall Time
- Risk Preference Distribution

---

## Methodology

- 3 participants completed multiple randomized trials.
- Question order and load conditions were shuffled to reduce prediction bias.
- All responses were logged automatically using CSV storage.
- Results were analyzed using Python-based statistical visualization.

---

## Technologies Used

- Python
- CSV Data Logging
- Matplotlib
- Pandas

---

## Key Observations

### 1. Analytical Performance Declined Under Load

Analytical tasks showed the strongest reduction in accuracy during memory-load conditions. Participants generally took longer to respond and produced more incorrect answers while simultaneously maintaining digit sequences.

### 2. Intuitive Tasks Were More Resistant

Intuitive reasoning tasks were less affected by cognitive load. Some participants maintained high accuracy even while performing memory recall simultaneously.

### 3. Response Time Increased Under Cognitive Stress

Load conditions generally increased response time, especially for analytical tasks, suggesting greater mental processing demand.

### 4. Confidence Remained High Despite Errors

Several participants maintained high confidence ratings even when analytical accuracy dropped, indicating possible overconfidence under cognitive stress.

### 5. Risk Preferences Shifted Between Conditions

Risk-choice distributions changed between load and no-load conditions for some participants, suggesting that cognitive burden may influence decision strategy.

---

## Graphical Analysis

### Analytical Accuracy Comparison

![Analytical Accuracy](graphs/analytical_accuracy.png)

### Intuitive Accuracy Comparison

![Intuitive Accuracy](graphs/intuitive_accuracy.png)

### Response Time Comparison

![Response Time](graphs/response_time.png)

### Confidence Level Comparison

![Confidence Levels](graphs/confidence_levels.png)

### Risk Preference Distribution

![Risk Preference](graphs/risk_distribution.png)

---

## Interpretation

The experiment demonstrates that cognitive load disproportionately affects tasks requiring structured reasoning and working-memory coordination. Analytical thinking appears more vulnerable to interference than intuitive pattern-based responses.

The findings align with cognitive psychology theories suggesting that working memory is a limited resource shared between reasoning and memory maintenance.

---

## Limitations

- Small participant pool
- Limited trial count
- Manual keyboard input variability
- Simplified risk scenarios

---

## Future Scope

Possible future improvements include:

- Larger participant datasets
- Statistical significance testing
- Adaptive difficulty systems
- Eye-tracking integration
- EEG or physiological stress monitoring
- Real-time cognitive load estimation

---

## Repository Structure

```text
decision-making-load/
│
├── decision_memoryload.py
├── decision_load_results.csv
├── graphs.py
├── report.md
│
├── graphs/
│   ├── analytical_accuracy.png
│   ├── intuitive_accuracy.png
│   ├── response_time.png
│   ├── confidence_levels.png
│   └── risk_distribution.png