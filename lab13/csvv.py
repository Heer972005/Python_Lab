#import csv
#
#with open(r'G:\sem-3\python_lab\lab13\data-1.csv', 'r') as file:
#    reader = csv.reader(file)
#    for i in reader:
#        print(i)

import csv
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Subject', 'Mark'])
    writer.writerow(['Aansh', 'PWP', 9])
    writer.writerow(['Ashutosh', 'PWP', 10])
    file.close()
