import pandas as pd
from sklearn.datasets import fetch_openml
import urllib.error

print("Fetching Titanic dataset...")

try:
    # Try fetching from OpenML first
    df = fetch_openml('titanic', version=1, as_frame=True)['data']
    print("Successfully fetched from OpenML.")
except (urllib.error.HTTPError, urllib.error.URLError, Exception) as e:
    print(f"OpenML fetch failed ({e}). Falling back to Seaborn's GitHub data source...")
    # Fallback to a reliable raw CSV dataset from GitHub
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
    df = pd.read_csv(url)
    print("Successfully fetched from GitHub fallback.")

print("\nDataset Info:")
print(df.info()) 
df.isnull().sum()

import seaborn as sns
import matplotlib.pyplot as plt

sns.set()
mis_val_table=pd.DataFrame(df.isnull().sum()/len(df)*100)
mis_val_table.plot(kind='bar',title="percentage of missing values")
plt.show()
print(f"size of the datasets: {df.shape}")
df.drop(['body'],axis=1,inplace=True)
print(f"size of the datasets: {df.shape}")