#!Python
#
# file: expMARCINFO
# auth: Michael Cummings, Watson Library Systems, Met Museum of Art
# desc: sub part of the explorer program reads MARC and compiles a list of dicts
# use:  The functions in this script are called from explorer.py
# ref:  https://www.loc.gov/marc/bibliographic/
'''
explorer sends this script MARC JSON for a bib record as 'jdata'; the script should
return selected fields from the MARC record in a list. Each list element
should have the following dictionary structure of three parts. If you don't want
to have a tag, enter " &nbsp; " as tge Tag value.
[
{  "Tag"  : "245",  "Label": "Title",  "Data" : "Gone with the Wind"}

'''
def getMARCINFO(jdata):
    '''
    Parse MARC bib data, return selected list of tags.
    This is more difficult than using the Sierra bib API, but more precise
    '''
    bibFieldsReturnList = []
    #print(jdata)
    # 
    # jdata controlfield has tags 001, 003, 005, 008
    #
    controlfields = jdata.get('controlfield')
    OCLCstring = ""
    for f in controlfields:
        if f.get('tag') == '001':
            OCLCstring = f.get('data')    
            myOCLC = {
                "Tag" : f.get('tag'),
                "Label" : "OCLC Number",
                "Data" : OCLCstring
                }
            bibFieldsReturnList.append(myOCLC)
    #
    # regular fields
    #
    fields = jdata.get('datafield')
    ISBNstring = ""
    for f in fields:
        if f.get('tag') == '020':
            i = f.get('subfield')
            for subfield in i:
                if subfield.get('code') == "a":
                    ISBNstring = subfield.get('data')    
            myISBNs = {
                "Tag" : f.get('tag')+'a',
                "Label" : "ISBN Number",
                "Data" : ISBNstring
                }
            bibFieldsReturnList.append(myISBNs)
    callnostring = ''
    for f in fields:
        if f.get('tag') == '090':
            c = f.get('subfield')
            for subfield in c:
                if subfield.get('code') == "a":
                    callnostring = subfield.get('data')
                if subfield.get('code') == "b":
                    callnostring += " " + subfield.get('data')
            myCallNo = {
                "Tag" : f.get('tag')+'ab',
                "Label" : "Call Number",
                "Data" : callnostring
                }
            bibFieldsReturnList.append(myCallNo)
        if f.get('tag') == '245':
            t = f.get('subfield')
            for subfield in t:
                if subfield.get('code') == "a":
                    titleString = subfield.get('data')
                if subfield.get('code') == "b":
                    titleString += " "+subfield.get('data')
                if subfield.get('code') == "c":
                    titleString += " "+subfield.get('data')
            myTitle = {
                "Tag" : f.get('tag')+'abc',
                "Label" : "Title",
                "Data" : titleString[0:100]
                }
            bibFieldsReturnList.append(myTitle)
        if f.get('tag') == '100':
            a = f.get('subfield')
            for subfield in a:
                if subfield.get('code') == "a":
                    authorString = subfield.get('data')
                if subfield.get('code') == "d":
                    authorString += " "+subfield.get('data')
                if subfield.get('code') == "e":
                    authorString += " "+subfield.get('data')
            myAuthor = {
                "Tag" : f.get('tag')+'ade',
                "Label" : "Author ",
                "Data" : authorString
                }
            bibFieldsReturnList.append(myAuthor)
        if f.get('tag') == '500':
            a = f.get('subfield')
            for subfield in a:
                if subfield.get('code') == "a":
                    noteString = subfield.get('data')

            myNote = {
                "Tag" : f.get('tag')+'a',
                "Label" : "Note ",
                "Data" : noteString
                }
            bibFieldsReturnList.append(myNote)
        if f.get('tag') == '650':
            sub650String = ''
            if f.get('ind') != ' 7':
                a = f.get('subfield')
                for subfield in a:
                    sub650String += subfield.get('data')+' -- '
                mySubject = {
                    "Tag" : f.get('tag')+'any',
                    "Label" : "Subject Topical",
                    "Data" : sub650String.rstrip(' -- ')
                    }   
                bibFieldsReturnList.append(mySubject) 
        if f.get('tag') == '651':
            sub651String = ''
            if f.get('ind') != ' 7':
                a = f.get('subfield')
                for subfield in a:
                    sub651String += subfield.get('data')+' -- '
                mySubject = {
                    "Tag" : f.get('tag')+'any',
                    "Label" : "Subject Geographic",
                    "Data" : sub651String.rstrip(' -- ')
                    }   
                bibFieldsReturnList.append(mySubject)   
        if f.get('tag') == '264':
            sub264String = ''    
            if f.get('ind') != ' 4':           
                c = f.get('subfield')
                for subfield in c:
                    if subfield.get('code') == "a":
                        sub264String += subfield.get('data')
                    if subfield.get('code') == "b":
                        sub264String += " " + subfield.get('data')
                    if subfield.get('code') == "c":
                        sub264String += " "+ subfield.get('data')
                myCopyright= {
                    "Tag" : f.get('tag')+'abc',
                    "Label" : "Copyright",
                    "Data" : sub264String
                    }   
                bibFieldsReturnList.append(myCopyright) 
        #  
        # Optionally add some more fields to bibFieldsReturnList
        # here are some suggestions. Be sure to compose a 
        # dictionary having Title, Lable, and Data.
        # ISBN
        # OCLC
        # material type
        # publisher
        # description
        # notes
        # alternate titles

    # ------------------------------------------
    # etc... then after gathering all fields
    # -------------------------------------------
    return(bibFieldsReturnList)

def getURIS(jdata):
    '''
    Parse MARC bib data, return list of URI fields.
    This function should return a list structured like this:
    [ { "Tag":"245", "Data":"http://loc.gov...etc"},
      { "Tag":"650", "Data":"http://loc.gov...etc"},}
    ]
    '''
    URIReturn = []
    fields = jdata.get('datafield')
    for f in fields:
        #print(f.get('tag'),f.get('subfield'))
        for s in f.get('subfield'):
            if s.get('code') == '0' and 'authorities' in s.get('data'):
                myuri = { "Tag" :f.get('tag'), "URI" : s.get('data') }
                URIReturn.append(myuri)
    try:
        # sort by tag number
        URIbytag = sorted(URIReturn, key=lambda x: x['Tag'])
    except:
        URIbytag = []
    return(URIbytag)
