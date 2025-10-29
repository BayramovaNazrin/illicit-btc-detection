# Elliptic Bitcoin Anomaly Detection

This repository investigates **illicit Bitcoin transaction detection** using the [Elliptic Dataset](https://www.kaggle.com/datasets/ellipticco/elliptic-data-set).  
The project integrates **classical machine learning**, **graph representation learning**, and **Graph Neural Networks (GNNs)** — primarily **GraphSAGE** — to classify transactions as *licit* or *illicit* within a dynamic Bitcoin network.

---

## Objective

The aim is to model Bitcoin transaction behavior as a graph and learn patterns that help:
- Detect illicit (money-laundering or ransomware-related) transactions.
- Compare classical ML baselines with GNN-based graph learning.
- Quantify which node features and temporal factors contribute most to detection.

---


## Dataset Description
| File                          | Description                                                 |
| ----------------------------- | ----------------------------------------------------------- |
| **elliptic_txs_features.csv** | 166 anonymized features per transaction node                |
| **elliptic_txs_edgelist.csv** | Directed edges between transactions                         |
| **elliptic_txs_classes.csv**  | Transaction class labels: `1=illicit`, `2=licit`, `unknown` |


---

## Models
| Category            | Model                                            | Description                                  |
| ------------------- | ------------------------------------------------ | -------------------------------------------- |
| **Classical ML**    | RandomForest, SVM, AdaBoost                      | Supervised baselines on transaction features |
| **Graph Embedding** | Node2Vec + RandomForest                          | Node embeddings + classifier                 |
| **GNN**             | GraphSAGE                                        | End-to-end graph-based node classification   |

---

## Results (GraphSAGE)
| Metric             | Value |
| ------------------ | ----- |
| Accuracy           | ~0.92 |
| F1-score (illicit) | ~0.86 |
| ROC-AUC            | ~0.94 |
| PR-AUC             | ~0.88 |

---
## Key Insights
Graph-based methods (GraphSAGE) outperform feature-based baselines.
Temporal context and neighborhood aggregation significantly improve illicit detection.
Feature importance analysis helps interpret illicit behavioral indicators

---
## Future Work
Integrate Graph Attention Networks (GAT) and Graph Transformers.
Extend to real-time Bitcoin streams for anomaly alerts.
Combine blockchain address clustering and transaction graph analytics

---
## References
**Youssef Elmougy and Ling Liu. 2023.**  
*Demystifying Fraudulent Transactions and Illicit Nodes in the Bitcoin Network for Financial Forensics.*  
In *Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD ’23)*,  
August 6–10, 2023, Long Beach, CA, USA.  
ACM, New York, NY, USA, 12 pages.  
[https://doi.org/10.1145/3580305.3599803](https://doi.org/10.1145/3580305.3599803)

### Dataset Source

This project uses the **Elliptic Bitcoin Transaction Dataset**, as analyzed in the above work.  
Dataset © Elliptic Ltd — available for academic use via [Kaggle](https://www.kaggle.com/datasets/ellipticco/elliptic-data-set).
