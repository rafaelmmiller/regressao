# -*- coding: utf-8 -*-
"""
Created on Mon Jun 05 20:14:05 2017

@author: rmmil
"""

import numpy as np
import pandas
from scipy import stats


df = pandas.read_excel('pedidos.xlsx')
f = open('resultado.txt', 'w')

for column in df.columns:
    
    for column2 in df.columns:
        
        values1 = []
        values2 = []
                
        values1 = np.array(df[column].values)
        values2 = np.array(df[column2].values)
              
        values2 = values2[np.logical_not(np.isnan(values1))]
        values1 = values1[np.logical_not(np.isnan(values1))]

        values1 = values1[np.logical_not(np.isnan(values2))]
        values2 = values2[np.logical_not(np.isnan(values2))]
        
# Altera a estrutura do array pra (numero_de_colunas,1)
#values1 = np.reshape(values1, (values1.size,1))
#values2 = np.reshape(values2, (values2.size,1))    

        if values1.size == 0 or values2.size == 0 or column == 'Pedidos' or column2 == 'Pedidos':
            pass
        else:
        
            slope, intercept, r_value, p_value, std_err = stats.linregress(values1, values2)
    
            if r_value**2 > 0.7 and column != column2:
                #print(repr(column).rjust.format(column, column2,r_value**2))
                print column,"\t",column2,"\t", r_value**2,"\n"
                print >> f, column,"\t",column2,"\t", r_value**2,"\n"
                

