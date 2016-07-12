#getfile.py parses the url and downloads the file
import urllib
import string



def getfile():
    ticker = str(raw_input("Enter a ticker \n"))

    # subtract one from month
    #enter a startdate in the form mm/dd/yyyy
    startdate = raw_input("Enter a start date in the form mm/dd/yyyy \n e.g. 05/10/2015 \n")
    enddate = raw_input("Enter an end date in the form mm/dd/yyyy \n e.g. 03/10/2016 \n")

    monthstart, daystart, yearstart = startdate.split("/")
    monthfinish, dayfinish, yearfinish = enddate.split("/")

    monthstart = str(int(monthstart) - 1)
    monthfinish = str(int(monthfinish) - 1)

    #some error handling
    startdayvalue = 365*yearstart + 30 * monthstart + daystart
    enddayvalue = 365*yearfinish + 30 * monthfinish + dayfinish


    filename =""

    if enddayvalue > startdayvalue:
        url = "http://real-chart.finance.yahoo.com/table.csv?s=" + ticker + "&a=" + monthstart + "&b=" + daystart + "&c=" + yearstart + "&d=" + monthfinish + "&e=" + dayfinish + "&f=" + yearfinish + "&g=d&ignore=.csv"
       # retrieve url
        filefromurl = urllib.URLopener()
        filename = str(ticker+ ".csv")
        filefromurl.retrieve(url, filename)
        return filename
        print("Successfully generated file from " + startdate + " to " + enddate)
    else:
        print("Please re-check your dates")
        getfile()

