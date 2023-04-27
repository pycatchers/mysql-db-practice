import pandas as pd

file_path = "/home/paranthaman/Downloads/cereal.csv"

cereals_df = pd.read_csv(file_path)
#
print(cereals_df.columns.value_counts())
# print(cereals_df.dtypes)
#
# # for row in cereals_df.itertuples():
# #     print(tuple(row)[1:])
#
# # print(cereals_df)
# print()