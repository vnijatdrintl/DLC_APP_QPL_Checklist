import pandas as pd
import tkinter as tk
from tkinter import messagebox as mBox
from tkinter import filedialog
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows
import xlsxwriter
import app_tracker
import qpl
import time
import os

start=time.time()

checklist='U:\\DLC\\app_qpl_checklist\\XXXXXX PL_Checklist_V4.3_8-23-2018 - Copy.xlsx'
root = tk.Tk()
root=root.withdraw()

qpl_file_path=filedialog.askopenfilename(initialdir='U:\\DLC\\app_qpl_checklist')
app_tracker_file_path=filedialog.askopenfilename(initialdir='U:\\DLC\\app_qpl_checklist')

qpl_df=qpl.qpl(qpl_file_path)
app_tracker_df=app_tracker.app_tracker(app_tracker_file_path)


save_file_path=filedialog.askopenfilename(initialdir='U:\\DLC\\app_qpl_checklist')
# #defaultextension=".xlsx"
# book=openpyxl.load_workbook(save_file_path)
#
# xls=pd.ExcelFile(save_file_path)
# writer = pd.ExcelWriter(xls,engine='openpyxl')
# #,engine='xlsxwriter'
# writer.book=book
# writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
# qpl_df.to_excel(writer, 'OEM Products', index=False)
# #writer.save()
#
# app_tracker_df.to_excel(writer, 'OEM Applications', index=False)
# writer.save()

with open(save_file_path,'a'):
    book=openpyxl.load_workbook(save_file_path)
    writer = pd.ExcelWriter(save_file_path,engine='openpyxl')
    writer.book=book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
    qpl_df.to_excel(writer, 'OEM Products', index=False)
    app_tracker_df.to_excel(writer, 'OEM Applications', index=False)
    writer.save()

end=time.time()
print(end-start)
