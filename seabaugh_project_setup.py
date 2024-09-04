'''Data Project No 2!!

This project demonstrates proficiency in loops, project folder creation using pathlib, and importing modules.

This module provides functions for creating a series of project folders
'''

########## Import Modules ############


#Import modules from python libraries
import pathlib

#Import local modules
import seabaugh_utils

########## Declare Global Variables #########



#Create a path object
project_path = pathlib.Path.cwd()

# Define the new sub folder path
data_path = project_path.joinpath('data')

# Create new if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_okay=True)


###### Define functions for folder creation ########



# Function 1: Generates folders for a given range (years)
def create_folders_for_range(start_year, end_year: int) -> None:


# Function 2: Creates folders from a list of names 
def create_folders_from_list(folder_list: int) -> None:

# Function 3: Creates prefixed folders by combinging a list of names with a prefix
def create_prefixed_folders(folder_list: list, prefix: str) -> None:

# Function 4: A While Loop that creates folders periodically
def create_folders_periodically(duration):


########### Define Main Function ###########

def main():
''' Main function to demonstrate module capabilities. '''

# Print byline from imported module
    print(f"Byline: {seabaugh_utils.byline}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'data-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # Add options e.g., to force lowercase and remove spaces 
    # to one or more of your functions (e.g. function 2) 
    regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)




# Conditional Script Execution
