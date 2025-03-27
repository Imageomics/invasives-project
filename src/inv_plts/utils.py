import random

import pandas as pd

def create_random_list_of_integers(N: int, seed: int = None):
    if seed:
        random.seed(seed)
    random_list = list(range(1, N+1))
    random.shuffle(random_list)
    return random_list

def create_data_splits_from_df(df: pd.DataFrame, train_ratio=0.7, val_ratio=0.1, test_ratio=0.2):
    all_training_ratio = train_ratio + val_ratio
    assert all_training_ratio + test_ratio == 1.0, "ratios must add up to 1.0"
    num_rows = df.shape[0]
    train_df = df.sample(frac=train_ratio + val_ratio)
    test_df = df.drop(train_df.index)
    val_df = train_df.sample(frac=(val_ratio / all_training_ratio))
    train_df = train_df.drop(val_df.index)
    assert train_df.shape[0] + val_df.shape[0] + test_df.shape[0] == num_rows, "Must ensure no lost or extra rows"
    
    train_df = train_df.reset_index()
    val_df = val_df.reset_index()
    test_df = test_df.reset_index()
    
    return train_df, val_df, test_df
    