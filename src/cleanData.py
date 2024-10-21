import pandas as pd

def cleanData(df):

    #df = pd.read_csv('data/drinks.csv') #this reads the csv file and saves it in a pandas dataframe 

    print("Here is the missing values in each column of the raw dataset: \n",df.isnull().sum().to_string()) #this prints the number of missing values in each column, the isnull() function returns a boolean dataframe with True for missing values and False for non-missing values and then sum function sums the number of True values in each column

    if (df.isnull().sum() == 0).all(): #this checks if there are any missing values in the dataset if isnull().sum() == 0 that means that there are no true values, and all checks each column
        #the all() function checks if all the values in the array are True
        print('No missing values in the dataset\n')
    else:
        print('Missing values found in the dataset:\n')
        df = df.dropna()

    df = df.rename(columns = {'country' : 'Country', 'beer_servings': 'Beer', 'spirit_servings': 'Spirits', 'wine_servings': 'Wine', 'total_litres_of_pure_alcohol': 'Total_litres_of_pure_alcohol'})


    print("Here is the cleaned dataset: \n", df.to_string())

    return df
  