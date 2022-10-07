import os
import platform
import glob
import seaborn as sns
from dateutil.parser import parse
import pandas as pd
import matplotlib.pyplot as plt
def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime

mutation_type_map = {"cmp-int-replace": "Compare\nOperator","const-replace":"Constant",
                     "branch-swap": "Branch\nSwap", "binop-int-replace":"Binary\nOperator", "cmp-swap": "Cmp\nSwap", "select-swap":"Select\nSwap" }


survival_path_dir = "/Users/ruji/Desktop/fuzz/s2n-tls/tests/saw/work/fuzz/seeds"



# Collect the information of all the surviving mutant, indexed by key (function/ instruction) 

seed_time = []
for report_dir in glob.glob(survival_path_dir + "/**"):
    trace_file = report_dir + "/trace.json"
    seed_time.append(creation_date(trace_file))

np_array = []

cnt = 0
for i in range(len(seed_time)):
    temp_array = []
    temp_array.append(seed_time[i])
    np_array.append(temp_array)
    cnt = cnt + 1

df = pd.DataFrame(np_array, columns=["Time Stamp"])
fig = sns.histplot(df, x="Time Stamp", cumulative=True, kde = True,alpha=.4)

fig.set(xlabel='Time Stamp (second)', ylabel='Number of Seed')
plt.savefig("seed_distribution.pdf")