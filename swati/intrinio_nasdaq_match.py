import pandas as pd
intri_df=pd.read_csv("intrinio_it_sanitized_entityanalysis.csv")
intri_mid=intri_df['mid']
intri_vendor=intri_df['source_vendor_name']
intri_mid = list(intri_mid)
intri_vendor = list(intri_vendor)

nasdaq_df = pd.read_csv("nasdaq_it_sanitized_entityanalysis.csv")
nasdaq_mid=nasdaq_df['mid']
nasdaq_vendor=nasdaq_df['source_vendor_name']
match=[]
vendor = []
vendor1 = []
index=1
final_list = pd.DataFrame(columns=['match'])
result_df = pd.DataFrame(columns=['Intrinio_source_vendor_name'])
nasdaq=pd.DataFrame(columns=['Nasdaq_source_vendor_name'])

nasdaq_mid = list(nasdaq_mid)
nasdaq_vendor=list(nasdaq_vendor)
#print(nasdaq_mid)
for (i, b) in zip(intri_mid,intri_vendor): 
	print("enter to for loop")
	for (j,a) in zip(nasdaq_mid,nasdaq_vendor):
		if(i!="-" and j!="-"):
			if j == i:
				match.append(j)
				vendor.append(b)
				vendor1.append(a)
				#print(match)

for (m,v,v1) in zip(match,vendor,vendor1):
	final_list.loc[index] = m
	result_df.loc[index] = v
	nasdaq.loc[index]=v1
	print(index)
	index = index + 1

#print(match)
result_df=pd.merge(result_df,final_list,right_index=True, left_index=True)
result_df=pd.merge(result_df,nasdaq,right_index=True, left_index=True)
result_df.to_csv('match.csv',index=False)