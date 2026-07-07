import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("job.csv")

status_count = df["Status"].value_counts()

status_count.plot(kind="bar")

plt.title("Job Applications")
plt.show()