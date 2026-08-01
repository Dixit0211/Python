import pandas as pd
import numpy as np

from io import StringIO,BytesIO

## combining usecols and index_col
data = ('a,b,c\n'
        '4,apple,bat,\n'
        '8,orange,cow,')

print(pd.read_csv(StringIO(data), usecols=['b','c'], index_col=False))

## Quoting and Escape Characters. very useful in NLP

"""
        Some text files use special characters (like quotes or delimiters) inside values.
        Normally, this would confuse the parser because pandas thinks the delimiter marks the end of a column.
        escapechar tells pandas: “If you see this character, treat the next character literally, not as a delimiter or quote.”
        It’s like saying: “Ignore the special meaning of the next character.”
"""

data = 'a,b\n"hello, \\"Bob\\", nice to see you",5'

print(pd.read_csv(StringIO(data), escapechar='\\'))

"""
df = pd.read_csv('https://download.bls.gov/pub/time.series/cu/cu.item', sep='\t')
print(df.head())

        The sep parameter in pandas.read_csv() tells pandas what character is used to separate values in the file.
        By default, pandas assumes a comma (,) — that’s why it’s called CSV (Comma-Separated Values). But many files use other delimiters like tabs (\t), semicolons (;), or pipes (|). If you don’t set sep correctly, pandas won’t split the columns properly.
"""

