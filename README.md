# Elliptic Bitcoin Anomaly Detection

This repository investigates **illicit Bitcoin transaction detection** using the [Elliptic Dataset](https://www.kaggle.com/datasets/ellipticco/elliptic-data-set).  
The project combines **classical machine learning**, **graph representation learning**, and **Graph Neural Networks (GNNs)** — primarily **GraphSAGE** — to classify transactions as *licit* or *illicit* within a dynamic Bitcoin network.

---

##  Objective

The goal is to model Bitcoin transaction behavior as a graph and learn structural and temporal patterns that:
- Detect illicit (money-laundering or ransomware-related) transactions.
- Compare traditional ML baselines with graph-based learning methods.
- Identify which node features and temporal contexts contribute most to anomaly detection.

---

##  Dataset Description

| File | Description |
|------|--------------|
| **elliptic_txs_features.csv** | 166 anonymized features per transaction node |
| **elliptic_txs_edgelist.csv** | Directed edges representing transaction links |
| **elliptic_txs_classes.csv**  | Transaction labels: `1=illicit`, `2=licit`, `unknown` |

---

##  Models

| Category | Model | Description |
|-----------|--------|-------------|
| **Classical ML** | RandomForest, SVM, AdaBoost | Supervised baselines using tabular features |
| **Graph Embedding** | Node2Vec + RandomForest | Node2Vec embeddings combined with classifier |
| **GNN** | GraphSAGE | End-to-end graph neural network for node classification |

---

##  Results (GraphSAGE)

| Metric | Value |
|--------|--------|
| Accuracy | ~0.92 |
| F1-score (illicit) | ~0.86 |
| ROC-AUC | ~0.94 |
| PR-AUC | ~0.88 |

---

##  Key Insights

- Graph-based learning (GraphSAGE) significantly outperforms feature-only baselines.  
- Temporal and neighborhood information enhance illicit node detection.  
- Permutation importance aids interpretability of contributing features.

---

##  Future Work

- Explore **Graph Attention Networks (GAT)** and **Graph Transformers**.  
- Extend to real-time detection on streaming Bitcoin data.  
- Combine blockchain address clustering and dynamic transaction graph analytics.

---

##  References

**Youssef Elmougy and Ling Liu. 2023.**  
*Demystifying Fraudulent Transactions and Illicit Nodes in the Bitcoin Network for Financial Forensics.*  
In *Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD ’23)*,  
August 6–10, 2023, Long Beach, CA, USA.  
ACM, New York, NY, USA, 12 pages.  
[https://doi.org/10.1145/3580305.3599803](https://doi.org/10.1145/3580305.3599803)

### Dataset Source

This project uses the **Elliptic Bitcoin Transaction Dataset**, as analyzed in the above work.  
Dataset © Elliptic Ltd — available for academic use via [Kaggle](https://www.kaggle.com/datasets/ellipticco/elliptic-data-set).
