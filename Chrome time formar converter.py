from pyautogui import *
import pyautogui
import datetime
import time
import keyboard
import random
import win32api, win32con
import sqlite3
import pandas
import os
import shutil
import time
import pandas as pd
from datetime import datetime

if pyautogui.locateOnScreen('QUIZ NAV.png') != None:
    date = datetime.now()
    dateString = date.strftime("%Y-%m-%d %H:%M:%S")


    def date_to_webkit(date_string):
        epoch_start = datetime(1601, 1, 1)
        date_ = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
        diff = date_ - epoch_start
        seconds_in_day = 60 * 60 * 24
        return '{:<017d}'.format(
            diff.days * seconds_in_day + diff.seconds + diff.microseconds)


    print(date_to_webkit(dateString))

if pyautogui.locateOnScreen('SUMMARY.png') != None:
    user = os.getlogin()
    urls = []
    titles = []
    visit_time = []
    chrome_time = []
    source_file = "C:/Users/" + user + "/AppData/Local/Google/Chrome/User Data/Default/History"
    destination_file = "C:/Users/" + user + "/Downloads/History"

    time.sleep(1)  # wait to update the history file
    shutil.copy(source_file, destination_file)

    con = sqlite3.connect("C:/Users/" + user + "/Downloads/History")

    times = "13294397690442982"

    cursor = con.execute(
        "SELECT url, title, datetime(last_visit_time / 1000000 + (strftime('%s', '1601-01-01')), 'unixepoch', 'localtime'), last_visit_time FROM urls "
        "WHERE last_visit_time >= " + times + " ORDER BY last_visit_time")
    for row in cursor:
        urls.append(row[0])
        titles.append(row[1])
        visit_time.append(row[2])
        chrome_time.append(row[3])

        df = pandas.DataFrame({'URL': urls,
                                'Title': titles,
                                'Visit time': visit_time,
                                'Chrome time': chrome_time})

    df.to_csv('testings2.csv', encoding='utf-8', index=False)
    con.close()


df = pd.read_csv('testings2.csv')
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

new_col = duration
data_new = pd.read_csv('testings2.csv')
data_new['Duration'] = pd.Series(new_col)
data_new = data_new.fillna(0)
data_new.to_csv('last.csv', encoding='utf-8', index=False)

data = pd.read_csv('last.csv')
data.drop('Chrome time', inplace=True, axis=1)
data.to_csv('testings2.csv', encoding='utf-8', index=False)




