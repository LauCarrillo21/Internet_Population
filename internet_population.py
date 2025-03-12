#Import Data
import csv
#Import Matplot to be able to create the plot
import matplotlib.pyplot as plt

#Create a variable to identify the file
filename = 'data.csv'
#Creates an empty dictionary that will store population data for each continent.
population_per_continent = {}

#Actions to take with the data
with open(filename, 'r') as csvfile:
  #Convert file to a Python Dictionary
  reader = csv.DictReader(csvfile)
  #Loop through each line in reader
  for line in reader:
    continent = line['continent']
    year = line['year']
    population = line['population']

    #Check if the continent exists in the dictionary
    if continent not in population_per_continent:
      #Initialize an entry for the new continent
      population_per_continent[continent] = {'population': [], 'years': []}
    #Store the population and year data
    population_per_continent[continent]['population'].append(population)
    population_per_continent[continent]['years'].append(year)

   

#Independent Plot
#X horizontal axis, Y vertical axis
plt.plot([2000, 2010, 2020, 2030], [100, 200, 300, 400], label="Europe", marker="o")
plt.plot([2000, 2010, 2020, 2030], [200, 300, 500, 800], label="Asia", marker="o")

#Plot Details
plt.title("Internet Population per continent")
plt.xlabel("Year")
plt.ylabel("Internet users")
plt.grid(True)
plt.legend()

#Show the Plot
plt.show()