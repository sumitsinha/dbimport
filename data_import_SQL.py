#Importing required packages
import numpy as np
import pandas as pd
from numpy import zeros, newaxis
import psycopg2
from sqlalchemy import create_engine
import zipfile  
import os
from open3d import *
from numpy import zeros, newaxis
#%%
#establish database connection and import to dataframe (change database name)
def databaseimport():
    engine = create_engine('postgresql://postgres@localhost:5432/IPQI')
    df = pd.read_sql_query('select * from "defect_all"',con=engine)
    return df

#Manipulate Dataframe to Numpy Array
def dataframe_to_numpy_array(df):
   
   for i in range(max(df['index'])):
        df_filtered = df[df['index'] == i+1]
        del df_filtered['index']
        df_filtered=df_filtered.values
        df_filtered=df_filtered[newaxis,:,:]
        if(i==0):
            final_dataset=df_filtered
        if(i>0):
            final_dataset=np.concatenate((final_dataset,df_filtered))
   return final_dataset