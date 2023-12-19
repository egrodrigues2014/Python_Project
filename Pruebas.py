from Project import get_float_from_input, get_int_from_input, populate_df
import pytest
import pandas as pd
import datatest as dt

b = populate_df(1,1000,100,0.01)
print(b)

a = {'Opening_Balance' : float(1000), 'Monthly_Investment' : float(100), 'Total_Month_Investment_Amount' : float(1100), 'Interest_Amount' : float(11), 'Final_Amount' : float(1111)}
print(a)

print(a ==b)