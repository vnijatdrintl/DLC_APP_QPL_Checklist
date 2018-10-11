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
# global df
# n=0
# for subdf in pd.read_csv(qpl,chunksize=10000):
#     if n==0:
#         df=subdf['Manufacturer'].drop_duplicates()
#     elif n!=0:
#         df.append(subdf['Manufacturer'].drop_duplicates())
#     n+=1
# df=df.drop_duplicates()
# df=df.sort_values()
# df=df.reset_index()
# df=df.drop(['index'],axis=1)

#option 1: find manufacturer
#df[df['Manufacturer'].str.contains('Shenzhen')]

#option 2: convert the data frame to a list and use a dropdown menu to select
#manufacturer
