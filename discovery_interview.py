import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

meeting_instances = pd.read_csv("meeting_instances.csv")
meeting_instances

meeting_metadata = pd.read_csv("meeting_metadata.csv")
meeting_metadata

person_info = pd.read_csv("person_info.csv")
person_info

person_level_df = person_info[["Person_Name", "Person_Level"]]

names_dic = dict(zip(person_level_df["Person_Name"], person_level_df["Person_Level"]))
# print(names_dic)
# print(names_dic["Pieter van Wyk"])
 
names_list = []
for names in person_info["Person_Name"]:
    # print(names)
    names_list.append(names)
# print(names_list)

# print(meeting_instances["Person_Name"])

for name in names_list:
    print(name)
    # print(names_dic[name])
    
    new_df = meeting_instances[meeting_instances["Person_Name"] == name] #creates a whole new dataframe with only a particular person
    new_df["Person_Name"] = names_dic[name]
    print(new_df[["Person_Name", "Meeting_Sentiment"]])

        # upated_name = names_dic[name]
        # new_df["Person_Name"] = updated_name
        # print(new_df[["Person_Name","Meeting_Sentiment"]])
    print("Mean : ", end="")
    print(new_df["Meeting_Sentiment"].describe().loc["mean"])
    # # print(new_df.describe())
    print("\n" * 5)
        
    
# print(len(person_level_df))
# print(person_level_df[4][["Person_Name", "Meeting_Sentiment"]])

exec_count = 0
exec_count_mean = 0

manager_count = 0
manager_count_mean = 0

staff_count = 0
staff_count_mean = 0

for df in person_level_df:
    if df["Person_Name"].iloc[0] == "Executive":
        exec_count += 1
        exec_count_mean += df["Meeting_Sentiment"].describe().loc["mean"]
        executive_average = exec_count_mean / exec_count

    elif df["Person_Name"].iloc[0] == "Manager":
        manager_count += 1
        manager_count_mean += df["Meeting_Sentiment"].describe().loc["mean"]
        manager_average = manager_count_mean / manager_count
# print(exec_count)

    elif df["Person_Name"].iloc[0] == "Staff":
        staff_count += 1
        staff_count_mean += df["Meeting_Sentiment"].describe().loc["mean"]
        staff_average = staff_count_mean / staff_count
# print(staff_count)
print("Executive Average Meeting Sentiment : ", end="")
print(round(executive_average, 3))

print("Manager Average Meeting Sentiment : ", end="")
print(round(manager_average, 3))

print("Staff Average Meeting Sentiment : ", end="")
print(round(staff_average, 3))

# person_df[5]
for x in range (len(person_df)):
    print(person_df[x]["Person_Name"].iloc[0], ": ", end="")
    print(len(person_df[x]["Person_Name"]))

plt.figure(figsize=(8, 6))
sns.histplot(meeting_instances["Meeting_Sentiment"], bins=25, kde=True)
plt.title("Distribution of Meeting sentiments")
plt.xlabel("Meeting sentiments")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
