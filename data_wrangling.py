#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:14:50 2020

@author: ptruong
"""


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def get_formatted_dataframe(df):
    df_new = df.loc[:, ["seqNum", "peak", "isoratio", "ion", "file", "scan", "n"]]
    df_new.isoratio = df_new.isoratio / df_new.n
    df_new.drop("n", axis = 1, inplace = True)
    return df_new


def transform_df_boxplot(df, peak, x = "MS", y = "MSMS_HCD_125"):
    """
    Takes input from get_formatted_dataframe and gives df_boxplot output format.
    
    peak - the peak from "peak" column of get_formatted_dataframe. We plot boxplots for each peak.
        x - one scan type (x-axis)
        y - second scan type (y-axis)
    """
    print("NOTE TO SELF: Check if data is empty - future version need error handler!")
    boxplot_cols = [
      "x_count", "x_mean", "x_std","x_min", "x_lower", "x_middle", "x_upper", "x_max",  
      "y_count", "y_mean", "y_std","y_min", "y_lower", "y_middle", "y_upper", "y_max",
      "category"
    ]
    
    df_boxplot = pd.DataFrame(data = None, columns = boxplot_cols)
    
    for category in df["ion"].unique():
        df_category = df[df["ion"] == category]
        df_category = df_category[df_category["peak"] == peak]
        
        var_x = df_category[df_category["scan"] == x].isoratio.describe()
        var_y = df_category[df_category["scan"] == y].isoratio.describe()
        
        data_boxplot = np.concatenate((var_x, var_y))
        data_boxplot = np.append(data_boxplot, category)
    
        df_boxplot_values = pd.DataFrame(data = [data_boxplot],
                                         columns = boxplot_cols)
        df_boxplot = df_boxplot.append(df_boxplot_values)
    return df_boxplot


df = pd.read_csv("tSIM experiment.csv")

df_formatted = get_formatted_dataframe(df)


x_lab = "MS"
y_lab = "MSMS_HCD_125"
iso = "13C"

for i in df_formatted.peak.unique(): 
    if i != "0":
        iso = i
        df_boxplot = transform_df_boxplot(df_formatted, 
                                          peak = iso,
                                          x = x_lab,
                                          y = y_lab)        
        df_boxplot.to_csv("results/" + iso + "__" + x_lab + "__" + y_lab + ".csv", sep = ";", index = False)








