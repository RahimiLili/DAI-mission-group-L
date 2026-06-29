# Predicting and Explaining Customer Churn in Telecommunications

**DAI Mission - Data & AI in Economics | TU Dortmund | Summer 2026**

Leila Rahimiyadkuri · Forough Asgari · Sara Davoodabadi

---

## Research Question

Does the type of contract a telecom customer holds (month-to-month vs. longer-term) causally increase their probability of churning and does this effect differ across distinct customer segments identified through unsupervised learning?

---

## Repository Contents

| File | Description |
|------|-------------|
| `mission.ipynb` | Final notebook - fully executed, all outputs visible |
| `requirements.txt` | Python dependencies |
| `slides.pdf` | Presentation slides |


> **Data:** The dataset is downloaded automatically inside the notebook via `kagglehub`. No manual download needed.

---

## Methods

| Block | Method |
|-------|--------|-----------|
| Causal Inference | DoWhy backdoor adjustment | 
| Supervised Learning | Logistic Regression + Random Forest | 
| Unsupervised Learning | K-Means |

---

## Setup

```bash
pip install -r requirements.txt
jupyter notebook mission.ipynb
```

> Requires a Kaggle account for the `kagglehub` download. Set up credentials at https://www.kaggle.com/settings/account

---



## Key Finding

Month-to-month contracts are the primary structural driver of churn. Moving a customer to a longer contract causally reduces their churn probability by ~13 percentage points. Cluster 1 (new customers, ~18 months tenure, 32% churn rate) is the highest-risk segment and the most effective target for contract upgrade incentives.
