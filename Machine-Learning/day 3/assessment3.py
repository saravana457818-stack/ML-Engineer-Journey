import pandas as pd
from sklearn.datasets import fetch_openml

df = fetch_openml('titanic', version=1, as_frame=True)['data']

print(df.info())