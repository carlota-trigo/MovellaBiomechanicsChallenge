# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 08:56:55 2023

@author: Carlota
"""

import os
import pickle

# Define the path to the parent folder containing the Px folders
data_folder = 'C:/Users/Carlota/Documents/MovellaBiomechanicsChallenge/data/'
# Define the number of rows and columns for the subplot grid
# Get a list of all Px folders and sort them in ascending order
px_folders = sorted([f for f in os.listdir(data_folder)])

macro_dict = {}
files = os.listdir(data_folder)
filtered_files = [f for f in files if f.startswith('P') and not f.endswith('.pkl')]
print(filtered_files)

for folder_name in filtered_files:
    print(folder_name)
    pkl_folder = data_folder + folder_name + '/' + 'PKL/'
    for file_name in os.listdir(pkl_folder):
        print(file_name)
        pkl_path = pkl_folder + file_name
        rnd = file_name.split("_")[-1].split(".")[0]
        with open(pkl_path, 'rb') as f:
            data_dict = pickle.load(f)
        
        macro_dict[folder_name] = {}
        macro_dict[folder_name][rnd] = {}
        macro_dict[folder_name][rnd] = data_dict
        print(file_name + 'saved')

print('Opening file ...')
f = open("C:/Users/Carlota/Documents/MovellaBiomechanicsChallenge/data/alldata.pkl","wb")
# write the python object (dict) to pickle file
print('Writing file...')
pickle.dump(macro_dict,f)
# close file
print('Closing file...')
f.close()


