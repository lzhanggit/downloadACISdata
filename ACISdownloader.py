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

def downloader(**params) :
    
    """ 

		This function was coded and modified by Beichen Zhang for class project

		April 30, 2020
	"""
    import numpy as np
    import pandas as pd
        
    elem_name = params['elems'].split(',')[:]
    raw = make_request(params)
    raw = eval(raw)
    data = raw['data']
    len_data = len(data)
    output_data=[]
    uid_list = []
    ll_list = []
    sids_list = []
    state_list = []
    elev_list = []
    name_list = []

    for i in range(len_data):
        stn = data[i]
        data_meta = stn['meta']
        keys = [k for k in data_meta.keys()]
        if 'uid' in keys:
            data_uid = data_meta['uid']
            uid_list.append(data_uid)
        else:
            uid_list.append(np.nan)
        if 'll' in keys:
            data_ll = str(data_meta['ll'])
            ll_list.append(data_ll)
        else:
            ll_list.append(np.nan)
        if 'sids' in keys:
            data_sids = str(data_meta['sids'])
            sids_list.append(data_sids)
        else:
            sids_list.append(np.nan)
        if 'state' in keys:
            data_state = data_meta['state']
            state_list.append(data_state)
        else:
            state_list.append(np.nan)
        if 'elev' in keys:
            data_elev = data_meta['elev']
            elev_list.append(data_elev)
        else:
            elev_list.append(np.nan)
        if 'name' in keys:
            data_name = data_meta['name']
            name_list.append(data_name)
        else:
            name_list.append(np.nan)
        data_stn = stn['data']
        output_data.append(data_stn)
    d = {'uid':uid_list,'lat and long':ll_list,'sids':sids_list,'state':state_list,\
        'elevation': elev_list, 'name':name_list}
    df = pd.DataFrame(data=d)
    output_data=np.asarray(output_data)
    output_data[output_data=='M']=np.nan
    output_data=output_data.astype(float)
    for j in range(len(elem_name)):
        data_arranged = output_data[:,j]
        df[str(elem_name[j])]=data_arranged
    return df
