# Author: Arey Ferrero Ramos.
# Date: March 24, 2023. Version: 1
# Description: This script calculates the alpha diversity of a species of vertebrate from those used in the study.
#   Parameters:
#       -A file that contains a table with the number of species per genus in every individual of that species of
#        vertebrate used in that study.
#   Output:
#       -The alpha diversity of the species of vertebrate.

import pandas as pd
import math
import sys
import os

if len(sys.argv) != 2:
    print("Error: The number of parameters is incorrect. The only parameter has to be a file.")
    exit()

if not os.path.isfile(sys.argv[1]):
    print("Error: The input must be a file corresponding to a species of vertebrate.")
    exit()

df_vertebrate = pd.read_table(sys.argv[1], delimiter=' ', header=0)
acum_diversity = 0
num_individuals = 0

for individual in df_vertebrate:
    num_bacterial_species_per_individual = 0
    for num_bacterial_species_per_genus in df_vertebrate[individual]:
        num_bacterial_species_per_individual += num_bacterial_species_per_genus
    acum_diversity += num_bacterial_species_per_individual * math.log(num_bacterial_species_per_individual)
    num_individuals += 1

print("Alpha_diversity: "+str(round(acum_diversity / num_individuals))+" species.")