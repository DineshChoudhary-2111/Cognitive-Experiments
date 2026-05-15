# Decision Making Under Cognitive Load

## Objective

This experiment was designed to study how cognitive load influences human decision-making, reasoning accuracy, confidence, and response behaviour.

The project specifically investigated whether holding information in working memory affects:
- intuitive reasoning,
- analytical reasoning,
- risk-based choices,
- response speed,
- and self-confidence during decision making.

---

## Background

Human cognition relies heavily on limited working memory resources.  
When the brain is occupied with retaining information, decision quality and reasoning efficiency may change.

This experiment explores the relationship between:
- memory load,
- cognitive processing,
- and behavioural decision outcomes.

The project combines concepts from:
- cognitive psychology,
- behavioural economics,
- and human-computer interaction.

---

## Experimental Design

Participants completed three categories of decision tasks:

### 1. Intuitive Reasoning
Questions designed to trigger fast, instinctive responses.

Example:
> “You pass the person in 2nd place. What position are you now?”

---

### 2. Analytical Reasoning
Questions requiring deliberate logical calculation.

Example:
> “20% of 150?”

---

### 3. Risk-Based Decisions
Participants selected between:
- a guaranteed reward (Option A),
- or a probabilistic reward (Option B).

Example:
> “A: 50 sure | B: 50% chance 120”

---

## Cognitive Load Mechanism

During LOAD trials:
- participants first memorized a 4-digit sequence,
- completed the reasoning task,
- then recalled the sequence afterward.

During NO LOAD trials:
- participants solved questions directly without memory interference.

This structure allowed comparison between:
- normal reasoning,
- and reasoning under working-memory pressure.

---

## Variables Measured

The experiment recorded:

- Decision accuracy
- Response time
- Confidence rating (1–5)
- Risk preference behaviour
- Memory recall accuracy
- Memory recall time

---

## Technologies Used

- Python
- CSV data logging
- Randomized trial sequencing
- Automated behavioural analysis

---

## Experimental Logic

Several mechanisms were intentionally designed to improve validity:

- Trial order was randomized to reduce predictability.
- Question categories were shuffled across sessions.
- Load and no-load conditions were intermixed to reduce adaptation effects.
- Confidence scoring was included to compare subjective certainty with actual performance.
- Memory recall was measured independently to verify cognitive load effectiveness.

---

## Results Summary

### Observed Trends

The collected data showed several consistent behavioural patterns:

- Analytical reasoning performance generally declined under memory load.
- Response times increased during cognitively demanding tasks.
- Intuitive questions were less affected by load compared to analytical questions.
- Participants often maintained high confidence even when analytical accuracy decreased.
- Risk preferences shifted inconsistently between participants, suggesting individual behavioural variation.
- Memory recall accuracy strongly influenced overall task performance.

---

## Cognitive Interpretation

The findings support the idea that:
- working memory resources are limited,
- and analytical reasoning depends more heavily on those resources than intuitive reasoning.

The experiment also demonstrates that:
- confidence does not always correlate with correctness,
- especially under increased cognitive pressure.

This aligns with established theories in:
- dual-process cognition,
- cognitive load theory,
- and bounded rationality.

---

## Graphical Analysis

Graphs generated from the dataset include:

- Accuracy comparison under LOAD vs NO LOAD
- Response time analysis
- Confidence level comparison
- Memory performance graphs
- Risk choice distribution graphs

These visualizations help identify behavioural trends across participants and conditions.

---

## Files Included

### Main Program
- `decision_memoryload.py`

### Dataset
- `decision_load_results.csv`

### Graph Generation
- `graphs.py`

### Graph Outputs
Stored inside:
- `/graphs`

---

## Future Improvements

Possible extensions of this project include:

- larger participant samples,
- adaptive cognitive load difficulty,
- statistical significance testing,
- eye-tracking integration,
- physiological stress monitoring,
- and machine learning analysis of behavioural patterns.

---

## Conclusion

This experiment demonstrates how cognitive load can influence:
- reasoning accuracy,
- response behaviour,
- confidence,
- and decision strategies.

The project highlights the relationship between memory pressure and higher-order thinking, while also showing measurable differences between intuitive and analytical cognition.

The results reinforce the idea that human decision making is not purely logical, but strongly shaped by cognitive limitations and mental workload.