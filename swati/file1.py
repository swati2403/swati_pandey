import pandas as pd
import requests
import json
company_df=pd.read_csv('/home/mw-swathi_ubuntu/Downloads/sanitized_it_company.csv')
company_df.head()
for index,curated in company_df.iterrows():
    indiv_item=curated[1]
    print(indiv_item)
    resp=requests.post("https://developers.google.com/apis-explorer/?hl=en_US#p/language/v1/language.documents.analyzeEntities",indiv_item)
    print(resp)
   """ obj = json.loads(resp)
    print(type(obj))"""
    exit() 

"""company_df.to_csv('/home/mw-swathi_ubuntu/Downloads/sanitized_it_company1.csv')
"""
