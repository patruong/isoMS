#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 15:15:38 2020

@author: ptruong

File should used on folder with scan folders...
"""

import pandas as pd
import numpy as np


file = "20200402_HCD0_HCD50_60K_AGC5e4_Val_1_at125_tSIM_fit.csv"
scan = "MS"

def read_and_transform_file(file, scan):
    file = file
    scan = scan
    df = pd.read_csv(file)
    df_vals = df.loc[:,['seqNum', 'peak', 'isoratio', 'ion']]
    
    scan = np.array([scan for i in range(len(df))])
    file = np.array([file for i in range(len(df))])
    
    df_vals["scan"] = scan
    df_vals["file"] = file
    return df_vals


def filter_df_on_relevant_ion(file, scan):
    df = read_and_transform_file(file, scan)
    target_ion = file.split("/")[1].split("_")[5][0]
    print(target_ion)
    df_filtered = df[df["ion"] == target_ion]
    return df_filtered

df = read_and_transform_file(file, scan)
df = filter_df_on_relevant_ion(df)


import os

scans = os.listdir()

df  =
for scan in scans:
    files = os.listdir(scan)
    for file in files:
        file_dir = (scan + "/" + file)
        print(file_dir)
        df = filter_df_on_relevant_ion(file_dir, file_dir.split("/")[0])
        df = df.append(df)
        print(len(df))



test1 = "MS/20200402_HCD0_HCD50_60K_AGC5e4_Hyp_1_at125_tSIM_fit.csv"
test2 = "MS/20200402_HCD0_HCD50_60K_AGC5e4_Pro_3_at125_tSIM_fit.csv"


df1 = filter_df_on_relevant_ion(test1, test1.split("/")[0])

df2 = filter_df_on_relevant_ion(test2, test2.split("/")[0])

df_t = df1.append(df2)
d

df = df1








