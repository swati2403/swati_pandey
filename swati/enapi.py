import six
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from textblob import TextBlob

import pandas as pd

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="My-First-Project-6c02d45824ae.json"

result_df = pd.DataFrame(columns=['source_vendor_name','type','mid','wiki_url','result_vendor_name'])
company_info_df = pd.read_csv('companies.csv',low_memory=False)
only_head = company_info_df["company_name"]
only_head = only_head
# print(only_head)

index = 1
for company in only_head:
    company_details = []
    company_details.append(company);
    # print(company)

    text = company

    blo = TextBlob(text)

    #print(blo.detect_language())
    try:

        client = language.LanguageServiceClient()

        if isinstance(text, six.binary_type):
            text = text.decode('utf-8')

        # Instantiates a plain text document.
        document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT)

        # Detects entities in the document. You can also analyze HTML with:
        #   document.type == enums.Document.Type.HTML
        entities = client.analyze_entities(document).entities

        if(len(entities) >= 1):
            for entity in entities:
                entity_type = enums.Entity.Type(entity.type)
                company_details.append(entity_type.name);
                company_details.append(entity.metadata.get('mid', '-'))
                company_details.append(entity.metadata.get('wikipedia_url', '-'))
                company_details.append(entity.name)


                # print(u'{:<16}: {}'.format('mid', entity.metadata.get('mid', '-')))
                # print(u'{:<16}: {}'.format('wikipedia_url', entity.metadata.get('wikipedia_url', '-')))
                # print(u'{:<16}: {}'.format('name', entity.name))
                break
        result_df.loc[index] = company_details
        print(index)
        index = index + 1
    except:
        print("in except block")
        company_details.append('-');
        company_details.append('-');
        company_details.append('-');
        company_details.append('-');
        result_df.loc[index] = company_details
        index = index + 1


result_df.to_csv('corpwatch_sanitized_entityanalysis.csv')