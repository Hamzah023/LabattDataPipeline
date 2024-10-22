import pandas as pd
import datasetDownloadScript as datasetDownloadScript
import inspectData as inspectData
import cleanData as cleanData
import connectToSnowflake as connectToSnowflake

df = pd.read_csv('../data/drinks.csv') #this reads the csv file and saves it in a pandas dataframe 

keepIn = True

while keepIn:

    print("Press 1 to download the dataset")
    print("Press 2 to inspect the dataset")
    print("Press 3 to clean the dataset")
    print("Press 4 to connect to Snowflake")
    print("Press 5 to exit")
    print("Enter your choice: ")
    inputValue = input()

    if inputValue == '1':
        datasetDownloadScript.datasetDownload()

    elif inputValue == '2':
        inspectData.inspectData(df)

    elif inputValue == '3':
        df = cleanData.cleanData(df)

    elif inputValue == '4':
        print("Connecting to Snowflake")
        connectToSnowflake.connectToSnowflake(df)

    elif inputValue == '5':
        keepIn = False



