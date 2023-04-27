import sys
import getopt
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

def to_GHz(freq):
    return freq*1e9

def to_MHz(freq):
    return freq*1e6

def to_nH(ind):
    return ind*1e9

def to_pF(cap):
    return cap*1e12

def to_nF(cap):
    return cap*1e9 

def solveBPF(filter_characteristic, fcut_low, fcut_high, impedance, filter_order):
    filter_coef = pd.read_excel('Filter_Coefficients.xlsx', sheet_name=filter_characteristic)
    f_res = math.sqrt(fcut_low * fcut_high)
    coeffs = filter_coef.iloc[filter_order-1].values
    coeffs = coeffs[~np.isnan(coeffs)]

    C = np.zeros(10)
    L = np.zeros(10)

    print(coeffs)

    for i in range(1,len(coeffs)):
        coeff = coeffs[i]
        if(i%2==1):
            C[i-1] = coeff / (2*math.pi*(fcut_high-fcut_low)*impedance)
            L[i-1] = ((fcut_high-fcut_low)*impedance) / (2*math.pi*fcut_low*fcut_high*coeff)
        elif(i%2==0):
            C[i-1] = (fcut_high - fcut_low) / (2*math.pi*fcut_high*fcut_low*impedance*coeff)
            L[i-1] = (impedance*coeff) / (2 * math.pi * (fcut_high-fcut_low))

    C = C[C != 0]
    L = L[L != 0]

    print("Values for C")
    print(C)
    print("Values for L")
    print(L)


def solveLPF(filter_characteristic, fcut, impedance, filter_order):
    filter_coef = pd.read_excel('Filter_Coefficients.xlsx', sheet_name=filter_characteristic)

    coeffs = filter_coef.iloc[filter_order-1].values
    coeffs = coeffs[~np.isnan(coeffs)]

    C = np.zeros(10)
    L = np.zeros(10)

    for i in range(1, len(coeffs)):
        coeff = coeffs[i]
        C[i-1] = coeff / (2*math.pi*fcut*impedance)
        L[i-1] = (impedance * coeff) / (2*math.pi*fcut)

    C = C[C != 0]
    L = L[L != 0]
    
    print("Values for C")
    print(C)
    print("Values for L")
    print(L)


def solveHPF(filter_characteristic, fcut, impedance, filter_order):
    filter_coef = pd.read_excel('Filter_Coefficients.xlsx', sheet_name=filter_characteristic)

    coeffs = filter_coef.iloc[filter_order-1].values
    coeffs = coeffs[~np.isnan(coeffs)]

    C = np.zeros(10)
    L = np.zeros(10)

    for i in range(1, len(coeffs)):
        coeff = coeffs[i]
        L[i-1] = (impedance) / (2*math.pi*fcut*coeff)
        C[i-1] = 1/ (2*math.pi*fcut*impedance*coeff)

    C = C[C != 0]
    L = L[L != 0]
    
    print("Values for C")
    print(C)
    print("Values for L")
    print(L)

# TODO: WILL BE IMPLEMENTED
def solveBSF():
    pass


def main():

    filter_type = input('Filter Type: ')
    if(filter_type == 'BPF' or filter_type == 'BSF'):
        fcut_low = float(input('Low cutoff frequency: '))
        fcut_high = float(input('High cutoff frequency: '))
    elif(filter_type == 'LPF' or filter_type == 'HPF'):
        fcut = float(input('Cutoff frequency: '))
    else:
        print('Invalid input for filter type. Exiting the program')
        exit()

    filter_characteristic = input('Filter characteristic: ')
    impedance = float(input('Impedance: '))
    filter_order = int(input('Filter order: '))

    if(filter_type == 'BPF'):
        solveBPF(filter_characteristic, fcut_low, fcut_high, impedance, filter_order)
    elif(filter_type == 'LPF'):
        solveLPF(filter_characteristic, fcut, impedance, filter_order)
    elif(filter_type == 'HPF'):
        solveHPF(filter_characteristic, fcut, impedance, filter_order)
    elif(filter_type == 'BSF'):
        solveBSF(filter_characteristic, fcut_low, fcut_high, impedance, filter_order)
    else:
        print('Invalid input for filter type. Exiting the program')
        exit()
        
main()
