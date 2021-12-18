import os
import numpy as np
import pandas as pd

from matplotlib import pyplot as plt


file_name = 'kr_suply.csv'
df = pd.read_csv(file_name)

plt.plot(df.year, df.monetary, label="monetary")
plt.plot(df.year, df.M1, label="M1")
plt.plot(df.year, df.M2, label="M2")
plt.plot(df.year, df.Lf, label="Lf")
plt.title("Korea Money Suply", fontsize=15)
plt.xlabel("Year", fontsize=13)
plt.ylabel("Money", fontsize=13)
plt.legend()
plt.show()