import csv

def file_open():
    with open('data-398-2018-08-30.csv') as isfile:
        reader = csv.DictReader(isfile)
        r = list(reader)
        for row in r:
        	print(row['Name'])


file_open()