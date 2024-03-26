import pandas as pd





df = pd.read_csv("input/laptop_price_cleaned.csv")

target = "Price_euros"

y = df[target]
X = df.drop(target, axis=1)


categorical_columns = X.select_dtypes(include=['category', 'object']).columns.tolist()
continuous_columns = X.select_dtypes(include=['float64', 'int32']).columns.tolist()


