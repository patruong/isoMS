# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

ToDo:
    - Fix get_peak_ratios

"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

filename = "20200306_AminoAcid_Pro_1_fit.csv"
MS_folder =  "MS"
MS = pd.read_csv(MS_folder + "/" + filename )    
MSMS_folder = "MSMS"
MSMS = pd.read_csv(MSMS_folder + "/" + filename )    



def get_peak_values(df, seqNum, ion):
    df = df
    seqNum = seqNum
    ion = ion
    
    # Select sequence run
    seq = df[df["seqNum"] == seqNum]
    
    # Select ion (based on file)
    ion_vals = seq[seq["ion"] == ion]
    
    # Select isotopes
    dict_peak = {}
    for i in ion_vals.peak.unique():
        isotope = ion[ion["peak"] == i]
        isotopic_peak =  isotope.I.values[0]
        dict_peak.update({isotope.peak.values[0] : isotopic_peak})
    return dict_peak


def get_peak_ratios(df, seqNum, ion):
    df = df
    seqNum = seqNum
    ion = ion
    
    # Select sequence run
    seq = df[df["seqNum"] == seqNum]
    
    # Select ion (based on file)
    ion_vals = seq[seq["ion"] == ion]
    
    # Select isotope ratioes
    dict_ratios = {}
    for i in ion_vals.peak.unique():
        isotope = ion_vals[ion_vals["peak"] == i]
        if not isotope.empty:
            dict_ratios.update({isotope.peak.values[0] : isotope.isoratio.values[0]})

    return dict_ratios


def get_all_peak_ratios(df, ion):
    df = df
    ion = ion
    dict_peak_ratios = {}
    for seqNum in df.seqNum.unique():
        peak_ratio = get_peak_ratios(df, seqNum, ion)
        dict_peak_ratios.update({seqNum : peak_ratio})
    return dict_peak_ratios

ratios_ms = get_all_peak_ratios(MS, "P")
df_ms = pd.DataFrame.from_dict(ratios_ms).T
ratios_msms = get_all_peak_ratios(MSMS, "P")
df_msms = pd.DataFrame.from_dict(ratios_msms).T    

ms = df_ms["13C"]
msms = df_msms["13C"]
plot_data = pd.DataFrame({'ms':ms.values, 'msms':msms.values})
ax = sns.scatterplot(x="ms", y="msms", data=plot_data)


import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")
ax = sns.scatterplot(x="total_bill", y="tip", data=tips)


