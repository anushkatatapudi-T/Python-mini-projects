import pandas as pd
df = pd.read_csv("students.csv")

print("\n--- CSV DATA ANALYZER ---")

print("Total records:", len(df))

print("\nColumn names:")
print(df.columns)

print("\nAverage age:", df["age"].mean())

print("\nOldest person:")
print(df.loc[df["age"].idxmax()])

print("\nYoungest person:")
print(df.loc[df["age"].idxmin()])

print("\nEducation counts:")
print(df["class"].value_counts())

print("\n-PEOPLE AGE ABOVE 18-")
print(df.loc[df['age'] > 18])
print("Number of age : " , len(df.loc[df['age'] > 18]))


print("\n-PEOPLE AGE BELOW 18-")
print(df.loc[df['age'] <= 18])
print("Number of age :", len(df.loc[df['age'] <= 18]))

print("\nCommon classes : " ,df['class'].value_counts().idxmax())
print("Number of people : " ,df['class'].value_counts().max() )
print("People are : ")
print(df.loc[df['class'] == 'btech'])
print("Avg : ",df.loc[df['class'] == "btech"]['age'].mean().round(2))
young = df.loc[df['class'] == "btech"]
print("\nYoungest person : " , young.min())
print("---DATA SUMMARY---")
print("Total people : ",len(df))
print("Avg age : " , round(df['age'].mean(),2))
print("Oldest age : " , df['age'].idxmax())
print("Youngest age " , df['age'].idxmin())
print("\n People in each class : ")
print(df['class'].value_counts())
print("Missing values in each column :")
print(df.isnull().sum())
print('\n=============================================')
print("Data anaylsis completed successfully!")