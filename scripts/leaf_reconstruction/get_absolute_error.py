import pandas as pd
import numpy as np

def mean_bias_error(y_true, y_pred):
    """
    Mean Bias Error (MBE)

    Parameters
    ----------
    y_true : array-like, shape (n_samples,)
        Ground-truth damage ratios.
    y_pred : array-like, shape (n_samples,)
        Predicted damage ratios.

    Returns
    -------
    float
        Positive  → systematic over-estimation  
        Negative  → systematic under-estimation  
        Exactly 0 → unbiased on average
    """
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    return np.mean(y_pred - y_true)

#over_rate = np.mean(estimated > ground_truth)
#under_rate = np.mean(estimated < ground_truth)


df_ground = pd.read_csv("ground_truths.csv")
df_test = pd.read_csv("result.csv")

mses = []
for i in range(len(df_test)):
    row_ground = df_ground.iloc[i]
    row_test = df_test.iloc[i]

    y_true = row_ground['proportion']
    y_pred= row_test['proportion']
    mse = abs((y_true-y_pred)*100)
    mses.append(mse)



print(np.mean(mses))
print(np.std(mses))

overestimation = np.sum(df_test['proportion'] > df_ground['proportion'])
underestimation = len(df_test['proportion']) - overestimation

import matplotlib.pyplot as plt

# Labels and values

arr = np.array(mses)
# Plot
plt.figure()
plt.hist(arr, bins=15, color='cadetblue')
plt.ylabel('Number of samples', fontsize=14)
plt.xlabel('Absolute Error', fontsize=14)
plt.xticks(fontsize=14)
plt.savefig("distr_plot_error.png",  dpi=300, bbox_inches='tight')




