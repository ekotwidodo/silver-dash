import pandas as pd

def read_csv(filename):
  df = pd.read_csv(filename)
  return df

def read_excel(filename):
  df = pd.read_excel(filename)
  return df