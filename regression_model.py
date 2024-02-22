import warnings

warnings.filterwarnings("ignore")

import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import sys
sys.path.append("/")

# from data_processing import split_data

def correlation_among_numeric_features(df, cols):
    numeric_col = df[cols]
    corr = numeric_col.corr()

    corr_features = set()
    for i in range(len(corr.columns)):
        for j in range(i):
            if abs(corr.iloc[i, j]) > 0.8:
                colname = corr.columns[i]
                corr_features.add(colname)
    return corr_features


def lr_model(x_train, y_train):
    x_train_with_intercept = sm.add_constant(x_train)
    lr = sm.OlS(y_train, x_train_with_intercept).fit()
    return lr


def identify_significant_vars(lr, p_value_threshold=0.05):
    pass


if __name__ == "__main__":
    capped_data = pd.read_csv("dataset/capped.csv")
    print(capped_data.shape)

    corr_features = correlation_among_numeric_features(capped_data, capped_data.columns)
    print(corr_features)
