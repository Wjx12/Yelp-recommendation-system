# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 14:44:46 2018

@author: YTZzz
"""
import pandas as pd
import cf_method as cf
from data_preparation import *

RMSE_baseline = cf.base_line(train_matrix, test_stars,train_stars)
RMSE_memory_based = cf.memory_based(train_matrix, test_stars, train_stars)
RMSE_item_based = cf.item_based(train_matrix, test_stars, train_stars)

