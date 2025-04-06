import datetime as dt
import pandas as pd

## 1. Web Scape Using Pandas
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
data = pd.read_html(url)
print(f"We have a {type(data)} with length {len(data)}")

print(data[0].head())