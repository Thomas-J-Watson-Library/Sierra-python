#!python
# file: explorer.py
# auth: Michael Cummings, Watson Library Systems, Met Museum of Art
# desc: This is the main part of the explorer project.
# Retrieves data for staff using multiple APIs. Generates a web page of results.
# Automatically opens web page in a browser.
# use : from terminal, python explorer.py 
#       enter the bibid
#
import expSIERRA, expMARCINFO, expITEMS
import expSUBJECTS, expNAMES
import expOUTPUT, expLIBUTIL
import expTIP, expEXTERNAL
import json

import webbrowser
from pprint import pprint

# -----------------------------------------------------------#
# Get bib from user, convert to b plus id no checkdigit and  #
# establish the variable named 'target'                      #
# -----------------------------------------------------------#

target  = ''
print('.......................................')
print(':                                     :')
print(':      D a t a   E x p l o r e r      :')
print(':                                     :')
print(':.....................................:')
print(': Enter Bib Record Number             :')
print(': without the . prefix or checkdigit  :')
print(':                                     :')
print(': examples:                           :')
print(': b1584252 *   b1998712    b1820481   :')
print(': b1819911     b1992983    b2001902   :')
print(': b2020799     b1983497    b1594826   :')
print(':                                     :')
print(':.....................................:')

bib     = input('   Bib: ')
target  = expLIBUTIL.get_target(bib)


# ------------------------------------------------------#
# Retrieve the MARC record from expSIERRA               #
# ------------------------------------------------------#
print("Thank you. Contacting Sierra database ...")
SierraResponseString = expSIERRA.getBIBMARC(target[1:])
# print(SierraResponseString)
# Use my custom utility function to put the response into valid JSON
editedResponseString = expLIBUTIL.API_cleanup(SierraResponseString)
if len(editedResponseString) < 100:
    print('\n  ',editedResponseString,'\n')
    expOUTPUT.make_404_page(target)
    webbrowser.open('404.html')
    exit(404)
# Convert string into Python JSON structure
jdata = json.loads(editedResponseString)
# print('\n')
# print(': from expSIERRA.getBIBMARC your record as JSON :')
# pprint(jdata, indent=4)

# ---------------------------------------------------------#
# Parse the MARC record from expSIERRA to get bib fields.  #
# ---------------------------------------------------------#
# Send jdata to expMARCINFO which parses jdata and will be
# returning a few fields as a list of dictionaries.
print('Parsing the MARC data ...')
BibDataList = expMARCINFO.getMARCINFO(jdata)
# print('\n')
# print(': from expMARCINFO.getMARCINFO this is saved in BibDataList:')
# pprint(BibDataList, indent=4)

BibData_byTag = sorted(BibDataList, key=lambda i: i['Tag'])
# print(': sorted list of bib fields saved in BibData_byTag:')
# pprint(BibData_byTag)
###Hold on to that data for now ... get more from other apis

# ------------------------------------------------------#
# Retrieve a non-MARC set of fields from tbd??          #
# ------------------------------------------------------#
# We  COULD use the Sierra  API get bib vby record id
# and request specific fields from another API call.
# I chose not to do it that way because there is more 
# control parsing as I do in expMARCINFO.py

# ------------------------------------------------------#
# Retrieve a list of items for this bib from expSIERRA  #
# ------------------------------------------------------#
print('Contacting Sierra database for items ...')
itemsList = expITEMS.getITEMS(target[1:])
# print('\nITEM fields return, as is, from expITEMS (itemList):')
# pprint(itemsList, indent=4)
# Hold on to that data for now ... get more

# ------------------------------------------------------#
# Parse the MARC data from expSIERRA to find URIs       #
# ------------------------------------------------------#
print('Parsing MARC data to retrieve the URIs ... ')
BibURIList = expMARCINFO.getURIS(jdata)
# print('\nURI fields return, as is, from Sierra (BibURIList):')
# pprint(BibURIList, indent=4)


# ------------------------------------------------------#
# Parse the BibURIList to separate names and subjects   #
# ------------------------------------------------------#
# For each NAME URI in BibURIList (they look like this)
# {"Tag":"100","URI":"http://id.loc.gov/authorities/names/n2016008390"}
#
print('Separating name and subject URIs ... ')
NameLinkedDataList = []
for uri in BibURIList:
    if "names" in uri.get("URI"):
        ldName = uri
        print('\nContacting Library of Congress Names Authority ...')
        NameLinkedDataList.append(expNAMES.getNAMES(ldName))
# print('\n fields returned, as is, from expNAMEseLinkedDataList):')
# pprint(NameLinkedDataList, indent=4)

# For each SUBJECT URI in BibURIList (they look like this)
#  {'Tag':'651','URI':'http://id.loc.gov/authorities/subjects/sh85115193'},
#

SubjectLinkedDataList = []
for uri in BibURIList:
    if "subjects" in uri.get("URI"):
        ldSubject = uri
        print('\nContacting Library of Congress Subjects Authority ...')
        SubjectLinkedDataList.append(expSUBJECTS.getSUBJECTS(ldSubject))
# print('\n fields returned, as is, from expSUBJECTS(SubjectLinkedDataList):')
# pprint(SubjectLinkedDataList, indent=4)

#-------------------------------------------------------------------#
# Retrieve fascinating info from EXTERNAL APIs                      #
#-------------------------------------------------------------------#
# get the OCLC number from the list we made earlier
#print('\Retrieving a list of holdings in local institutions ...')
#for field in BibDataList:
#    if field.get("Label") == "OCLC Number":
#	    myOCLC = field.get("Data")
#b2001902OclcLibList = expEXTERNAL.OCLCHOLDINGS(myOCLC)

print('\nChecking for a cover image from Open Library')
myISBN = ""
for field in BibDataList:
    if myISBN == "":
        if field.get("Label") == "ISBN Number":
	        myISBN = field.get("Data")


#-------------------------------------------------------------------#
# Use my expOUTPUT routines to generate the HTML page.              #
#-------------------------------------------------------------------#
print('\nGenerating the HTML page ...')
expOUTPUT.make_head(bib)
expOUTPUT.make_body_to_sierra(bib)
# Bibiographic info section. Pass the dictionary elements from the
# list named BibData_byTag
expOUTPUT.make_bibinfo(bib)
for field in BibData_byTag:
    expOUTPUT.make_data_row(bib,field.get('Tag'),field.get('Label'),field.get('Data'))

expOUTPUT.make_end_accordion_item(bib)
# Item info section. Pass the dictionary elements from the
# list named itemsList
#
expOUTPUT.make_iteminfo(bib)
if len(itemsList) > 1:
    for item in itemsList:
        expOUTPUT.make_data_row(bib,' &nbsp; ',item.get('Label'),item.get('Data'))
else:
    expOUTPUT.make_data_row(bib, " &nbsp; ", "Summary","No item records found.")
expOUTPUT.make_end_accordion_item(bib)
#
# Name URI info section. Pass the dictionary elements in each list[0] from the
# list named NameLinkedDataList
expOUTPUT.make_namesinfo(bib)
for nameuri in NameLinkedDataList:
    expOUTPUT.make_data_row(bib,nameuri[0].get('tag'),nameuri[0].get('Label'),nameuri[0].get('Data'))
    expOUTPUT.make_data_row(bib,nameuri[1].get('tag'),nameuri[1].get('Label'),nameuri[1].get('Data'))
#
# Subject URI info section. Pass the dictionary elements in each list[0] from the
# list named SubjectLinkedDataList
expOUTPUT.make_subjectsinfo(bib)
for subjecturi in SubjectLinkedDataList:
    expOUTPUT.make_data_row(bib,subjecturi[0].get('tag'),subjecturi[0].get('Label'),subjecturi[0].get('Data'))

#
# # end accordion3 name and subject
expOUTPUT.make_end_accordion_item(bib)
#
# a fourth accordion for external apis
expOUTPUT.make_external(bib)
# cover from openlibrary
expOUTPUT.make_openlibrary(bib)
expOUTPUT.make_cover(bib,myISBN)

# local holdings from oclc
#expOUTPUT.make_oclcinfo(bib)
#for holding in OclcLibList:
#    expOUTPUT.make_data_row(bib,"&nbsp;","Held by",holding)
# end accordion4 external
expOUTPUT.make_end_accordion_item(bib)

expOUTPUT.make_footer(bib)
#
print('All done processing and generating a page for ' + target)
print('Opening the page in the webbrowser. ')

#
# Display Random advice
#
expTIP.getAdvice()
#
# Launch the page that was generated
#
url = 'b' + target  + 'a.html'
webbrowser.open(url)
#
# Save summary report in a file
#
# See formatting options help at scaler.com/topics/python/string-formatting-in-python
# Right justify numbers in 6-characters
myColumnHeading ="   BIBID|FIELDS| ITEMS| NAMES| SUBJS|HOLDNG"
myCounters ="{:>6}".format(len(BibDataList))+"|"
myCounters+="{:>6}".format(len(itemsList))+"|"
myCounters+="{:>6}".format(len(NameLinkedDataList))+"|"
myCounters+="{:>6}".format(len(SubjectLinkedDataList))+"|"
#myCounters+="{:>6}".format(len(OclcLibList))
with open('expReport.txt','a') as REPORT:
    print("", file=REPORT)
    print(myColumnHeading, file=REPORT)
    print(target+"|"+myCounters, file=REPORT)
print("See summary in expReport.txt")

