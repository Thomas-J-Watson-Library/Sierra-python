#!Python
# auth: Michael Cummings, Watson Library Systems, Met Museum of Art
# file: expITEMS.py
# use:  The functions in this script are called from explorer.py

def getITEMS(bibrecno):
    import expITEMDETAIL
    import requests
    import base64
    import json
    from pprint import pprint
    from requests import Request, Session
    ### ESTABLISH API SETTINGS for read-only access with this key, secret ###
    SIERRA_API_HOST = 'https://library.metmuseum.org:443'
    SIERRA_API_KEY = 'DN4DAGoe+gIN1mkNHhBvWOA0qRbG'
    SIERRA_API_KEY_SECRET = 'Re@dbetweenthelines'

    ### BEGIN BOILERPLATE REST API AUTHENTICTION TEMPLATE ###
    AUTH_URI = '/iii/sierra-api/v6/token'
    AUTH_URL = SIERRA_API_HOST + AUTH_URI
    ENCODED_KEY = base64.b64encode((SIERRA_API_KEY + ':' +
    SIERRA_API_KEY_SECRET).encode('utf-8')).decode('utf-8')
    AUTH_HEADERS = {'Accept': 'application/json', 'Authorization': 'Basic ' +
              ENCODED_KEY,'Content-Type': 'application/x-www-form-urlencoded'}
    GRANT_TYPE = 'client_credentials'
    AUTH_RESPONSE = requests.post(AUTH_URL, headers = AUTH_HEADERS, data = GRANT_TYPE)
    ACCESS_TOKEN = AUTH_RESPONSE.json()['access_token']
    API_ENDPOINT = '/iii/sierra-api/v6/items/'

    ### CUSTOM REQUEST HEADER FOR THIS API ONLY SET Content-Type to
    ### application/marc-json
    REQUEST_HEADERS = {'Accept': 'application/marc-json', 'Authorization': 'Bearer ' +
                ACCESS_TOKEN,'Content-Type': 'application/json'}
    RECORD_ID = bibrecno
    PARAMS = "?bibIds=" + RECORD_ID
        #------------------------------------------------------------#
        # Retrieve MARC record from Sierra API   #
        #------------------------------------------------------------#
    IURL = SIERRA_API_HOST + API_ENDPOINT + PARAMS
    ITEMRES = requests.get(IURL, headers = REQUEST_HEADERS)
    itemData = json.loads(ITEMRES.text)
    #print("***",itemData)
    #
    itemsList = []
    if itemData.get('code') != 107:
        for item in itemData.get("entries"):
            thisItemDict = expITEMDETAIL.getITEMDETAIL(item.get('id'))
            # print("Dictionary returned from expITEMDETAIL:")
            # print(thisItemDict)
            itemsList.append(thisItemDict)
            # I am adding a blank row between items
            itemsList.append({ "Tag":" &nbsp; ","Label":" &nbsp; ","Data":" &nbsp;" })                                                                   
    return(itemsList)
