#rename file calculatebut keep as getaverages for now
import os
adj, date, openprice, high, low, close, volume, change, gains, losses, averagegain, averageloss, rs, rsi = [], [], [], [], [], [], [], [], [], [], [], [], [], []
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
    for i in range(0,len(adj)-1):
        x= float(adj[i])
        y= float(adj[i+1])
        number = y-x
        change.append(str(number))
    change.insert(0,"0")

    for values in change:
        if float(values) > 0:
            gains.append(str(values))
            losses.append("0")
        elif float(values) < 0:
            losses.append(str(abs(float(values))))
            gains.append("0")
        elif float(values) == 0:
            gains.append(str(values))
            losses.append(str(values))
    averagegainslosses(gains,losses)

def sumindices(list,index):
    generatedvalue =0
    for i in range(index,index+14):
        generatedvalue+=float(list[i])
    return generatedvalue/14

def averagegainslosses(gains,losses):
    lengains= len(gains) -1
    for i in range(0,lengains-12):
        averagegain.append(str(sumindices(gains,i)))
        averageloss.append(str(sumindices(losses, i)))
    for i in range(0,14):
        averagegain.insert(0, "0")
        averageloss.insert(0, "0")
    findrs(averagegain,averageloss)

def findrs(averagegain,averageloss):
    for i in range(0,len(averagegain)-1):
        if (float(averagegain[i])==0 or float(averageloss[i])==0):
            rs.append("0")
        else:
            gainloss = float(averagegain[i])/float(averageloss[i])
            rs.append(str(gainloss))
    findrsi(rs)


def findrsi(rs):
    for i in range(0,len(rs)):
        rsivalue = (100 - (100/(1+float(rs[i]))))
        rsi.append(str(rsivalue)+" \n")
    #addheaders
    rsi.insert(0,"RSI value \n")
    rs.insert(0,"RS value")
    averagegain.insert(0,"Average gains")
    averageloss.insert(0, "Average losses")
    change.insert(0,"Change")
    gains.insert(0,"Gains")
    losses.insert(0,"Losses")
    adj.insert(0,"Adjusted")


def writefile(file):
    f = open(file, 'w')
    for x in range(0,len(rsi)-1):
        line = date[x] +"," + openprice[x] + "," + high[x]+","+low[x]+","+close[x]+","+volume[x]+","+adj[x]+","+str(change[x])+","+gains[x]+","+losses[x]+","+averagegain[x]+","+averageloss[x]+","+rs[x]+","+rsi[x]
        #+change[x]+","+gains[x]+","+losses[x]+","+averagegain[x]+","+averageloss[x]+","+rs[x]+","+rsi[x]
        #adj, date, openprice, high, low, close, volume, change, gains, losses, averagegain, averageloss, rs, rsi
        f.write(line)
    f.close()
