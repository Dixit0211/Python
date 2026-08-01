import pandas as pd
import numpy as np
from io import StringIO,BytesIO

## index columns and training delimiters

data = ('index,a,b,c\n'
        '4,apple,bat,5.7\n'
        '8,orange,cow,10')

print(pd.read_csv(StringIO(data), index_col=0))

data = ('a,b,c\n'
        '4,apple,bat,\n'
        '8,orange,cow,10')

print(pd.read_csv(StringIO(data), index_col=0)) # index become column number 0
print(pd.read_csv(StringIO(data), index_col=1)) # index become column number 1

print(pd.read_csv(StringIO(data),index_col = False)) # default data type is None

data = ('a,b,c\n'
        '4,apple,bat,\n'
        '8,orange,cow,')

print(pd.read_csv(StringIO(data)))
print(pd.read_csv(StringIO(data), index_col=False))