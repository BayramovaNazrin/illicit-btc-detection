def load_data():

    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np

    features = '/content/drive/MyDrive/anomaly_detection/elliptic_txs_features.csv'
    edges = '/content/drive/MyDrive/anomaly_detection/elliptic_txs_edgelist.csv'
    classes = '/content/drive/MyDrive/anomaly_detection/elliptic_txs_classes.csv'
    features = pd.read_csv(features, header=None)
    edges = pd.read_csv(edges)
    classes = pd.read_csv(classes, header=0)
    num_cols = features.shape[1]
    feature_cols = ['txId', 'time_step'] + [f'feature_{i}' for i in range(1, num_cols - 1)]
    features.columns = feature_cols
    classes.columns = ['txId', 'class']
    classes['class'] = classes['class'].astype(str).str.strip().replace({  'unknown': 3})

    features['txId'] = features['txId'].astype(str)
    classes['txId'] = classes['txId'].astype(str)


    merged_df = features.merge(classes, on='txId', how='left')
    merged_df['class'] = pd.to_numeric(merged_df['class'], errors='coerce')
    return features, edges, classes, merged_df
