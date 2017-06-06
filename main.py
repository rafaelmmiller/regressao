# -*- coding: utf-8 -*-
"""
Created on Mon Jun 05 20:14:05 2017

@author: rmmil
"""

import numpy as np
import pandas
from scipy import stats


df = pandas.read_excel('pedidos.xlsx')

values1 = np.array(df[131].values)
values2 = np.array(df[132].values)
            
              
values2 = values2[np.logical_not(np.isnan(values1))]
values1 = values1[np.logical_not(np.isnan(values1))]

values1 = values1[np.logical_not(np.isnan(values2))]
values2 = values2[np.logical_not(np.isnan(values2))]
        
# Altera a estrutura do array pra (numero_de_colunas,1)
#values1 = np.reshape(values1, (values1.size,1))
#values2 = np.reshape(values2, (values2.size,1))    
        
slope, intercept, r_value, p_value, std_err = stats.linregress(values1, values2)

print "r-squared:", r_value**2
