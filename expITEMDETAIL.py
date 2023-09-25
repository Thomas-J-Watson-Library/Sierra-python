#!Python
# auth: Michael Cummings, Watson Library Systems, Met Museum of Art
# file: expITEMDETAIL.py
# use:  The functions in this script are called from expITEMS.py
#       expITEMDETAIL.getITEMDETAIL(an item id)

def getITEMDETAIL(itemid):
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
    RECORD_ID = itemid
    PAYLOAD = {'fields':'callNumber,barcode,fixedFields'}

    ITEM_DETAIL_URL = SIERRA_API_HOST + API_ENDPOINT + RECORD_ID 
    ITEM_DETAIL_RES = requests.get(ITEM_DETAIL_URL, headers = REQUEST_HEADERS, params = PAYLOAD)
    itemDetail= json.loads(ITEM_DETAIL_RES.text)

    # print('\nResponse for individual item detail:')
    # pprint(itemDetail)
    #
    # This creates my standard dictionary, but the Data is a longer line comprised of multiple
    # data elements.
    datatext = ""
    barcode_text = "No barcode"
    if itemDetail.get("barcode") != None:
        barcode_text = itemDetail.get("barcode")
    itemtag = " &nbsp; "
    itemDict = { "Tag": itemtag, "Label": ".i" + itemDetail.get("id") +"a | " + barcode_text, "Data":None}
    #
    call_num_text = "No item call no."
    if itemDetail.get("callNumber") != None:
        call_num_text = itemDetail.get("callNumber").replace('|b',' ')
        datatext = "Item Call Number: " + call_num_text + " | "
    #
    datatext += "&nbsp; Location: "  + itemDetail.get("fixedFields").get("79").get("display") + " <BR/> "
    datatext += "&nbsp; Created: "   + itemDetail.get("fixedFields").get("83").get("value")[0:10] + " | "  
    datatext += "&nbsp; Item Type: " + itemDetail.get("fixedFields").get("61").get("display") + " | "
    datatext += "&nbsp; Checkouts: LYR " + itemDetail.get("fixedFields").get("110").get("value") + " | "
    datatext += "YTD " + itemDetail.get("fixedFields").get("109").get("value") + " | "
    datatext += "TTL " + itemDetail.get("fixedFields").get("76").get("value")
     # determine itemicon
    chkouts = itemDetail.get("fixedFields").get("76").get("value")
    chkcount= int(chkouts)
    if chkcount == 0:
        datatext += " &nbsp; | <i class='bi bi-dash-circle-dotted'></i>"
    if chkcount > 0 and chkcount < 3:
        datatext += " &nbsp; | <i class='bi bi-star'></i>"
    if chkcount >= 3:
        datatext += " &nbsp; | <i class='bi bi-gem'></i>"
    #
    # put the datatext in the Data element of itemDict
    itemDict["Data"] = datatext
    # print("This item dictionary:")
    # print(itemDict)
    return(itemDict)