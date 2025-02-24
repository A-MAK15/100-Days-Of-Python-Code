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
        
    
# for name in meeting_instances["Person_Name"]:
#     if name == "Karen Smith":
#         print(name)

