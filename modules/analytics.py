import pandas as pd

def score_summary(scores_df):
    if scores_df.empty:
        return None
    return scores_df.groupby('module')['score'].mean().reset_index()
