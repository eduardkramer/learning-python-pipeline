import pandas as pd

# CSV-bestand inlezen
df = pd.read_csv("data/orders.csv")

# Rijen met ontbrekende waarden verwijderen
df_clean = df.dropna()

# Schone dataset tonen
print(df_clean)