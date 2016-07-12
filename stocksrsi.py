import getfile
import getaverages
import sys, subprocess

#don't forget py2app

# do it in one line
# format as mm/dd/yyyy or intelligent
# startdate = raw_input("Enter a start date in the form mm/dd/yyyy (e.g. 04/07/2014) \n")
#split by slash, add the zero
# check if month > 12 or day > 31 or year > today's date.
#input in different forms.s
#add chosen ticker or ability to find


csvfile= getfile.getfile()



# getaverages.averagegains(filename)
# getaverages.averagelosses(filename)


def openfile():
    opener = "open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, csvfile])


getaverages.readfile(csvfile)

# def writefile
#
# def closefile

# openfile()



