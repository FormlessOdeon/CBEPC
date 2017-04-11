import xlrd
import pandas as pd
import numpy as np

###The first version of my Ebay COmic Price Finder .00
ComicList = "C:\\Users\sam.APM\Desktop\PyTest\Testspreadsheet.xlsx"            #input("Enter a File Path")
PanComicList = pd.read_excel(ComicList)
IssueColumn = PanComicList['Issues']
TitleColumn = PanComicList['Title']
TCount = 0
TList = []
TNI = []

for TitleCell in TitleColumn:
    TList.append(str(TitleCell))

#print(TList)
for IssueCell in IssueColumn:
    Issues = str(IssueCell).split(',')
    #print(Issues)
    for Issue in Issues:
        #print(TList[TCount])
        TNI.append(ListAdd)
        TCount = TCount + 1
    #for Issue in Issues:
        #print(Title)
        #print(Issue)
#print(TNI)
#print(PanComicList)




