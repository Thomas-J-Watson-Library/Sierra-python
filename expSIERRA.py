#!python
#
# file: expSIERRA.py
# auth: Michael Cummings, Watson Library Systems, Met Museum of Art
'''
Skeleton Sierra API calls
explorer calls these functions to get bib MARC data 
'''
def getBIBMARC(recno):
    import requests
    import base64
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
    API_ENDPOINT = '/iii/sierra-api/v6/bibs/'

    ### CUSTOM REQUEST HEADER FOR THIS API ONLY SET Content-Type to
    ### application/marc-json
    REQUEST_HEADERS = {'Accept': 'application/marc-json', 'Authorization': 'Bearer ' +
                ACCESS_TOKEN,'Content-Type': 'application/marc-json'}
    RECORD_ID = str(recno)
        #------------------------------------------------------------#
        # Retrieve MARC record from Sierra API   #
        #------------------------------------------------------------#
    BURL = SIERRA_API_HOST + API_ENDPOINT + RECORD_ID + '/marc'
    BIBRES = requests.get(BURL, headers = REQUEST_HEADERS)

    '''
    This function can return the JSON string. (The JSON string will be
    passed to a utility function that adds required quotes around The
    key names.)

    '''
    # There are many attributes of a response. We want the text.
    return(BIBRES.text)
