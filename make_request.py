
def make_request(params):
        
    """ 
    This function was originall written by Bill Noon and shared on github:
	https://github.com/bnoon/acis-pandas

	This function was editted and modified by Beichen Zhang for class project
    It is used to send a request to ACIS website

	April 29, 2020
    """
    import urllib.request
    import requests
    import json
    api_name = 'MultiStnData'
    req = requests.get('http://data.rcc-acis.org/'+api_name,
        json.dumps(params))
    print(req)
    try :
        response = urllib.request.urlopen(req)
    except urllib.request.HTTPError as e :
        if e.code == 400 and e.msg == 'Bad Request' :
            raise ValueError('Invalid parameters')
        raise
    return json.loads(response.read())
