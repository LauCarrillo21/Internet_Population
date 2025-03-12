#Import Data
import csv
filename = 'data.csv'

#Actions to take with the data
with open(filename, 'r') as csvfile:
  #Convert file to a Python Dictionary
  reader = csv.DictReader(csvfile)
  for line in reader:
    continent = line['continent']
    year = line['year']
    population = line['population']

    print(continent)
    print(year)
    print(population)