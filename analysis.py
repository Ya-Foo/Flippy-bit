import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

directory = os.getcwd()
bot_path = fr"{directory}\bot"
data_path = fr"{directory}\data"


# ============================================================= #
# ================= Prepare data for plotting ================= #
# ============================================================= #
data = {}
for botVersion in os.listdir(bot_path):
    log_path = fr"{os.path.abspath(fr"bot\{botVersion}")}\log.txt"
    data[botVersion] = []
    with open(log_path, 'r') as f:
        for score in f:
            data[botVersion].append(int(score.rstrip("\n")))

# Ensure that column have equal entries
maxLen = len(max(data.values(), key=lambda x: len(x)))
maxVal = max(max(data.values(), key=lambda x: max(x)))
minVal = min(min(data.values(), key=lambda x: min(x)))
for k, v in data.items():
    while len(v) != maxLen:
        data[k].append(None)
data = pd.DataFrame(data).convert_dtypes()


# ============================================================= #
# =========================== Plot ============================ #
# ============================================================= #
sns.set(style="ticks", context="talk")

dist = sns.displot(data, kind='kde', rug=True, fill=True)
plt.savefig(fr'{data_path}\dist.svg', bbox_inches='tight')

hist = sns.histplot(data, legend=False)
hist.set_xlim(minVal, maxVal)
plt.savefig(fr'{data_path}\hist.svg', bbox_inches='tight')

box = sns.boxplot(data, legend=False)
sns.stripplot(data, size=4, color=".3")
plt.savefig(fr'{data_path}\box.svg', bbox_inches='tight')