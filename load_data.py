def load_data():
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np

    # --- Paths ---
    features_path = '/content/drive/MyDrive/anomaly_detection/elliptic_txs_features.csv'
    edges_path = '/content/drive/MyDrive/anomaly_detection/elliptic_txs_edgelist.csv'
    classes_path = '/content/drive/MyDrive/anomaly_detection/elliptic_txs_classes.csv'

    # --- Load features and edges ---
    features = pd.read_csv(features_path, header=None)
    edges = pd.read_csv(edges_path)
    classes = pd.read_csv(classes_path, names=['txId', 'class'], skiprows=1)

    # Remove rows that break integer conversion
    classes = classes[classes['class'].notna()]                
    classes = classes[classes['class'].astype(str).str.lower() != 'class']  
    classes = classes[classes['class'] != 'unknown']            

    # Convert to int
    classes['class'] = classes['class'].astype(int)

    # Rename feature columns
    num_cols = features.shape[1]
    feature_cols = ['txId', 'time_step'] + [f'feature_{i}' for i in range(1, num_cols - 1)]
    features.columns = feature_cols

    # Ensure IDs are comparable as strings
    features['txId'] = features['txId'].astype(str)
    classes['txId'] = classes['txId'].astype(str)

    # Merge
    merged_df = features.merge(classes, on='txId', how='left')
    merged_df['class'] = pd.to_numeric(merged_df['class'], errors='coerce')

    return features, edges, classes, merged_df
