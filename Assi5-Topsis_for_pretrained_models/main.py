import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Model": [
        "DialoGPT-Medium",
        "BlenderBot-400M",
        "GPT-2 Medium",
        "T5-Base (Chat)"
    ],
    "Response_Quality": [4.2, 4.5, 3.9, 4.1],   
    "Coherence": [4.1, 4.6, 3.8, 4.0],          
    "Inference_Time": [90, 140, 110, 85],      
    "Model_Size": [345, 450, 355, 220]         
}

df = pd.DataFrame(data)

criteria_matrix = df.iloc[:, 1:].values
normalized = criteria_matrix / np.sqrt((criteria_matrix ** 2).sum(axis=0))

weights = np.array([0.35, 0.30, 0.20, 0.15])
weighted_matrix = normalized * weights

ideal_best = np.array([
    weighted_matrix[:, 0].max(),
    weighted_matrix[:, 1].max(),
    weighted_matrix[:, 2].min(),
    weighted_matrix[:, 3].min()
])

ideal_worst = np.array([
    weighted_matrix[:, 0].min(),
    weighted_matrix[:, 1].min(),
    weighted_matrix[:, 2].max(),
    weighted_matrix[:, 3].max()
])

distance_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
distance_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

topsis_score = distance_worst / (distance_best + distance_worst)

df["TOPSIS_Score"] = topsis_score
df["Rank"] = df["TOPSIS_Score"].rank(ascending=False)

print("\nFinal TOPSIS Result:\n", df.sort_values("Rank"))

plt.figure()
plt.bar(df["Model"], df["TOPSIS_Score"])
plt.xlabel("Model")
plt.ylabel("TOPSIS Score")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()