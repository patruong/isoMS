#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:08:27 2020

@author: ptruong
"""

import os

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# filename = "20200306_AminoAcid_Pro_1_fit.csv"
# MS_folder =  "MS"
# MS = pd.read_csv(MS_folder + "/" + filename )    
# MSMS_folder = "MSMS"
# MSMS = pd.read_csv(MSMS_folder + "/" + filename )    



def get_file_list(folder):
    """
    Gets files in folder.
    """
    folder = folder
    files = os.listdir(folder)
    res = []
    for f in files:
        if f[0] == "2":
            res.append(f)
    return res


# sålla bort onödiga aminosyror från MS - dataframe
def filter_on_amino_acids(file, amino_acids = ["P", "Hyp"]):
    """
    Function takes file name to find which amino acid is prevalent in sample
    and filters on that.
    
    file = file name
    amino_acids all amino acids in file folder that was checked for.
    """
    file = file
    amino_acids = amino_acids
    
    df = pd.read_csv(file)
    file = file.replace("Pro", "P") #Replace Pro in filenames with P.
    file_name_splitted = file.split("_")
    for amino_acid in amino_acids:
        if amino_acid in file_name_splitted:
            df_res = df[df.ion == amino_acid]
    return df_res # Might/should cause error if no matching ion!

def get_filtered_data(ms_file, scan_type = "MS", amino_acids = ["P", "Hyp"]):
    """
    Function filters the correct ion from the ms and msms files.
    
    Function also corrects the seqNum for MSMS scan so it has matching 
    seqNum to its MS counterpart.
    """
    scan_type = scan_type
    amino_acids = amino_acids
    file = scan_type + "/" + ms_file
    df = filter_on_amino_acids(file, amino_acids)
    df = df.loc[:, ["seqNum", "peak", "isoratio", "ion"]] # columns to filter on
    
    if scan_type == "MSMS":    
        df.seqNum = (df.seqNum - 1)
    
    filename = ms_file
    filename_col = np.array([filename for i  in range(len(df))])
    df["filename"] = filename_col
    
    scan_type_col = np.array([scan_type for i in range(len(df))])
    df["scan_type"] = scan_type_col
    return df

# check diff between two lists
def check_difference_between_lists(list1, list2):
    return list(set(list1)-set(list2))

def get_formatted_dataframe(amino_acids = ["P", "Hyp"]):
    """
    Function formats data so that we can work with the isoratios.
    """
    amino_acids = amino_acids # Specify amino acids
    folders = ["MS", "MSMS"] # Specify folder
    
    
    ms_files = get_file_list("MS")
    msms_files = ms_files = get_file_list("MSMS")    
    
    if not check_difference_between_lists(ms_files, msms_files):
        print("Files in MS and MSMS folders are matching!")
    else:
        print("WARNING: files in MS and MSMS folders are not same!")
    
    print("Loading and adding files...")
    df = pd.DataFrame(data=None, columns = ["seqNum", "peak", "isoratio", "ion", "filename", "scan_type"])
    for ms_type in folders:
        for file in ms_files:
            df_ms = get_filtered_data(ms_file = file, scan_type = ms_type, amino_acids = amino_acids)
            df = df.append(df_ms)
            print(ms_type + "/" + file)
    print("Done!")
    return df

#if __name__ == "__main__":

    
df = get_formatted_dataframe(amino_acids = ["P", "Hyp"])


############
# Plotting #
############

# Load plotnine.
from plotnine import *

# slice my data
z






##############################
# DOUBLE BOX PLOT FORMATTING #
##############################

df.to_csv("aminos.csv")
# Format the data to iris format

boxplot_cols = [
  "x_count", "x_mean", "x_std","x_min", "x_lower", "x_middle", "x_upper", "x_max",  
  "y_count", "y_mean", "y_std","y_min", "y_lower", "y_middle", "y_upper", "y_max",
  "category"
]

df_boxplot = pd.DataFrame(data = None, columns = boxplot_cols)

category = "setosa" # ions P, Hyp and V 

var_x = df_category["sepalLength"].describe()
var_y = df_category["sepalWidth"].describe()

df_ion = df[df.peak == "13C"]
df_MS = df_ion[df_ion.scan_type == "MS"]
df_MSMS = df_ion[df_ion.scan_type == "MSMS"]

for category in df["species"].unique():
    df_category = df[df["species"] == category]

    var_x = df_category["sepalLength"].describe()
    var_y = df_category["sepalWidth"].describe()
    data_boxplot = np.concatenate((var_x, var_y))
    data_boxplot = np.append(data_boxplot, category)
    
    df_boxplot_values = pd.DataFrame(data = [data_boxplot],
                                     columns = boxplot_cols)
    df_boxplot = df_boxplot.append(df_boxplot_values)









