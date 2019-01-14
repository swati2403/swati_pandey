import pandas as pd
df = pd.read_csv('latest_curated.csv',low_memory=False,encoding='latin-1')

# // Get the Item columna from csv filed
only_head = df['Item']

# print the values from item as head
# print(only_head.head())

# company_value=[]
# classi_type=[]
excel_file="CIO - Product Type v2.xlsx"
data= (pd.read_excel(excel_file, sheet_name=1))

# print('>>>>>>>>',data.head())

data  = dict(data)
# print(data)

for item in only_head:
    diction = {}
    item_word = item.split()
    # print(item_word)
    for items1 in item_word:

        print(items1,">>>>>>>>>")
        for key, value in data.items():
            value = list(value)
            if type(value) is list:
                if items1 in value:
                    print("item found")
                    diction[key] = items1
                    print(diction)

        if len(diction) > 0:
            seriesofdict = pd.Series(diction)

            # remove space and special character
            seriesofdict.to_csv(item+ ".csv")









#
# for item in only_head:
#     item_word=item.split()
#     for key,value in data.items():
#
#         value1 = value
#         value1 = str(value1)
#         if value1 in item_word :
#             #print("match found")
#             company_value.append(value1)
#             classi_type.append(key)
#         # else:
#         #     s=" "
#         #     company_value.append(s.join(item_word))
#         #     classi_type.append("-")
#
# final_list = pd.DataFrame({'value' : [company_value],
#  'Type' : [classi_type]
#   }, columns=['value','Type'])
# final_list.to_csv('final.csv',index=False)

 