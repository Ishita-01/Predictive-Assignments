# Learning PDF Using GAN

## Methodology
**Pipeline**: Data Collection → Data Pre-processing → Non-Linear Transformation → GAN Training → Sample Generation → PDF Approximation → Result Analysis

This assignment focuses on learning an unknown probability density function directly from data samples using Generative Adversarial Networks without assuming any parametric form.

---

## Dataset
- India Air Quality Dataset (Kaggle)
- Dataset Link: https://www.kaggle.com/datasets/shrutibhargava94/india-air-quality-data
- Feature used: NO₂ concentration (`x`)

---
## Objective
The objective of this assignment is to learn an unknown probability density function of a transformed random variable using only data samples. No analytical or parametric form of the probability density function is assumed. A Generative Adversarial Network (GAN) is used to implicitly learn the distribution directly from the data.

---

## Mathematical Formulation
# Non-Linear Transformation
Each NO₂ value x is transformed into z using the roll-number-parameterized non-linear function:
```
z = x + aᵣ sin(bᵣ x)
```
where:

- aᵣ = 0.5 × (r mod 7)
- bᵣ = 0.3 × (r mod 5 + 1)
- r is the university roll number

# Transformation Parameters
For the given university roll number:

- r = 102317254
- aᵣ = 0.5 × (r mod 7) = 0.5 × (102317254 mod 7) = 0.5 × 4 = 2.0
- bᵣ = 0.3 × ((r mod 5) + 1) = 0.3 × ((102317254 mod 5) + 1) = 0.3 × (4 + 1) = 1.5

In the code, these are represented as:

- **ar = 2.0**
- **br = 1.5**
---

## GAN Architecture

### Generator
- Input: Gaussian noise N(0,1)
- Layers: 1 → 32 → 32 → 1
- Activations: ReLU

### Discriminator
- Input: Sample (real or fake)
- Layers: 1 → 32 → 32 → 1
- Activations: LeakyReLU, Sigmoid

Training uses Binary Cross Entropy loss and Adam optimizer.

---
## . Training Details
- Optimizer: Adam optimizer for both networks ($lr = 0.0002$)
- Loss Function: Binary 
- Cross Entropy Loss (BCELoss)
- Epochs: 5,000.Batch Size: 128.

---
## PDF Estimation
After training the GAN:
- Samples are generated from the Generator
- PDF is estimated using:
  - Histogram Density Estimation
  - Kernel Density Estimation (KDE)

---

## Observations

### Mode Coverage
- Major modes of the real distribution are captured.
- Minor deviations occur in low-density regions.

### Training Stability
- GAN training remains stable.
- No significant mode collapse observed.

### Quality of Generated Distribution
- Generated samples closely match the real data distribution.
- KDE and histogram plots show good overlap.

<img width="1062" height="678" alt="image" src="https://github.com/user-attachments/assets/50c8c5a0-fa59-4184-aaaa-7039d5b47955" />


---

## Conclusion
The GAN successfully learns the unknown probability density function of the transformed variable using data only, without assuming any parametric form.



