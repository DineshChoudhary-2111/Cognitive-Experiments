# Decision Making Under Cognitive Load Experiment

## Abstract

This project investigates how cognitive load influences human decision-making performance across intuitive reasoning, analytical reasoning, and risk-based decision tasks. A Python-based experimental system was developed to compare decision performance under normal conditions versus conditions involving working memory interference. Participants performed decision-making tasks while simultaneously maintaining digit sequences under load conditions. Experimental data was collected across multiple sessions and analyzed using decision accuracy, response time, confidence levels, risk preference patterns, and memory recall performance metrics.

---

## Objective

The objective of this experiment was to explore how cognitive load affects decision-making performance under divided attention conditions. Instead of treating decision-making as a purely isolated process, the experiment aimed to observe how working memory interference influences accuracy, response speed, confidence stability, and risk-based behavioral choices.

---

## Experimental Design

The experiment consisted of two primary conditions:

### Control Condition

Participants performed decision-making tasks (intuitive, analytical, and risk-based) without any additional cognitive load.

### Interference (Load) Condition

Participants performed the same decision-making tasks while simultaneously memorizing and later recalling a 4-digit sequence. This introduced working memory interference during decision processing.

The order of conditions and tasks was randomized across trials to reduce prediction effects and learning bias.

---

## Participants and Sessions

The experiment included:
- 3 participants
- 3 sessions per participant
- multiple randomized trials per session under both conditions

Repeated sessions were used to improve stability of behavioral trends and reduce one-time variability effects.

---

## Variables Measured

The following metrics were recorded:

- Decision Accuracy  
- Response Time  
- Confidence Levels (1–5 scale)  
- Risk Choice Distribution (A vs B)  
- Memory Recall Accuracy (load condition only)  
- Memory Recall Time  

These variables were used to evaluate how cognitive load affects both decision quality and underlying cognitive stability.

---

## Cognitive Basis

This experiment is based on working memory limitation theory and dual-task interference models in cognitive psychology. Cognitive load reduces available mental resources, forcing participants to divide attention between memory retention and decision-making processes.

The memory task required participants to actively maintain digit sequences while simultaneously performing reasoning tasks, creating a controlled interference condition that simulates real-world multitasking constraints.

An important aspect of the experiment was analyzing not just correctness, but also how response behavior, confidence, and decision stability change under cognitive strain.

---

## Results

### Decision Accuracy Comparison

![Accuracy Graph](graphs/accuracy_comparison.png)

Analytical reasoning showed a noticeable drop in accuracy under load conditions, while intuitive reasoning remained relatively stable. This suggests that structured reasoning is more sensitive to cognitive interference than heuristic-based decision-making.

---

### Response Time Comparison

![Response Time Graph](graphs/reaction_time_comparison.png)

Response times increased under load conditions across both intuitive and analytical tasks, indicating higher cognitive processing demands when working memory resources are divided.

---

### Confidence Comparison

![Confidence Graph](graphs/confidence_comparison.png)

Confidence levels showed only minor changes under load, suggesting that subjective certainty does not always directly reflect actual performance degradation.

---

### Memory Performance (Load Condition Only)

![Memory Accuracy Graph](graphs/memory_accuracy.png)

Memory recall accuracy decreased under load conditions, while recall time increased, confirming the effect of interference on working memory retention and retrieval speed.

---

### Risk Choice Distribution

![Risk Behavior Graph](graphs/risk_choice_distribution.png)

Risk-based decisions showed variability under load conditions, indicating that cognitive strain influences consistency in probabilistic decision-making.

---

## Observations and Interpretation

One of the key observations was that analytical reasoning was significantly more affected by cognitive load compared to intuitive reasoning. While participants were still able to complete tasks under interference, their response times increased and accuracy decreased in structured reasoning tasks.

Risk-based decisions showed inconsistent shifts under load, suggesting that cognitive stress can alter decision patterns even in situations with no objectively correct answer.

Memory performance clearly degraded under interference, confirming that working memory resources are shared between retention and decision-making processes.

Another important finding was that confidence levels remained relatively stable despite performance drops, indicating a disconnect between subjective certainty and actual cognitive performance under load.

---

## Limitations

Several limitations were present during the experiment:

- small participant sample size  
- limited number of sessions  
- simplified lab simulation compared to real-world cognitive load  
- absence of physiological measurements  
- controlled environment not fully reflective of natural decision contexts  

---

## Future Scope

Possible future improvements include:
- larger participant groups  
- statistical significance testing (ANOVA, t-tests)  
- adaptive memory load variation  
- integration of physiological tracking (eye tracking, EEG, heart rate)  
- machine learning models for predicting decision behavior under load  

---

## Technologies Used

- Python  
- Pandas  
- Matplotlib  
- CSV-based data logging  
- Randomized experimental design  

---

## Conclusion

This project demonstrates that cognitive load significantly influences human decision-making performance, particularly in analytical reasoning and working memory dependent tasks. While intuitive reasoning remains relatively stable, analytical performance and response time are strongly affected under load conditions.

Memory interference further amplifies cognitive strain, leading to reduced recall performance and slower retrieval. Risk-based decisions also show variability under cognitive load, suggesting that working memory limitations can influence decision consistency even in uncertain scenarios.

Overall, the experiment provides a structured computational framework for analyzing how cognitive load impacts decision-making behavior across multiple cognitive domains.