#!/usr/bin/env python
# coding: utf-8

# # Analysis of Access, Equity, and Diversity in MBA Admissions

# ### Loading the Dataset and Checking for Missing Values
# In this section, we load the MBA Admissions dataset into a Pandas DataFrame and check for missing values to understand the completeness of our data.

# In[1]:


import pandas as pd       # for data manipulation
import numpy as np        # for numerical operations
import matplotlib.pyplot as plt  # for plotting
import seaborn as sns     # for advanced visualizations
from ydata_profiling import ProfileReport


# In[2]:


import os
base_dir = os.getcwd()
file_path = os.path.join(base_dir, "Data", "MBA.csv")

df = pd.read_csv(file_path)
df.head()


# In[3]:


import os
print("Fichiers dans le dossier Data :", os.listdir("Data"))


# In[4]:


# Check the missing values
df.isnull().sum()


# ### Data Cleaning Notes
# 
# According to the dataset documentation:
# 
# - In the `admission` column, null values represent **Denied** applications. We will fill these nulls with "Deny" to make our analysis clearer and more consistent.
# - In the `race` column, null values correspond to **international students**. We will fill these nulls with "International" to simplify our categorical analysis.
# 

# In[5]:


# Replace nulls in 'admission' with 'Deny' and nulls in race  with international
df["admission"]=df["admission"].fillna("Deny")
df["race"]=df["race"].fillna("International")
df.isnull().sum()



# ### Statistics

# In[6]:


# Summary statistics for numeric columns
df[['gpa', 'gmat', 'work_exp']].describe()


# In[7]:


# Categorical columns
categorical_cols = ['gender', 'international', 'major', 'race', 'work_industry', 'admission']
for col in categorical_cols:
    print(df[col].value_counts(normalize=True) * 100)
    print("\n")


# ### Transforming Work Experience, gpa and gmat  into Categories

# In[8]:


# Create exp_group bins 
df["work_exp_group"] = pd.cut(
    df["work_exp"],
    bins=[0, 3, 6, 10],        
    labels=["1-3 years", "4-6 years", "7+ years"]
)
# Check the transformation
print(df["work_exp_group"].value_counts().sort_index())
  


# In[9]:


# Create gmat_group bins
df["gmat_group"] = pd.cut(
    df["gmat"],
    bins=[550, 600, 650, 700, 750, 800],
    labels=[
        "550–599",
        "600–649",
        "650–699",
        "700–749",
        "750–800"
    ]
)
#Check the transformation
print(df["gmat_group"].value_counts().sort_index())


# In[10]:


#Create gpa_group bins 
df["gpa_group"] = pd.cut(
    df["gpa"],
    bins=[2.50, 2.75, 3.00, 3.25, 3.50, 3.75, 4.00],
    labels=[
        "2.50–2.74",
        "2.75–2.99",
        "3.00–3.24",
        "3.25–3.49",
        "3.50–3.74",
        "3.75–4.00"
    ]
)
#Check the transformation 
print(df["gpa_group"].value_counts().sort_index())


# ### Distribution

# In[11]:


# Race distribution
race_counts = df['race'].value_counts(normalize=True) * 100
print("Percentage of applicants by race:")
print(race_counts.round(2))
print("\n")

# major distribution
major_counts = df['major'].value_counts(normalize=True) * 100
print("Percentage of applicants by major:")
print(major_counts.round(2))
print("\n")
# Industry distribution
work_industry_counts = df['work_industry'].value_counts(normalize=True) * 100
print("Percentage of applicants by industry:")
print(work_industry_counts.round(2))
print("\n")

# Gender distribution
gender_counts = df['gender'].value_counts(normalize=True) * 100
print("Percentage of applicants by gender:")
print(gender_counts.round(2))
print("\n")

# international distribution
intl_counts = df['international'].value_counts(normalize=True) * 100
print("Percentage of applicants by international status:")
print(intl_counts.round(2))


# ### Analysis

# In[12]:


# Admission Rate by gender
gender_admission = pd.crosstab(df["gender"], df["admission"], normalize="index") * 100
print("Admission Rate by Gender (%) ")
display(gender_admission.round(2))


# In[13]:


# Admission Rate by Major
major_admission = pd.crosstab(df["major"], df["admission"], normalize="index")*100
print("Admission Rate  by Major (%)")
(major_admission.round(2))


# In[14]:


# Admission Rate by race
race_admission=pd.crosstab(df["race"], df["admission"], normalize="index")*100
print("Admission Rate by Race (%)")
display(race_admission.round(2))


# In[15]:


#Admission Rate by work-industry
work_industry_admission=pd.crosstab(df["work_industry"], df["admission"], normalize="index")*100
print("Admission Rate by work_industry (%)")
display(work_industry_admission)


# In[16]:


# Admission rate by work_exp_group
admission_work_exp_group= pd.crosstab(df["work_exp_group"], df["admission"], normalize="index")*100
print("Admission by Work_exp")
display(admission_work_exp_group)


# In[17]:


# Mean of gpa and gmat of admssion statut
df1=df.groupby("admission")[["gpa", "gmat"]].mean().round(5)
df1


# In[18]:


# Mean of GPA and GMAT
mean_gpa = df['gpa'].mean()
mean_gmat = df['gmat'].mean()
mean_exp = df["work_exp"].mean()

print(f"Mean GPA: {mean_gpa:.2f}")
print(f"Mean GMAT: {mean_gmat:.2f}")
print(f"Mean work_exp:{mean_exp:.2f}")


# In[19]:


print(df.dtypes)
print("\n")
print(df.shape)


# ### Exporting the Final Dataset for Power BI
# 

# In[20]:


# Get current working directory
base_dir = os.getcwd()

# Path for output file inside Data folder
output_path = os.path.join(base_dir, "Data", "MBA_admissions_final.csv")

# Export the DataFrame without index
df.to_csv(output_path, index=False)

