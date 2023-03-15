# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 20:52:19 2023

@author: Carlota
"""
import os
import argparse
import matplotlib.pyplot as plt
import mvn
from load_mvnx import load_mvnx
from tqdm import tqdm
from mvnxtodict import mvnx2dict
import pickle
import os

# Puede que tengas que modificar este path. 
data_folder = 'Documents/MovellaBiomechanicsChallenge/data/'

for folder_name in os.listdir(data_folder):
    mvnx_folder = data_folder + folder_name + '/' + 'MVNX/'
    for file_name in os.listdir(mvnx_folder):
            file_path = mvnx_folder + file_name           
            mvnx_file = load_mvnx(file_path)
            mvnx_dict = mvnx2dict(mvnx_file)
            
            subject_folder = data_folder + folder_name 
            pkl_folder = subject_folder + '/' + 'PKL'
            if not os.path.exists(pkl_folder):
                os.makedirs(pkl_folder)
            pkl_name = folder_name + '_' + file_name.replace('_round.mvnx', '') + '.pkl'
            pkl_path = pkl_folder + '/' + pkl_name
            # create a binary pickle file 
            f = open(pkl_path,"wb")
            # write the python object (dict) to pickle file
            pickle.dump(mvnx_dict,f)
            # close file
            f.close()



'''
# TO LOAD THE FILE
with open(path_to_pkl, 'rb') as f:
    data = pickle.load(f)
'''