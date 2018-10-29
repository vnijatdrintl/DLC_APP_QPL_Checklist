import pandas as pd
import tkinter as tk
from tkinter import messagebox as mBox
from tkinter import filedialog
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows
import app_tracker, qpl, time, os

#start=time.time()

root = tk.Tk()
root.geometry('600x500')
root.title('DLC Application Tracker and QPL Checklist')

#root=root.withdraw()

qpl_file_path = tk.StringVar()
app_tracker_file_path = tk.StringVar()
save_file_path = tk.StringVar()
manufacturer=tk.StringVar()
manufacturers=[]

#qpl product list
def openQPLFile():

    global qpl_file_path
    global manufacturers

    qpl_file_path = filedialog.askopenfilename()
    pathLabel1.config(text=os.path.split(qpl_file_path)[1])

    manufacturers=qpl.getManufacturers(qpl_file_path)
    manufacturer=manufacturers[0]

    wMenu=tk.Label(root,justify=tk.CENTER,text='Choose a Manufacturer',font=18).pack()
    scrollbar=tk.Scrollbar(root)
    scrollbar.pack(side='right',fill='y')

    listbox=tk.Listbox(root)
    listbox.pack()

    for m in reversed(manufacturers):
        listbox.insert(0,m)

    listbox.config(yscrollcommand=scrollbar.set,width=0,height=0)
    scrollbar.config(command=listbox.yview)

w1=tk.Label(root,justify=tk.CENTER,text='QPL Checklist File',font=18).pack()

pathLabel1=tk.Label(root)
pathLabel1.pack()

wopen1=tk.Button(text='Open File', command=openQPLFile)
wopen1.pack()


#option menu
# wMenu=tk.Label(root,justify=tk.CENTER,text='Choose a Manufacturer',font=18).pack()
# popupmenu=tk.OptionMenu(root,manufacturer,*manufacturers)
# popupmenu.pack()


#Application Tracker
def openAppFile():

    global qpl_file_path

    app_tracker_file_path = filedialog.askopenfilename()
    pathLabel2.config(text=os.path.split(app_tracker_file_path)[1])

w2=tk.Label(root,justify=tk.CENTER,text='Application Tracker',font=18).pack()


pathLabel2=tk.Label(root)
pathLabel2.pack()

wopen2=tk.Button(text='Open File', command=openAppFile)
wopen2.pack()




root.mainloop()
# qpl_file_path=filedialog.askopenfilename(initialdir='U:\\DLC\\app_qpl_checklist')
# app_tracker_file_path=filedialog.askopenfilename(initialdir='U:\\DLC\\app_qpl_checklist')
#
# qpl_df=qpl.qpl(qpl_file_path)
# app_tracker_df=app_tracker.app_tracker(app_tracker_file_path)
#
#
# save_file_path=filedialog.askopenfilename(initialdir='U:\\DLC\\app_qpl_checklist')
#
with open(save_file_path,'a'):
    book=openpyxl.load_workbook(save_file_path)
    writer = pd.ExcelWriter(save_file_path,engine='openpyxl')
    writer.book=book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
    qpl_df.to_excel(writer, 'OEM Products', index=False)
    app_tracker_df.to_excel(writer, 'OEM Applications', index=False)
    writer.save()
#
# end=time.time()
# print(end-start)
