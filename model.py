#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 06:58:29 2020

@author: jason-bourne
"""

import warnings

warnings.filterwarnings( "ignore" )

import pandas as pd

# data cleaning

df = pd.read_csv( 'raw_cardio.csv', sep = ';')

df.drop( 'id', axis = 1, inplace = True )

df.drop_duplicates( inplace = True )

X = df.iloc[:,:11]

Y = df.iloc[:,11:]

# train and test setting

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size = 0.2 )

# model training

from sklearn.neighbors import KNeighborsClassifier

hx = KNeighborsClassifier( n_neighbors = 9, weights = 'uniform', algorithm = 'brute' )

hx.fit( X_train, Y_train )

# save the model

import pickle

pickle.dump( hx, open( 'model.pkl','wb' ) ) 