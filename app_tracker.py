#import all the packages
import pandas as pd

#app_tracker='U:\\DLC\\app_qpl_checklist\\DLC-APPS-2018-09-17_AMS.xlsx'

def app_tracker(file_path):

    #get data
    xls=pd.ExcelFile(file_path)
    df=pd.read_excel(file_path,sheet_name='Applications')
    df=df[df['Manufacturer']=='ABOVE ALL LIGHTING INC.']
    df=df.drop_duplicates()
    df=df.reset_index()
    df=df.drop(['index'],axis=1)

    return df
