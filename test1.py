from pandas import *

time1 =13293022515810692
time2 = 13293022530280102
time3 = 13293022545242313
time4 = 13293023008946639
time5 = 13293023009188352
data = read_csv("USER_ACTIVITY lann Francisco.csv")

url = data['Other Activities'].tolist()

seconds = ((time5 - time1) / 1000000)
seconds = seconds % (24 * 3600)
hour = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
totalDuration = ("%d:%02d:%02d" % (hour, minutes, seconds))
print(totalDuration)

