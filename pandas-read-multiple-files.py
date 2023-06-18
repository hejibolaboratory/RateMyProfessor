# importing pandas
import pandas as pd

file_list=["students%s.csv"%count for count in range(1,240)]

print(file_list)
 
main_dataframe = pd.DataFrame(pd.read_csv(file_list[0]))
 
for i in range(1,len(file_list)):
    data = pd.read_csv(file_list[i])
    df = pd.DataFrame(data)
    main_dataframe = pd.concat([main_dataframe,df],axis=1)
print(main_dataframe)