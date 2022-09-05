### preperation ###
# install neede pacakge - pandas and give it the shorter name as "pd"
import pandas as pd
# install other useful packages 
import datetime as dt 
import uuid # create unique identifier 
import numpy as np # for missing values, installed in pandas already


### Load data into python ###
df =  pd.read_csv('data\School_Learning_Modalities.csv')


### ptint counts of columns & rows of the dataset
df.shape # (row: 741876,column: 9)


### provide a print out of the column names
list(df)


### clean the column names
# rename var 
df = df.rename(columns={
    'District NCES ID':'District ID',
    'Week':'Date',
    'Student Count':'Student Number',
    'ZIP Code':'ZIP'
    })
# replace all special characters with white space
df.columns = df.columns.str.replace('[^A-Za-z0-9]+', ' ')
# then replace all white spaces with "_"
df.columns = df.columns.str.replace(' ', '_')
# change all var names into lower case
df.columns = df.columns.str.lower()
# check changed var names
df.columns 


### clean the strings that might exist within each column ???
# replacing empty or white space cells with NaN
df.replace(to_replace='', value=np.nan, inplace=True)
df.replace(to_replace=' ', value=np.nan, inplace=True)


### assess white space or special characters 
# remove all whitespace for values within each string var
df['district_name'] = df['district_name'].str.strip()
df['date'] =df['date'].str.strip()
df['learning_modality'] = df['learning_modality'].str.strip()
df['city'] = df['city'].str.strip()
df['state'] = df['state'].str.strip()

# remove all special characters and whitespace ' ' from each string var
df['district_name'] = df['district_name'].str.replace('[^A-Za-z0-9]+', '')
df['date'] = df['date'].str.replace('[^A-Za-z0-9]+', '')
df['learning_modality'] = df['learning_modality'].str.replace('[^A-Za-z0-9]+', '')
df['city'] = df['city'].str.replace('[^A-Za-z0-9]+', '')
df['state'] = df['state'].str.replace('[^A-Za-z0-9]+', '')


### convert the colum types to the correct types
# check all var types
df.dtypes
# change the type of "date" var to datetime from object
# check "date" var format/ how data look like in this var
print(df['date'])
# conevrt "date" to datetime var
df['date'] = pd.to_datetime(df['date'], format='%m%d%Y%H%M%S%p') # format needs to align with how data look like in var, no space or "/" in this case
print(df['date'].dtypes)

# change 'student_number' var into integer 
# assign '-999' to missing values in 'student_number' - check if -999 is integer
pd.api.types.is_integer(-999) # return 'True' means given object is integer
df['student_number'] = df['student_number'].fillna(-999)
# convert 'student_number' from float to int
df['student_number'] = df['student_number'].astype(int)
# check 'student_number' type
print(df['student_number'].dtypes)


### look for duplicate rows and remove them
# delete duplicated rows 
df.drop_duplicates() # now dataset has [741876 rows x 9 columns]

### assess missingness (count of missing values per column)
df.isnull().sum() # no missing detected because in previous step, already convert missing values in 'student_number' to -999

### new data field - create a new column called "modality_inperson" based on existing var "learning_modality"
# "in-person" = true; "remote"/"hybrid" = false
df['modality_inperson'] = np.where(df['learning_modality']=='in-person', True, False)
df['modality_inperson']
# show all var types
df.dtypes


### save the modified dataset to a new folder "data/modified"
df.to_csv('data\modified.csv')
