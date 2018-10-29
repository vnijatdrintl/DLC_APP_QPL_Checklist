#import all the packages
import pandas as pd

def app_tracker(file_path,manufacturer):

    #get data
    xls=pd.ExcelFile(file_path)
    df=pd.read_excel(file_path,sheet_name='Applications')
    df=df[df['Manufacturer']==Manufacturer]
    df=df.drop_duplicates()
    df=df.reset_index()
    df=df.drop(['index'],axis=1)

    return df
