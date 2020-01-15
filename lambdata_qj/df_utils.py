"""
Utility functions for working with dataframes
"""

import pandas as pd
import numpy as np
# generate random number 
TEST_DF = pd.DataFrame([1,2,3,np.nan])

def nan_finder(df):
    """
    input pandas dataframe
    output rows and cols where the nans are
    """ 
    [(i,j) for i,j in zip(*np.where(df.isnull()))]
    # to confirm nan
    # [df.iloc[i,j] for i,j in zip(*np.where(z))]
    



def uniform_random(X1=0, X2=1, n=10):
    """
    input n, X1, X2, n must be integer
    output n random numbers between X1,X2
    """
    x = np.random.uniform(X1, X2, n) 
    return x
