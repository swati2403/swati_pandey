a="Honesty is the best policy"
b=["Honesty","best"]
company_details=[]
word=a.split()
for word in word:
    for match in b:
        if(match==word):
            company_details.append(match)
        #else:
            #company_details.append("NULL")

print(company_details)
