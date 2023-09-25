#! Python
# file: expADVICE.py
# 
'''
This API returns random advice in the format of a nested dictionary. Example:
{'slip': {'id': 169, 'advice': 'Do something selfless.'}}
'''
def getAdvice():
    import urllib.request
    import json
    url='https://api.adviceslip.com/advice'
    with urllib.request.urlopen(url) as response:
        res = response.read()
    ainfo = json.loads(res)
    print("\nAdvice:",ainfo.get('slip').get('advice'),"\n")

