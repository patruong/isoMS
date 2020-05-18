#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 15:15:38 2020

@author: esynergetics
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


df = read_and_transform_file(file, scan)

target_ion = file.split("_")[5][0]

df[df["ion"] == target_ion]





