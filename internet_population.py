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
    #Convert data to integer to be able to show in plot
    continent = line['continent']
    year = int(line['year'])
    population =int(line['population'])

    #Check if the continent exists in the dictionary
    if continent not in population_per_continent:
      #Initialize an entry for the new continent
      population_per_continent[continent] = {'population': [], 'years': []}
    #Store the population and year data
    #The population and year from the current CSV row are added to the respective lists for that continent
    population_per_continent[continent]['population'].append(population)
    population_per_continent[continent]['years'].append(year)

#Loop through each continet
for continent in population_per_continent:
  #Define X and Y variables
  years = population_per_continent[continent]['years']
  population = population_per_continent[continent]['population']
  #Plot with X & Y axis
  plt.plot(years, population, label=continent, marker="o", alpha=0.5)   

#Plot Details
plt.title("Internet Population per continent")
plt.xlabel("Year")
plt.ylabel("Internet users (in billion users)")
plt.grid(True)
plt.legend()

#Show the Plot
plt.show()