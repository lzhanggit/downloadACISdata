import urllib.request
import json

def make_request(params):
    api_name = 'MultiStnData'
    req = urllib.request.Request('http://data.rcc-acis.org/'+api_name,
        json.dumps(params),
        {'Content-Type':'application/json'})
    try :
        response = urllib.request.urlopen(req)
    except urllib.request.HTTPError as e :
        if e.code == 400 and e.msg == 'Bad Request' :
            raise ValueError('Invalid parameters')
        raise
    return json.loads(response.read())
