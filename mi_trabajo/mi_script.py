# conda activate mlcourse
# conda install -c conda-forge ydata-profiling
# pip install numba==0.58.1
import os

import pandas as pd
from ydata_profiling import ProfileReport

PATH = "data/telecom_churn.csv"

print(f"Working on {os.getcwd()}")
print(f"Reading data from {PATH}")
df = pd.read_csv(PATH)
profile = ProfileReport(df, title="Pandas Profiling Report")
profile.to_file("output.html")
