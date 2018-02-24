import xlrd
import pandas as pd
import numpy as np
import ebaysdk
from ebaysdk.finding import Connection as finding

###The first version of my Ebay COmic Price Finder .10

#Initialize primary variables.
#ComicList = input('Enter path of file')
ComicList = "C:\ProjectRepo\CBEPC\Testspreadsheet.xlsx"
PanComicList = pd.read_excel(ComicList)
IssueColumn = PanComicList['Issues']
TitleColumn = PanComicList['Title']
TCount = -1
IList = []
TList = []
TNI = []
api = finding(siteid='EBAY-GB', appid='????', config_file=None)



#Create list of titles
for TitleCell in TitleColumn:
    TList.append(str(TitleCell))

# Create array of issue numbers. Each element of the list is a list. The inner list's elements are the specific issue
# numbers seperated by commas
for IssueCell in IssueColumn:
    Issues = (str(IssueCell).split(','))
    IList.append(Issues)

# Create a list where each element is a title and issue number. There should be an element for every single issue
# where the title is matched with every issue number in it's corresponding list. This is presently the #1 challenge
# with this app
for T in TList:
    TCount += 1
    for I in IList[TCount]:
        TNI.append(T + I)

for Elm in TNI:
    api.execute('findcompleteditems', {'keywords': Elm, 'categoryid': ['1', '63'],"paginationInput": {'entriesPerPage': '25','pageNumber': '1'},'sortOrder': 'CurrentPriceHighest'})

dictstr = api.response_dict()

for item in dictstr['searchResult']['item']:
    print("ItemID: %s" % item['itemId'].value)
    print("Title: %s" % item['title'].value)
    print("CategoryID: %s" % item['primaryCategory']['categoryId'].value)



#print(TList)
#print(IList)
#print(TNI)
#print(PanComicList)





