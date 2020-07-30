import csv
import os
import re


with open('CSV Files/test.csv', 'r') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)
    l1 = [line[0] for line in csv_reader]
    
    files = os.listdir('files/')
    l2, l3 = [], []
    for data in files:
        ls = re.findall('[0-9]+', data)
        for i in ls:
            for j in l1:
                if i == j:
                    l3.append([j, data, 'Yes'])
                    l2.append(j)
    for i in l1:
        if not i in l2:
            l3.append([i, '----------', 'No'])

    with open('CSV Files/result.csv', 'w') as f1:

        csv_writer = csv.writer(f1)

        csv_writer.writerow(['Pr.No', 'FileName', 'Yes/No'])

        for rows in l3:
            csv_writer.writerow(rows)
