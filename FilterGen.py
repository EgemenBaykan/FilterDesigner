import pandas as pd
import numpy as np
import math

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

class Filter:
    def __init__(self, filter_type, filter_order, filter_characteristic, impedance):
        self.filter_type = filter_type
        self.filter_characteristic = filter_characteristic
        self.filter_order = filter_order
        self.impedance = impedance
        self.fcut = 0
        self.fcut_low = 0
        self.fcut_high = 0

        filter_coef = pd.read_excel('Filter_Coefficients.xlsx', sheet_name=self.filter_characteristic)
        self.coeffs = filter_coef.iloc[filter_order-1].values
        self.coeffs = self.coeffs[~np.isnan(self.coeffs)]

        self.C = np.zeros(10)
        self.L = np.zeros(10)


    def __str__(self):
        pass

    def solve(self):
        if(self.filter_type == 'LPF'):
            for i in range(1, len(self.coeffs)):
                coeff = self.coeffs[i]
                self.C[i-1] = coeff / (2*math.pi*self.fcut*self.impedance)
                self.L[i-1] = (self.impedance * coeff) / (2*math.pi*self.fcut)
        elif(self.filter_type == 'HPF'):
            for i in range(1, len(self.coeffs)):
                coeff = self.coeffs[i]
                self.L[i-1] = (self.impedance) / (2*math.pi*self.fcut*coeff)
                self.C[i-1] = 1/ (2*math.pi*self.fcut*self.impedance*coeff)
        elif(self.filter_type == 'BPF'):
            for i in range(1,len(self.coeffs)):
                coeff = self.coeffs[i]
                if(i%2==1):
                    self.C[i-1] = coeff / (2*math.pi*(self.fcut_high-self.fcut_low)*self.impedance)
                    self.L[i-1] = ((self.fcut_high-self.fcut_low)*self.impedance) / (2*math.pi*self.fcut_low*self.fcut_high*coeff)
                elif(i%2==0):
                    self.C[i-1] = (self.fcut_high - self.fcut_low) / (2*math.pi*self.fcut_high*self.fcut_low*self.impedance*coeff)
                    self.L[i-1] = (self.impedance*coeff) / (2 * math.pi * (self.fcut_high-self.fcut_low))
        elif(self.filter_type == 'BSF'):
            print('Band stop filters are not implemented yet. Exiting the program.')
            exit()
        else:
            print('Invalid filter type. Exiting the program')
            exit()

        self.C = self.C[self.C != 0]
        self.L = self.L[self.L != 0]

        return self.C, self.L

def main():

    filter_type = input('Filter Type: ')

    filter_characteristic = input('Filter characteristic: ')
    impedance = float(input('Impedance: '))
    filter_order = int(input('Filter order: '))

    flt = Filter(filter_type, filter_order, filter_characteristic, impedance)
    
    if(filter_type == 'BPF' or filter_type == 'BSF'):
        flt.fcut_low = float(input('Low cutoff frequency: '))
        flt.fcut_high = float(input('High cutoff frequency: '))
    elif(filter_type == 'LPF' or filter_type == 'HPF'):
        flt.fcut = float(input('Cutoff frequency: '))
    else:
        print('Invalid input for given filter type. Exiting the program.')
        exit()

    C, L = flt.solve()

    print("Values for C")
    print(C)
    print("Values for L")
    print(L)
        
main()
