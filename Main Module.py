import xlrd
import pandas as pd
import numpy as np

###The first version of my Ebay COmic Price Finder .10

#Initialize primary variables.
ComicList = input('Enter path of file')
#ComicList = "C:\\Users\sam.APM\Desktop\PyTest\Testspreadsheet.xlsx"           
PanComicList = pd.read_excel(ComicList)
IssueColumn = PanComicList['Issues']
TitleColumn = PanComicList['Title']
TCount = 0
TList = []
TNI = []

#Create list of titles
for TitleCell in TitleColumn:
    TList.append(str(TitleCell))
#print(TList)

#Create array of issue numbers. Each element of the list is a list. The inner list's elements are the specific issue numbers seperated by commas
for IssueCell in IssueColumn:
    Issues = str(IssueCell).split(',')
    #print(Issues)
    #Create a list where each element is a title and issue number. There should be an element for every single issue where the title is matched with every issue number in it's corresponding list.
    #This is presently the #1 challenge with this app
    for Issue in Issues:
        #print(TList[TCount])
        TNI.append(ListAdd)
        TCount = TCount + 1
    #for Issue in Issues:
        #print(Title)
        #print(Issue)
#print(TNI)
#print(PanComicList)




