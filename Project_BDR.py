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

# Data Cleansing
# Dua kolom yang menunjukkan terjadinya transaksi tidak bertipe datetime,
# maka ubahlah kedua kolom tersebut ke tipe data datetime.
# Kemudian cetaklah kembali 5 data teratas dari dataframe df dan juga tipe data masing-masing kolomnya.

# Kolom First_Transaction
df['First_Transaction'] = pd.to_datetime(
    df['First_Transaction']/1000, unit='s', origin='1970-01-01')
# Kolom Last_Transaction
df['Last_Transaction'] = pd.to_datetime(
    df['Last_Transaction']/1000, unit='s', origin='1970-01-01')

print('Lima data teratas:')
print(df.head())

print('\nInfo dataset:')
print(df.info())
