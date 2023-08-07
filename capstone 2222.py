import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly as px






data = pd.read_csv("C:/Users/Elsayed Hassan/.spyder-py3/autosave/International_Report_Departures.csv")

#x = data.iloc[:,:-1]
#y = data.iloc[:,-1]

df = pd.DataFrame(data)
df = df.drop("data_dte", axis=1)




column_types = {col : "numerical" if df[col].dtype in ["int64","float64"]  else "categorical" for col in df.columns}


df.fillna(method = "ffill", inplace=True)



df = pd.get_dummies(df, columns=[col for col , col_type in column_types.items() if col_type == "categorical"])

data_numerical = df[[col for col, col_type in column_types.items() if col_type == 'numerical']]
data_normalized = (data_numerical - data_numerical.min()) / (data_numerical.max() - data_numerical.min())
df[data_normalized.columns] = data_normalized


for col, col_type in column_types.items():
    if col_type == "numerical":
        
        plt.figure()
        sns.histplot(df[col], kde=True)
        plt.title(f"histogram for {col}")
        plt.show()
        
        
        plt.figure()
        sns.boxplot(df[col])
        plt.title(f"box plot for {col}")
        plt.show()
        
        
        
        plt.figure()
        sns.scatterplot(data = df, x=col , y="target")
        plt.title(f"scatter plot for {col}")
        plt.show()
    
    elif col_type == "categorical":
    
        plt.figure()
        sns.barplot(data = df, x=col , y="target")
        plt.title(f"bar plot for {col}")
        plt.show()
        
        
   
        
        
        
        