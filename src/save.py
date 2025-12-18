# save.py
import pandas as pd

def save_report(results):
    df = pd.DataFrame(results)
    df.to_csv("data/job_report.csv", index=False)
    print("\nReport saved to data/job_report.csv")
