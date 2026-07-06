import pandas as pd

df = pd.read_csv("jobs.csv")

# print(df[df["Status"] == "Applied"])

# print(df.groupby("Status").size())

# print(df.sort_values(by="Company"))

df["Priority"] = df["Status"].apply(
    lambda x: "High" if x == "Interview" else "Low"
)

print(df)