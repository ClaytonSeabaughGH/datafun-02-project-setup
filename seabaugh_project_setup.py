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
def create_prefixed_folders(folder_list, prefix: str) -> None:

# Function 4: A While Loop that creates folders periodically
def create_folders_periodically(duration):


# Define Main Function

# Conditional Script Execution
