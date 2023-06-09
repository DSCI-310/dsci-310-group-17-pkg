import pytest
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sys.path.append('src/group17pkg')
from eda import plot_correlations

def test_data():
    """
    Creates a mock dataframe for testing with a subset of the data
    Parameters
    ----------
    None
    Returns
    ----------
    pd.DataFrame: A mock dataframe with a subset of the data
    """
    return pd.DataFrame({
        'age':[41,23,46,70],
        'TSH':[1.3, 4.1, 0.98, 0.16],
        'TT4':[125,102,109,175],
        'T4U':[1.14,0.91,0.87,1.3],
        'FTI':[109,120,70,141]
    })

def empty_plot():
    """
    Creates an empty plot to use for testing
    Parameters
    ----------
    None
    Returns
    ----------
    fig: An empty scatterplot
    """
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.set(font_scale=1)
    sns.heatmap(pd.DataFrame(), annot=True, ax=ax, cmap=plt.cm.Blues, vmin=0, vmax=1)
    return fig
    
def test_empty_plot():
    """
    Tests that the empty_plot() returns an empty figure
    Parameters
    ----------
    None
    Returns
    ----------
    None
    """
    fig = empty_plot()
    assert fig is not None

def test_plot_correlations_keyerror():
    """
    Tests that data has the correct columns when used as input to plot_correlations
    Parameters
    ----------
    None
    Returns
    ----------
    None if columns are correct, prints "Data must have the following columns: 
    ['age', 'TSH', 'TT4', 'T4U', 'FTI']" if column names are incorrect
    """
    try:
        result = plot_correlations(pd.DataFrame())
    except KeyError:
        print("Data must have the following columns: ['age', 'TSH', 'TT4', 'T4U', 'FTI']")

def test_plot_correlations_empty():
    """
    Tests that data is present when used as input to plot_correlations
    Parameters
    ----------
    None
    Returns
    ----------
    None if data is present in the dataframe, prints "Data frame provided has correct columns but no data. 
    Correlation cannot be made" if there is not data present in the dataframe
    """
    try:
        empty_df = pd.DataFrame(columns=['age', 'TSH', 'TT4', 'T4U', 'FTI'])
        result = plot_correlations(empty_df)
    except ValueError:
        print("Data frame provided has correct columns but no data. Correlation cannot be made")
