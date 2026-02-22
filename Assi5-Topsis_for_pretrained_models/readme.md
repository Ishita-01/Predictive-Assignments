# TOPSIS for Selecting Best Pre-trained Text Conversational NLP Model

## Overview
This project applies the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** multi-criteria decision-making method to identify the best pre-trained **conversational (dialogue) NLP model** among popular transformer-based models.

Conversational AI models must balance response quality, coherence, and computational efficiency. TOPSIS provides a structured and quantitative approach to rank these models by considering both benefit and cost criteria.

---

## Objective
To select the optimal pre-trained conversational model using TOPSIS based on multiple evaluation metrics.

---

## Models Evaluated
The following conversational models were considered in this study:

- DialoGPT-Medium  
- BlenderBot-400M  
- GPT-2 Medium  
- T5-Base (Chat-fine-tuned)

---

## Evaluation Criteria

| Criterion | Description | Type |
|----------|-------------|------|
| Response Quality | Human evaluation score (out of 5) | Benefit |
| Coherence | Logical consistency and relevance of responses | Benefit |
| Inference Time (ms) | Average response generation time | Cost |
| Model Size (MB) | Storage requirement of the model | Cost |

---

## Weights Assigned

| Criterion | Weight |
|----------|--------|
| Response Quality | 0.35 |
| Coherence | 0.30 |
| Inference Time | 0.20 |
| Model Size | 0.15 |

---

## Methodology
The TOPSIS method was applied using the following steps:

1. Construct the decision matrix using model performance metrics  
2. Normalize the decision matrix  
3. Apply weights to the normalized matrix  
4. Determine ideal best and ideal worst solutions  
5. Calculate Euclidean distances from ideal solutions  
6. Compute TOPSIS scores  
7. Rank models based on TOPSIS scores  

---

## Results
<img width="1099" height="173" alt="image" src="https://github.com/user-attachments/assets/f057b558-0cd9-4c7b-b14a-6f7a6a09d82c" />
**Best Conversational Model Identified:** **T5-Base (Chat)**


---

## Visualization
A bar graph is generated to visualize and compare the TOPSIS scores of all conversational models.
<img width="759" height="653" alt="image" src="https://github.com/user-attachments/assets/4f78fad3-37fa-42e8-b7b7-9b9198dde967" />


---

## Conclusion

This project demonstrates that TOPSIS is an effective multi-criteria decision-making technique for selecting the best pre-trained conversational NLP model by jointly considering performance quality and computational efficiency. The methodology can be extended to other NLP tasks such as text summarization, text generation, classification, and semantic similarity
