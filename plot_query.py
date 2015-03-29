# this will plot results from the age-score relation query
import numpy as np
import matplotlib.pyplot as p

# you'll likely need to modify this, just check the last line of the
#  CSV you've gotten and see what number is there, then edit accordingly
days = 1589
avgScore = np.zeros(days+1)
daysSince = np.linspace(0,days,days+1)
avgByMonth = np.zeros(days/30)

# function to read the file
def readFile(fname):
    fp = open(fname,"r")
    unused = fp.readline()
    for line in fp:
        x,f1 = line.split()
        avgScore[int(x)] = float(f1)
    fp.close()
    
# this is how I saved it, modify it as you need it
filename = "Age-Score_QueryResults.csv"
readFile(filename)

# this was to see the average scores at "late times" that I quoted
aUp = (avgScore[300:] >= +2)
aDn = (avgScore[300:] <= -2)
aZr = (avgScore[300:] == 0)

print float(aUp.sum())
print float(aDn.sum())
print float(aZr.sum())

# find 30 day averages
for i in range(0,days/30):
    temp = 0
    for j in range(i,i+30):
        temp += avgScore[j]
    avgByMonth[i] = temp/30.0
avgMonths = np.linspace(0,51,52)

# hack trendline
z = np.polyfit(daysSince, avgScore,1)
w = np.poly1d(z)

# plot the data
p.clf()
p.figure(1)
p.scatter(daysSince, avgScore, c=(avgScore-5))
p.plot(daysSince, w(daysSince), 'r--', linewidth=3)
p.xlabel('Days between Q & A')
p.ylabel('Average score')
# you can be selective about your ranges too
p.xlim([0,days])
# this line is for the zoomed-in data table. Comment out with # if you want
#  the unadultered data
p.ylim([-5,5])
p.show()

# plot the monthly averages
p.figure(2)
p.scatter(avgMonths, avgByMonth)
p.xlabel('Months between Q & A')
p.ylabel('Average score')
p.show()

