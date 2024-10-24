import pandas as pd
import numpy as np

s = pd.Series(list('abca'))

print(pd.get_dummies(s))


s1 = ['a', 'b', np.nan, np.nan,1,2, 'a']

print(pd.get_dummies(s1, dummy_na=True))


df = pd.DataFrame({'A': ['a', 'b', 'a'], 'B': ['b', 'a', 'c'],
                   'C': [1, 2, 3]})

#print(pd.get_dummies(df, prefix=['col1', 'col2']))

#print(s)