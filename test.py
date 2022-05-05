from csv import writer
from datetime import datetime
import sqlite3
import pandas
from pandas import *
import shutil
import time
import pandas as pd
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
    if pyautogui.locateOnScreen('QUIZ NAV.png', grayscale=True) != None:
        date = datetime.now()
        dateString = date.strftime("%Y-%m-%d %H:%M:%S")
        a = 2
        chromeTime = date_to_webkit(dateString)
        print("START AT " + dateString)

while b == 1:
    if pyautogui.locateOnScreen('COMPLETE.png', grayscale=True) != None:
        date = datetime.now()
        dateEnd = date.strftime("%Y-%m-%d %H:%M:%S")
        endTime = date_to_webkit(dateEnd)
        print("COMPLETED AT " + dateEnd)
        b = 2
        user = os.getlogin()
        urls = []
        titles = []
        visit_time = []
        chrome_time = []
        source_file = "C:/Users/" + user + "/AppData/Local/Google/Chrome/User Data/Default/History"
        destination_file = os.path.join("history", "History")

        time.sleep(5)
        shutil.copy(source_file, destination_file)

        con = sqlite3.connect(destination_file)

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


new_col = duration
data_new = pd.read_csv('USER_ACTIVITY.csv')
data_new['Duration'] = pd.Series(new_col)
data_new['Other Activities'] = data_new['URL'].apply(lambda x: 'pre-final-thesis' not in str(x) )
data_new = data_new.fillna(0)
data_new.to_csv('USER_ACTIVITY.csv', encoding='utf-8', index=False)


data = pd.read_csv('USER_ACTIVITY.csv')
data.drop('Chrome time', inplace=True, axis=1)
data.to_csv('USER_ACTIVITY.csv', encoding='utf-8', index=False)

data = pd.read_csv('USER_ACTIVITY.csv')
df = data.drop(data.index[-1])
df.to_csv('USER_ACTIVITY.csv', encoding='utf-8', index=False)

seconds = ((int(endTime) - int(chromeTime)) / 1000000)
seconds = seconds % (24 * 3600)
hour = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
totalDuration = ("%d:%02d:%02d" % (hour, minutes, seconds))

data = read_csv('USER_ACTIVITY.csv')
url = data['Other Activities'].tolist()
count = 0
with open('USER_ACTIVITY.csv', 'r') as f:
    for line in f:
        count += 1

from collections import Counter
counts = Counter(url)
true = counts[True]
false = counts[False]
percentage = (true/count)*100

resultss = 'TOTAL:'+str(count), 'TOTAL:'+str(count), dateString+' to '+dateEnd, 'Total Duration: '+totalDuration, 'Percentage of other Activites: '+str(percentage)+'%'

with open('USER_ACTIVITY.csv', 'a', newline='') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(resultss)
    f_object.close()
