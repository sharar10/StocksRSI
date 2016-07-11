import urllib
import subprocess, sys
import os

ticker = str(raw_input("Enter a ticker \n"))
# do it in one line
# format as mm/dd/yyyy or intelligent
# startdate = raw_input("Enter a start date in the form mm/dd/yyyy (e.g. 04/07/2014) \n")
#split by slash, add the zero
# check if month > 12 or day > 31 or year > today's date.


#subtract one from month
monthstart = str(int(raw_input("Enter your start month \n")) - 1)
daystart = str(int(raw_input("Enter your start month \n")))
yearstart = str(raw_input())
monthfinish = str(int(raw_input("Enter your start month \n")) - 1)
dayfinish = str(int(raw_input("Enter your start month \n")))
yearfinish = str(raw_input())


url = "http://real-chart.finance.yahoo.com/table.csv?s=" + ticker + "&a=" + monthstart + "&b=" + daystart + "&c=" + yearstart + "&d=" + monthfinish + "&e=" + dayfinish + "&f=" + yearfinish + "&g=d&ignore=.csv"
print(url)
#retreive url
filefromurl = urllib.URLopener()
filename = str(ticker + ".csv")
filefromurl.retrieve(url, filename)

#open file with this
opener ="open" if sys.platform == "darwin" else "xdg-open"
subprocess.call([opener, filename])


#works




##def parsedate(startmonth,startdate, yearstart, ):
# ticker = str(raw_input("Enter a ticker \n"))
# monthstart = str(int(raw_input("Enter your start month \n")) - 1)
# daystart = str(int(raw_input("Enter your start month \n")))
# yearstart = str(raw_input())
# monthfinish = str(int(raw_input("Enter your start month \n")) - 1)
# dayfinish = str(int(raw_input("Enter your start month \n")))
# yearfinish = str(raw_input())
#    return url