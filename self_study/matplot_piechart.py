import matplotlib.pyplot as plt

status = ["Applied", "Interview", "Rejected"]
count = [5,2,1]

plt.pie(count, labels=status)

plt.title("Job Status Distribution")

plt.show()
