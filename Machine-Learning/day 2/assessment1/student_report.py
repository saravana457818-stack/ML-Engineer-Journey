import pandas as pd
df=pd.read_csv("ML/day 2/assessment1/student.csv")
print(df)
print("the average marks:",df["Marks"].mean())
topper = df.loc[df["Marks"].idxmax()]
print("the topper name and its mark:", topper["Name"], topper["Marks"])
print("the students above 80:\n", df[df["Marks"] > 80][["Name", "Marks","Age"]].to_string(index=False))
print("the student details has been updated")




