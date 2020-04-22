#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:08:27 2020

@author: esynergetics
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
    df = filter_on_amino_acids(file)
    df = df.loc[:, ["seqNum", "isoratio", "ion"]] # columns to filter on
    
    if scan_type == "MSMS":    
        df.seqNum = (df.seqNum - 1)
    
    filename = ms_files[0]
    filename_col = np.array([filename for i  in range(len(df))])
    df["filename"] = filename_col
    
    scan_type_col = np.array([scan_type for i in range(len(df))])
    df["scan_type"] = scan_type_col
    return df

# check diff between two lists
def check_difference_between_lists(list1, list2):
    return list(set(list1)-set(list2))

#if __name__ == "__main__":
folders = ["MS", "MSMS"] # Specify folder
amino_acids = ["P", "Hyp"] # Specify amino acids

ms_files = get_file_list("MS")
msms_files = ms_files = get_file_list("MSMS")    

if not check_difference_between_lists(ms_files, msms_files):
    print("Lists are same")

df = pd.DataFrame(data=None, columns = ["seqNum", "isoratio", "ion", "filename", "scan_type"])

df_ms = get_filtered_data(ms_file = ms_files[0], scan_type = "MS", amino_acids = amino_acids)
df = df.append(df_ms)
df_msms = get_filtered_data(ms_file = ms_files[0], scan_type = "MSMS", amino_acids = amino_acids)
df = df.append(df_msms)


















