#!Python
# file: expSUBJECTS.py
# auth: Michael Cummings, Watson Library Systems, Met Museum of Art
# functions to retrieve linked data elements from loc.gov.authorities/subjects
#
# This provides a framework that can be fleshed out later.
import pprint
import urllib.request
import json

def getSUBJECTS(ldsubject):
    '''
    Receive a tag and uri in dict ldsubject; go to loc.gov.authories/subjects;
    retrieve JSON; parse JSON and put useful bits into a list of dictionaries.
    Return the list to the main program
    '''
    # Extract the last segment of the URI which contains the subjectID
    mySubjectID = ldsubject.get("URI").split("/")[5]

    # Connect to loc.gov.authorities page for this nameID
    myUri = ldsubject.get("URI")+".json"
    with urllib.request.urlopen(myUri) as response:
        locSubjectRes = response.read()
    # Convert JSON response to Python
    linkedDataJson = json.loads(locSubjectRes)
    # You can use the next command to see the whole response, a fairly complex,
    # nested list of dicts and lists!
    #print(json.dumps(linkedDataJson, indent=4))
    # initalize a list and variable(s)
    mysubjects = []
    locLbl  = None
    for element in linkedDataJson:
      # You can use the next command to see each element
      #print(json.dumps(element, indent=4,),"\n\n")
      # get the nameID

      try:
          # Capture the authoritative label. Use try/except to avoid error
          authorizedLabel = \
          element.get('http://www.loc.gov/mads/rdf/v1#authoritativeLabel')
          if authorizedLabel != None:
              locLbl = authorizedLabel[0].get("@value")
              myAL = {
                      "tag":ldsubject.get("Tag"),
                      "Label":"Authoritative Label",
                      "Data": "(" + mySubjectID + ") . . . . " + locLbl
                      }
      except:
            continue
    mySubjectID = {
            "tag": None,
            "Label":"Subject ID",
            "Data": mySubjectID
            }
    # load up the list of names and any associated fields
    mysubjects.append(myAL)
    mysubjects.append(mySubjectID)
    # ** Many other fields can probably be gleaned from the linked data
    # ** To do: parse the return from library of congress, create a dictionary
    #    to hold info as modelled above, add the additional info to mynames

    # last, send the list back to the main script
    return(mysubjects)
