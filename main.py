from datetime import datetime
import sqlite3
import pandas
import shutil
import time
import pandas as pd
import csv
from tkinter import *
from tkinter import ttk
import tkinter
from google.cloud import vision
from PIL import Image
import cv2
import numpy as np
import os
import pyautogui



a = 1
b = 1


def date_to_webkit(date_string):
    epoch_start = datetime(1601, 1, 1)
    date_ = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
    diff = date_ - epoch_start
    seconds_in_day = 60 * 60 * 24
    return '{:<017d}'.format(diff.days * seconds_in_day + diff.seconds + diff.microseconds)

while a == 1:
    if pyautogui.locateOnScreen('QUIZ NAV.png', region=(1470,250,300,300), grayscale=True) != None:
        date = datetime.now()
        dateString = date.strftime("%Y-%m-%d %H:%M:%S")
        a = 2
        chromeTime = date_to_webkit(dateString)
        print("START AT " + dateString)

while b == 1:
    if pyautogui.locateOnScreen('COMPLETE.png', region=(50,200,600,350), grayscale=True) != None or pyautogui.locateOnScreen('COMPLETE2.png', region=(400,200,300,300), grayscale=True) != None:
        b = 2
        user = os.getlogin()
        urls = []
        titles = []
        visit_time = []
        chrome_time = []
        source_file = "C:/Users/" + user + "/AppData/Local/Google/Chrome/User Data/Default/History"
        destination_file = "C:/Users/" + user + "/Downloads/History"

        time.sleep(5)
        shutil.copy(source_file, destination_file)

        con = sqlite3.connect("C:/Users/" + user + "/Downloads/History")

        sub = 28805000000
        times = (int(chromeTime)) - sub

        cursor = con.execute(
            "SELECT url, title, datetime(last_visit_time / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch', 'localtime'), last_visit_time FROM urls "
            "WHERE last_visit_time >= " + str(times) + " ORDER BY last_visit_time")
        for row in cursor:
            urls.append(row[0])
            titles.append(row[1])
            visit_time.append(row[2])
            chrome_time.append(row[3])

            df = pandas.DataFrame({'URL': urls,
                                   'Title': titles,
                                   'Visit time': visit_time,
                                   'Chrome time': chrome_time})

        df.to_csv('USER_ACTIVITY.csv', encoding='utf-8', index=False)
        con.close()

df = pd.read_csv('USER_ACTIVITY.csv')
numline = len(df)
x = 0
row1 = 1
row2 = row1 - 1
duration = []

while x < numline - 1:
    int1 = df.iloc[row1, 3]
    int2 = df.iloc[row2, 3]
    x += 1
    row1 += 1
    row2 += 1

    seconds = ((int1 - int2) / 1000000)
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    duration += [("%d:%02d:%02d" % (hour, minutes, seconds))]

image = pyautogui.screenshot(region=(1700, 100, 200, 50))
image.save('C:/Users/'+ user +'/Desktop/user.jpg')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'D:\Downloads\chromatic-trees-342514-99b2f35a2213.json'
img = np.asarray(Image.open('C://Users//' + user + '//Desktop//user.jpg'))
success, encoded_image = cv2.imencode('.jpg', img)
roi_image = encoded_image.tobytes()
client = vision.ImageAnnotatorClient()
image = vision.Image(content=roi_image)
response = client.text_detection(image=image)
texts = response.text_annotations
result = texts[0].description.strip()

new_col = duration
data_new = pd.read_csv('USER_ACTIVITY.csv')
data_new['cheat'] = data_new['URL'].apply(lambda x: 'kimjejl' not in str(x) )
data_new['Duration'] = pd.Series(new_col)
data_new = data_new.fillna(0)
data_new.to_csv('USER_ACTIVITY.csv', encoding='utf-8', index=False)

new_col = [result]*len(data_new)
data_new = pd.read_csv('USER_ACTIVITY.csv')
data_new['Username'] = pd.Series(new_col)
data_new = data_new.fillna(0)
data_new.to_csv('USER_ACTIVITY.csv', encoding='utf-8', index=False)

data = pd.read_csv('USER_ACTIVITY.csv')
data.drop('Chrome time', inplace=True, axis=1)
data.to_csv('USER_ACTIVITY.csv', encoding='utf-8', index=False)

data = pd.read_csv('USER_ACTIVITY.csv')
df = data.drop(data.index[-1])
df.to_csv('USER_ACTIVITY '+result+'.csv', encoding='utf-8', index=False)

root = tkinter.Tk()
root.title("User Activity ("+ result+")")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (0.50 * w, 0.4 * h))


def displayontowindow():
    frame = Frame(root, width=300, height=200, bg="light grey")

    frame = ttk.Frame(root, width=200, height=150)

    # Canvas creation with double scrollbar
    hscrollbar = ttk.Scrollbar(frame, orient=tkinter.HORIZONTAL)
    vscrollbar = ttk.Scrollbar(frame, orient=tkinter.VERTICAL)
    sizegrip = ttk.Sizegrip(frame)
    canvas = tkinter.Canvas(frame, bd=0, highlightthickness=0, yscrollcommand=vscrollbar.set,
                            xscrollcommand=hscrollbar.set)
    vscrollbar.config(command=canvas.yview)
    hscrollbar.config(command=canvas.xview)
    subframe = ttk.Frame(canvas)

    with open("USER_ACTIVITY.csv", newline="") as file:
        reader = csv.reader(file)

        r = 0
        for col in reader:
            c = 0
            for row in col:
                label = tkinter.Label(subframe, width=60, height=1,
                                      text=row, relief=tkinter.RIDGE)
                label.grid(row=r, column=c)
                c += 1
            r += 1

    subframe.pack(fill=tkinter.BOTH, expand=tkinter.TRUE)
    hscrollbar.pack(fill=tkinter.X, side=tkinter.BOTTOM, expand=tkinter.FALSE)
    vscrollbar.pack(fill=tkinter.Y, side=tkinter.RIGHT, expand=tkinter.FALSE)
    sizegrip.pack(in_=hscrollbar, side=BOTTOM, anchor="se")
    canvas.pack(side=tkinter.LEFT, padx=5, pady=5, fill=tkinter.BOTH, expand=tkinter.TRUE)
    frame.pack(padx=5, pady=5, expand=True, fill=tkinter.BOTH)

    canvas.create_window(0, 0, window=subframe)
    root.update_idletasks()  # update geometry
    canvas.config(scrollregion=canvas.bbox("all"))
    canvas.xview_moveto(0)
    canvas.yview_moveto(0)

displayontowindow()

root.mainloop()