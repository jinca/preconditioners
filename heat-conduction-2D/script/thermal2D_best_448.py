import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
plt.rcParams.update({'font.size': 15})

df = pd.read_csv("best_the_large_name_ALL.csv")

fig, ax = plt.subplots(2, sharex=True)

sns.boxplot(x="mpi", y="fep", hue="opt_name", data=df, ax=ax[0])
sns.boxplot(x="mpi", y="time", hue="opt_name", data=df, ax=ax[1])
ax[0].set_ylabel("FE time (s)")
ax[0].set_xlabel("MPI tasks (n)",fontdict={"fontsize":16})
ax[1].set_ylabel("Total Time (s)")
ax[1].set_xlabel("MPI tasks (n)",fontdict={"fontsize":16})
ax[0].legend()
ax[1].legend()
plt.show()

