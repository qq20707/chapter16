import csv
from matplotlib import pyplot as plt 
from datetime import datetime

filename = 'sitka_weather_2014.csv'
#filename ='sitka_weather_07-2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	#print(header_row)

#for index,column_header in enumerate(header_row):
#	print(index,column_header)

	highs =[]
	dates =[]
	lows = []
	for row in reader:
		current_date = datetime.strptime(row[0],'%Y-%m-%d')
		dates.append(current_date)
		high = int(row[1])
		highs.append(high)

		low  = int(row[3])
		lows.append(low)
	#print(highs)
	#print(dates)

#绘制图形
fig = plt.figure(dpi=96,figsize=(10,6))
plt.plot(dates,highs)
plt.plot(dates,lows,c='red')
#
#plt.title("Daily high temperatures ,July 2014",fontsize=24)
plt.title("Daily high temperatures -2014 ",fontsize = 20)
plt.xlabel('',fontsize = 12)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)',fontsize = 12)
plt.tick_params(axis='both',which='major',labelsize=12)

plt.show()
