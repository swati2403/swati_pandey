import csv
reader=csv.reader(open('sanitized_it_company.csv','r'))
writer=csv.writer(open('sanitized_it_company1.csv','w'))
for row in reader:
    writer.writerow(row)

