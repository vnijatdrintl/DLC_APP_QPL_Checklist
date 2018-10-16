#import all the packages
import pandas as pd

#later use tkinter's filedialog to get all paths
qpl='U:\\DLC\\app_qpl_checklist\\qpl_all_products_9-6-2018.csv'
#app_tracker='U:\\DLC\\app_qpl_checklist\\DLC-APPS-2018-09-17_AMS.xlsx'
checklist='U:\\DLC\\app_qpl_checklist\\XXXXXX PL_Checklist_V4.3_8-23-2018.xlsx'

def qpl(file_path):

    global df
    n=0
    for subdf in pd.read_csv(file_path,chunksize=10000):
        if n==0:
            df=subdf[subdf['Manufacturer']=='ABOVE ALL LIGHTING INC.']
        elif n!=0:
            df.append(subdf[subdf['Manufacturer']=='ABOVE ALL LIGHTING INC.'])
        n+=1
    df=df.drop_duplicates()
    df=df.reset_index()
    df=df.drop(['index'],axis=1)

    return df

#get manufacturer's name
# only read the manufacturer column
def getManufacturers(file_path):

    manufacturers=pd.read_csv(file_path,usecols=['Manufacturer'])
    manufacturers=manufacturers.drop_duplicates()

    manufacturers=sorted(list(manufacturers.Manufacturer),key=str.lower)

    return manufacturers
