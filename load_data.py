def load_data():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Paths
    features_path = '/content/drive/MyDrive/anomaly_detection/elliptic_txs_features.csv'
    edges_path = '/content/drive/MyDrive/anomaly_detection/elliptic_txs_edgelist.csv'
    classes_path = '/content/drive/MyDrive/anomaly_detection/elliptic_txs_classes.csv'

    # Load features 
    features = pd.read_csv(features_path, header=None)
    num_cols = features.shape[1]
    feature_cols = ['txId', 'time_step'] + [f'feature_{i}' for i in range(1, num_cols - 1)]
    features.columns = feature_cols

    # Load edges
    edges = pd.read_csv(edges_path)
    edges.columns = ['txId1', 'txId2']

    # Load classes 
    classes = pd.read_csv(classes_path)
    classes = classes[classes['class'].notna()]                
    classes = classes[classes['class'] != 'unknown']           
    classes['class'] = classes['class'].astype(int)            

    # Convert IDs to consistent string format 
    features['txId'] = features['txId'].astype(str)
    classes['txId'] = classes['txId'].astype(str)
    edges['txId1'] = edges['txId1'].astype(str)
    edges['txId2'] = edges['txId2'].astype(str)

    # Merge for optional analysis 
    merged_df = features.merge(classes, on='txId', how='left')
    merged_df['class'] = pd.to_numeric(merged_df['class'], errors='coerce')

    return features, edges, classes, merged_df
