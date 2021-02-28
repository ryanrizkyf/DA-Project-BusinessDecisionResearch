# Importing Data dan Inspection
# Importlah dataset dari https://storage.googleapis.com/dqlab-dataset/data_retail.csv
# dan kemudian inspeksilah dataset tersebut dengan :
# 1. mencetak lima data teratas saja,
# 2. mencetak info dataset.

import pandas as pd

df = pd.read_csv(
    'data_retail.csv', sep=';')

print('Lima data teratas:')
print(df.head())

print('\nInfo dataset:')
print(df.info())
