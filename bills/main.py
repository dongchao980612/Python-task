import os
import pandas as pd # rename 
"""
#inlcude <stdio.h>  

a.h a.c

main.c
"""

dirpath = os.path.dirname(__file__)
out = os.path.join(dirpath, "out.tsv")
files = [os.path.join(dirpath, f) for f in os.listdir(dirpath) if f.endswith(".xls") or f.endswith(".xlsx")]

df_list = [pd.read_excel(f) for f in files]
df = pd.concat(df_list, axis=0)
grp = df.groupby("员工姓名").sum().reset_index()

print(grp)
grp.to_csv(out, index=False, sep="\t")


