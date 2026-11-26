import pandas as pd
print(pd.__version__)
 
data = {"Name":["Alice","Bob","Charlie"],
"Age":[25,30,35],
"City":["New York","Los Angeles","Chicago"]}
 
df = pd.DataFrame(data)
print(df)
 
 
s1 = pd.Series([100,200,300,400,500])
print(s1)
 
print(s1[1])
print(s1[3])
 
s2 = pd.Series([10,20,30,40,50])
print(s1 + s2)
 
 
print(df[["Name","City"]])
 
df["Salary"] = [50000,60000,70000]
print(df)
 
print(df["Age"].mean())
print(df["Salary"].sum())
 
 
print(df[df["Age"] > 28])
 
df = df.set_index("Name")
print(df)
 
df = df.reset_index()
print(df)
 
 
with open("employees.csv", "w") as f:
    f.write("Name, Department, Salary\n")
    f.write("John, Sales, 50000\n")
    f.write("Jane, Marketing, 60000\n")
    f.write("Emily, HR, 55000\n")
 
emp = pd.read_csv("employees.csv", skipinitialspace=True)
print(emp)
 
filtered = emp[emp["Salary"] > 55000]
print(filtered[["Name","Department"]])
 
 
print(emp.groupby("Department")["Salary"].mean())
 
print(emp.groupby("Department")["Salary"].agg(["min","max"]))
 
 
df1 = pd.DataFrame({
"Name":["John","Jane","Emily"],
"Department":["Sales","Marketing","HR"]
})
 
df2 = pd.DataFrame({
"Name":["John","Jane","Emily"],
"Experience (Years)":[5,7,3]
})
 
merged = pd.merge(df1, df2, on="Name")
print(merged)
 
 
print(merged.sort_values("Experience (Years)", ascending=False))