import pandas as pd
data_file = "C:/Users/307-07/Downloads/data/missing_data.test.csv"

df = pd.read_csv(data_file, encoding="cp949", index_col="연도")

 