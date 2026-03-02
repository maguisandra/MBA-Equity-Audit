import pandas as pd       
import numpy as np        

path = "C:/Users/SANDRINE/Documents/MBA_data_admission_Project/MBA.csv"
df = pd.read_csv(path,encoding="utf-8")

# Replace null values
df["admission"] = df["admission"].fillna("Deny")
df["race"] = df["race"].fillna("International")

# Work Experience Groups
df["work_exp_group"] = pd.cut(
    df["work_exp"],
    bins=[0, 3, 6, 10],        
    labels=["1-3 years", "4-6 years", "7+ years"]
)

# GMAT Groups
df["gmat_group"] = pd.cut(
    df["gmat"],
    bins=[550, 600, 650, 700, 750, 800],
    labels=["550-599", "600-649", "650-699", "700-749", "750-800"]
)

# GPA Groups
df["gpa_group"] = pd.cut(
    df["gpa"],
    bins=[2.50, 2.75, 3.00, 3.25, 3.50, 3.75, 4.00],
    labels=["2.50-2.74", "2.75-2.99", "3.00-3.24", "3.25-3.49", "3.50-3.74", "3.75-4.00"]
)

df

