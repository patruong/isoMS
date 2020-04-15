# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

ToDo:
    - Fix get_peak_ratios

"""

import pandas as pd

folder =  "MS"
filename = "20200306_AminoAcid_Pro_1_fit.csv"
df = pd.read_csv(folder + "/" + filename )    


def get_peak_values(df, seqNum, ion):
    df = df
    seqNum = seqNum
    ion = ion
    
    # Select sequence run
    seq = df[df["seqNum"] == seqNum]
    
    # Select ion (based on file)
    ion = seq[seq["ion"] == ion]
    
    # Select isotopes
    dict_peak = {}
    for i in ion.peak.unique():
        isotope = ion[ion["peak"] == i]
        isotopic_peak =  isotope.mu.values[0]
        dict_peak.update({isotope.peak.values[0] : isotopic_peak})
    return dict_peak


def get_peak_ratios(df, seqNum, ion):
    df = df
    seqNum = seqNum
    ion = ion
    
    # Select sequence run
    seq = df[df["seqNum"] == seqNum]
    
    # Select ion (based on file)
    ion = seq[seq["ion"] == ion]
    
    # Select isotopes
    dict_peak = {}
    for i in ion.peak.unique():
        isotope = ion[ion["peak"] == i]
        isotopic_peak =  isotope.mu.values[0]
        dict_peak.update({isotope.peak.values[0] : isotopic_peak})
    return dict_peak

"""   
def get_peak_ratios(df, seqNum, ion):
    df = df
    seqNum = seqNum
    ion = ion

    # Select sequence run
    seq = df[df["seqNum"] == seqNum]
    
    # Select ion (based on file)
    ion = seq[seq["ion"] == ion]
    
    # Select isotopes
    monoisotopic = ion[ion["peak"] == "0"]
    C = ion[ion["peak"] == "13C"]
    N = ion[ion["peak"] == "15N"]
    H = ion[ion["peak"] == "2H"]
    O = ion[ion["peak"] == "18O"]
    
    # Select mass of peaks
    
    monoisotopic_peak = monoisotopic.mu.values[0]
    monoisotopic_peak_ratio = monoisotopic_peak/monoisotopic_peak
    C_peak_ratio = C.mu .values[0]/monoisotopic_peak
    N_peak_ratio = N.mu.values[0]/monoisotopic_peak
    H_peak_ratio = H.mu.values[0]/monoisotopic_peak
    O_peak_ratio = O.mu.values[0]/monoisotopic_peak
    
    peak_dict_ratio = {
        "monoisotopic":monoisotopic_peak_ratio,
        "13C":C_peak_ratio,
        "15N":N_peak_ratio,
        "2H":H_peak_ratio,
        "18O":O_peak_ratio,
        }
    
    return peak_dict_ratio
"""

seq = df[df.seqNum == 5]
ion = seq[seq.ion == "P"]


monoisotopic = ion[ion["peak"] == "0"]
C = ion[ion["peak"] == "13C"]
N = ion[ion["peak"] == "15N"]
H = ion[ion["peak"] == "2H"]
O = ion[ion["peak"] == "18O"]

if monoisotopic.empty = 
monoisotopic_peak = monoisotopic.mu.values[0]
C_peak = C.mu .values[0]
N_peak = N.mu.values[0]
H_peak = H.mu.values[0]
O_peak = O.mu.values[0]


for seqNum in df.seqNum.unique():
    peak_ratios = get_peak_values(df, seqNum, "P")
    
peaks = get_peak_values(df, 1, "P")
peak_ratios = get_peak_ratios(df, 1, "P")

#apply(get_peak_ratios(1, "P", "MS","20200306_AminoAcid_Pro_1_fit.csv"))











