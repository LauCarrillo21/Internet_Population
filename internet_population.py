#Import Data
import csv
#Import Matplot to be able to create the plot
import matplotlib.pyplot as plt

#Generate polutation dictionary from csv data
def generate_population_dictionary_from_csv(filename):
  '''
  Return a dictionary follow this structure:
  {
    "Africa": { population: [100, 200, 300], years: [1990, 2000, 2010]},
    "Asia": { population: [100, 200, 300], years: [1990, 2000, 2010]}
  }
  '''
  #Creates an empty dictionary that will store population data for each continent.
  output = {}
  #Actions to take with the data
  with open(filename, 'r') as csvfile:
    #Convert file to a Python Dictionary
    reader = csv.DictReader(csvfile)
    #Loop through each line in reader
    for line in reader:
      #Convert data to integer to be able to show in plot
      continent = line['continent']
      year = int(line['year'])
      population = int(line['population'])
      #Check if the continent exists in the dictionary
      if continent not in output:
        #Initialize an entry for the new continent
        output[continent] = {'population': [], 'years': []}
      #Store the population and year data
      #The population and year from the current CSV row are added to the respective lists for that continent
      output[continent]['population'].append(population)
      output[continent]['years'].append(year)

  return output

#Generate the population plots from a dictionary
def generate_population_plots_from_dictionary(population_dictonary):
  #Loop through each continent
  for continent in population_dictonary:
    #Define X and Y variables
    years = population_dictonary[continent]['years']
    population = population_dictonary[continent]['population']
    #Plot with X & Y axis
    plt.plot(years, population, label=continent, marker="o", alpha=0.5)
   
  #Plot Details
  plt.title("Internet Population per continent")
  plt.xlabel("Year")
  plt.ylabel("Internet users (in billion users)")
  plt.grid(True)
  plt.tight_layout()
  plt.legend()
  plt.show()

#Create a variable to identify the file
filename = 'data.csv'

# Display internet population in a plot
population_per_continent = generate_population_dictionary_from_csv(filename)
generate_population_plots_from_dictionary(population_per_continent)
