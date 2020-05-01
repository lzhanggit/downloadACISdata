
def make_request(params):
        
    """ 
	This function was coded by Beichen Zhang for class project
    It is used to send a request to ACIS website and download climate 
    dataset.

    Details of the format and variables in the request can be found at
    the website: https://www.rcc-acis.org/docs_webservices.html

	April 30, 2020
    """
    import requests
    import json
    url = 'http://data.rcc-acis.org/MultiStnData'
    req = requests.post(url,json=params)
    if req.status_code == 400 and req.reason == 'Bad Request':
        raise ValueError('Invalid parameters')
    else:
        return req.text