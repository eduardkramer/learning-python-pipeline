import pandas as pd

# CSV-bestand inlezen
df = pd.read_csv("data/orders.csv")

# Dataset tonen
print(df.head(4))