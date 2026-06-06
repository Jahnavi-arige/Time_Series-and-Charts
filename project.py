import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Date": ["2024-01-01","2024-01-02","2024-01-03","2024-01-04"],
    "Sales": [100, 200, 150, 300],
    "Category": ["A","B","A","C"]
}
df = pd.DataFrame(data)
plt.figure()
df.plot(x="Date", y="Sales", kind="line", title="Sales Over Time")
plt.savefig("line.png")
plt.show()
plt.figure()
df.groupby("Category")["Sales"].sum().plot(kind="bar", title="Category Sales")
plt.savefig("bar.png")
plt.show()
plt.figure()
df.groupby("Category")["Sales"].sum().plot(kind="pie", autopct="%1.1f%%", title="Share")
plt.savefig("pie.png")
plt.show()
