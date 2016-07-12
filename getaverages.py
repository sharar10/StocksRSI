#rename file calculatebut keep as getaverages for now
adj, date, openprice, high, low, close, volume = [], [], [], [], [], [], []
def readfile(file) :
    with open(file) as f:
        #date,openprice,high,low,close,volume,

        for line in f:
            words = line.split(",")
            date.append(words[0])
            openprice.append(words[1])
            high.append(words[2])
            low.append(words[3])
            close.append(words[4])
            volume.append(words[5])
            adj.append(words[6].rstrip('\n'))
        del adj[0]
        calculatechange(adj)

def calculatechange(adj):
    change, gains, losses = [], [], []
    for i in range(0,len(adj)-1):
        x= float(adj[i])
        y= float(adj[i+1])
        number = y-x
        change.append(number)
    change.insert(0,0)

    for values in change:
        if values > 0:
            gains.append(values)
            losses.append(0)
        elif values < 0:
            losses.append(values)
            gains.append(0)
        elif values == 0:
            gains.append(values)
            losses.append(values)
    averagegainslosses(gains,losses)

def sumindices(list,index):
    generatedvalue =0
    for i in range(index,index+14):
        generatedvalue+=list[i]
    return generatedvalue/14

def averagegainslosses(gains,losses):
    averagegain,averageloss = [], []
    lengains= len(gains) -1
    for i in range(0,lengains-12):
        averagegain.append(sumindices(gains,i))
        averageloss.append(sumindices(losses, i))
    for i in range(0,14):
        averagegain.insert(0, 0)
        averageloss.insert(0, 0)
    findrs(averagegain,averageloss)

def findrs(averagegain,averageloss):
    rs = []
    for i in range(0,len(averagegain)-1):
        if (averagegain[i]==0 or averageloss[i]==0):
            rs.append(0)
        else:
            rs.append(averagegain[i]/averageloss[i])
    findrsi(rs)


def findrsi(rs):
    rsi=[]
    for i in range(0,len(rs)):
        rsivalue = 100 - (100/(1+rs[i]))
        rsi.append(rsivalue)
        print(rsivalue)
    #addheaders()

# def addheaders(list,columnhead):
#     list.insert(0,columnhead)
#
# def writefile: