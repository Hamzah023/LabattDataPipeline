import os;
import zipfile;
import kaggle;

dataSet = 'codebreaker619/alcohol-comsumption-around-the-world'
kaggle.api.dataset_download_files(dataSet, path = 'data/', unzip = True)

print('Data downloaded successfully!')