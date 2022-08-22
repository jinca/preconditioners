import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
plt.rcParams.update({'font.size': 17})

df = pd.read_csv("best_9_dmono_8_7_name_OK.csv")
df = df[df["time"]!= 0]

fig, ax = plt.subplots(2, sharex=True)

sns.boxplot(x="opt_name", y="fep", data=df, ax=ax[0])
plt.xticks(rotation=12, fontsize=15)
sns.boxplot(x="opt_name", y="time", data=df, ax=ax[1])
ax[0].set_ylabel("FE time (s)")
ax[1].set_ylabel("Total Time (s)")
ax[0].set_xlabel("HypreBoomerAMG options")#,fontdict={"fontsize":12})
#ax[0].legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
ax[1].set_xlabel("HypreBoomerAMG options")#,fontdict={"fontsize":12})
#ax[1].legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
