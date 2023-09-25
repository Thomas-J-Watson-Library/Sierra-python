#! python

def OCLCHOLDINGS(oclc):
    import json
    import requests
    from requests import Request, Session
    BASE_URL='http://www.worldcat.org/webservices/catalog/content/libraries/'
    OCLC_ID =oclc
    # This a private key OCLC issued to Watson
    KEY  ='kJbnGpNW4MDGCVTq9xmh7RDBHaNhdoAXciJfQTYmbOScCM8cNEWCDttwBqT74LpUK9V4aD0dw6Li8koj'
    # Make a request
    oclc_response = requests.get(BASE_URL + OCLC_ID + '?location=10025&maximumLibraries=50&wskey=' + KEY)
    # The format of the response is XML :-o
    # print(oclc_response.status_code)
    # Convert the XML response into a Python object
    import xmltodict
    oclc_data = xmltodict.parse(oclc_response.content)
    oclcList = []
    try:
        # This code is iterating through a Python ordered dict object.
        # This was painful.
        for h in oclc_data.get("holdings").get("holding"):
            for key, value in h.items():
                if key == "physicalLocation":
                    myLoc = value
                if key == "institutionIdentifier":
                    for key, value in value.items():
                        if key == "value":
                            myInstID = value
            oclcList.append(myInstID + " : " + myLoc)
    except:
        print("no OCLC holdings were identified.")
    return(oclcList)    
    # If you needed to for some reason, this prints the original xml format
    # print(xmltodict.unparse(oclc_data, pretty=True))
    ''' -----------------------
    # example of error:
    # -----------------------
    #200
    #{
    #    "diagnostics": {
    #        "@xmlns:diag": "http://www.loc.gov/zing/srw/diagnostic/",
    #        "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
    #        "@xmlns:isohol": "http://oclcpica.org/?id=1013&ln=uk",
    #        "diagnostic": {
    #            "@xmlns": "http://www.loc.gov/zing/srw/diagnostic/",
    #            "uri": "info:srw/diagnostic/1/65",
    #            "message": "Record does not exist"
    #        }
    #    }
    #}
    # -----------------------
    # example of match:
    # -----------------------
    #200
    #{
    #    "holdings": {
    #        "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
    #        "@xsi:noNamespaceSchemaLocation": "http://www.loc.gov/standards/iso20775/N121_ISOholdings_v4.xsd",
    #        "holding": [
    #            {
    #                "institutionIdentifier": {
    #                    "value": "DLC",
    #                    "typeOrSource": {
    #                        "pointer": "http://worldcat.org/registry/institutions/"
    #                    }
    #                },
    #                "physicalLocation": "Library of Congress",
    #                "physicalAddress": {
    #                    "text": "Washington, DC 20540 United States"
    #                },
    #                "electronicAddress": {
    #                    "text": "https://www.worldcat.or..."
    #                },
    #                "holdingSimple": {
    #                    "copiesSummary": {
    #                        "copiesCount": "1"
    #                    }
    #                }
    #            }
    #            ]
    #        }
    #    }
    '''        

