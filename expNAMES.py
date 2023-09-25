#!Python
# file: expNAMES.py
# auth: Michael Cummings, Watson Library Systems, Met Museum of Art
# Functions to retrieve linked data elements from loc.gov.authorities/names
# This script is called by explorer.py
# This provides a framework that can be fleshed out later.
from operator import contains
import pprint
import urllib.request
import json

def getNAMES(ldname):
    '''
    Receive a tag and uri in dict ldname; go to loc.gov.authories/names;
    retrieve JSON; parse JSON and put useful bits into a list of dictionaries.
    Return the list to the main program
    '''
    works_count = 0
    contributor_count = 0
    myCounts = ""
    # Extract the last segment of the URI which contains the nameID
    myNameID = ldname.get("URI").split("/")[5]

    # Connect to loc.gov.authorities page for this nameID
    myUri = ldname.get("URI")+".json"
    with urllib.request.urlopen(myUri) as response:
        locNameRes = response.read()
    # Convert JSON response to Python
    linkedDataJson = json.loads(locNameRes)
    # You can use the next command to see the whole response, a fairly complex,
    # nested list of dicts and lists!
    # print("full dump of loc name response:")
    #print(json.dumps(linkedDataJson, indent=4))
    
    # print("---end of loc name response ---\n")
    # initalize a list and variable(s)
    mynames = []
    locLbl  = None
    for element in linkedDataJson:
        #print(element.keys())
      # You can use the next command to see each element
      #print(json.dumps(element, indent=4,),"\n\n")
      ## NEW
        if  "wikidata" in element.get("@id"):
            myWiki = {
                "tag":" &nbsp; ",
                "Label":"WikiData " + element.get("@id").split("/")[4],
                "Data": "<A href=" + element.get("@id")+" target=new>"+ element.get("@id") + "</A>"
                }
            mynames.append(myWiki)
      ## END NEW
      # get the nameID
        if element.get("@type")[0] == "http://id.loc.gov/ontologies/bibframe/Work":
            works_count += 1
        #
        #
        try:
          # Capture the authoritative label. Use try/except to avoid error
          authorizedLabel = \
          element.get('http://www.loc.gov/mads/rdf/v1#authoritativeLabel')
          if authorizedLabel != None:
              locLbl = authorizedLabel[0].get("@value")
              myAL = {
                      "tag":ldname.get("Tag"),
                      "Label":"Authoritative Label",
                      "Data": "(" + myNameID + ") . . . . " + locLbl
                      }
        except:
            continue
        #
        contrib = element.get("http://id.loc.gov/ontologies/bflc/contributorTo")
        if contrib:
            contributor_count += len(contrib)

    myCOUNTS = {
            "tag": ' &nbsp; ',
            "Label":"Counts",
            "Data": "Works: " + str(works_count) + " | Contributor To: " + str(contributor_count)
            }            
    # load up the list of names and any associated fields
    mynames.append(myAL)
    mynames.append(myCOUNTS)
    # ** Many other fields can probably be gleaned from the linked data
    # ** To do: parse the return from library of congress, create a dictionary
    #    to hold info as modelled above, add the additional info to mynames
    
    # last, send the list back to the main script
    return(mynames)
