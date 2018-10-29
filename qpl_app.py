#import all the packages
import pandas as pd

def oemProducts(file_path, manufacturer):

    global df
    n=0
    for subdf in pd.read_csv(file_path,chunksize = 10000):
        if n==0:
            subdf = subdf[subdf['Manufacturer']==manufacturer]
            if subdf.shape[0]==0:
                continue
            df=subdf
        elif n!=0:
            df.append(subdf[subdf['Manufacturer']==manufacturer])
        n+=1
    df = df.drop_duplicates()
    df = df.reset_index()
    df = df.drop(['index'],axis=1)

    return df

def plProducts(file_path, manufacturer):

    global df
    n=0
    for subdf in pd.read_csv(file_path,chunksize = 10000):
        if n==0:
            subdf = subdf[subdf['Manufacturer']==manufacturer]
            if subdf.shape[0]==0:
                continue
            df=subdf
        elif n!=0:
            df.append(subdf[subdf['Manufacturer']==manufacturer])
        n+=1
    df = df.drop_duplicates()
    df = df.reset_index()
    df = df.drop(['index'],axis=1)

    return df

def app_tracker(file_path,manufacturer):

    #get data
    xls=pd.ExcelFile(file_path)
    df=pd.read_excel(file_path,sheet_name='Applications')
    df=df[df['Manufacturer']==manufacturer]
    df=df.drop_duplicates()
    df=df.reset_index()
    df=df.drop(['index'],axis=1)

    return df


#get manufacturer's name
# only read the manufacturer column
def getManufacturers(file_path):

    manufacturers = pd.read_csv(file_path,usecols=['Manufacturer'])
    manufacturers = manufacturers.drop_duplicates()

    manufacturers = sorted(list(manufacturers.Manufacturer),key=str.lower)

    return manufacturers
