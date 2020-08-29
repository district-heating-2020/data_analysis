import matplotlib.pyplot as plt
import seaborn as sns
import ppscore as pps  # Predictive Power Score (nonlinear correlation)


def pps_heatmap(df):
    sns.set()
    fig, ax = plt.subplots()
    ax = sns.heatmap(df.reset_index(drop=True), vmin=0, vmax=1, cmap="Blues",
                     linewidths=0.5, annot=True, ax=ax)
    ax.set_title('PPS matrix')
    ax.set_xlabel('feature')
    ax.set_ylabel('target')
    return ax


def corr_heatmap(df):
    sns.set()
    ax = sns.heatmap(df, vmin=-1, vmax=1, cmap="BrBG", linewidths=0.5, annot=True)
    ax.set_title('Correlation matrix')
    return ax
