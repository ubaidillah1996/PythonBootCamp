# Exercise 1 : PAPARKAN SEMUA DATA

import pandas as pd

df = pd.read_csv("jaa.csv")

# print(df)

# Eexercise 2 : PAPARKAN MAKLUMAT APPLIED SAHAJA

# df = pd.DataFrame(data columns, =["Applied"])

# print(df)


# applied_job = df[df["Status"] == "Applied"] #fixed code

# print(applied_job)

# Exercise 3 : KIRA JUMLAH SETIAP STATUS

# df["Status"].value_counts()

# (df["Status"].value_counts(print)) # fixed code

# Exercise 4 : SUSUN IKUT COMPANY

# print(df.sort_values(by=["Company"], ascending=True))

# EXERCISE 5 : TAMBAH COLUMN BARU
# Priority
# Interview = High
# Lain-lain = Low

# df.loc[len(df)] = ["Priority"]

df["Priority"] = df["Status"].apply(
    lambda x : "High" if x == "Interview" else "Low"
)

print(df)