#For a few files:
import pandas as pd
df = pd.concat(map(pd.read_csv, ['data/d1.csv', 'data/d2.csv','data/d3.csv']))

#For many files:
from os import listdir
filepaths = [f for f in listdir("./data") if f.endswith('.csv')]
df = pd.concat(map(pd.read_csv, filepaths))

import glob
df = pd.concat(map(pd.read_csv, glob.glob('data/*.csv))



