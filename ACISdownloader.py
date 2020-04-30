def downloader(**params) :
    
    """ 
		This function was originall written by Bill Noon and shared on github:
		https://github.com/bnoon/acis-pandas

		This function was editted and modified by Beichen Zhang for class project

		April 29, 2020
	"""
    import numpy as np
    import pandas as pd
    from check_params import check_params
    from make_request import make_request
    from make_labels import make_labels
        
    # validate params
    # validate elems
    # calculate timeseries
    cvt_missing = params.pop('missing','M')
    cvt_trace = params.pop('trace','T')
    cvt_subseq = params.pop('subseq','S')
    if 'accum' in params :
        if params['accum'] == True : 
            cvt_accum = lambda a : float(a[:-1])
        else : 
            cvt_accum = lambda a : params['accum']
    p_dict, options = check_params(params)
    columns = make_labels(p_dict['elems'])
    raw = make_request(p_dict)
    
    if 'error' in raw : raise TypeError(raw['error'])

    sdate = p_dict.get('sdate',p_dict['date'])
    if isinstance(sdate,(list,tuple)) : sdate = '-'.join(map(str,sdate))
    raw, datum_slice = raw['data'], slice(0,None)
    all_data = {}
    dates = None
    one_date = 'one_date' in options
    for stn_raw in raw :
        stn_data = dict([(key,[]) for key in columns])
        meta = stn_raw['meta']
        sid = meta['sids'][0].split(' ')[0]
        if one_date : raw_data = [stn_raw['data']]
        else : raw_data = stn_raw['data']
        if dates is None :
            dates = pd.date_range(sdate,periods=len(raw_data),freq=options['date_freq'])
        for datum in raw_data :
            for i,e in enumerate(datum[datum_slice]) :
                try :
                    stn_data[columns[i]].append(float(e))
                except ValueError :
                    if e == 'M' : stn_data[columns[i]].append(cvt_missing)
                    elif e == 'T' : stn_data[columns[i]].append(cvt_trace)
                    elif e == 'S' : stn_data[columns[i]].append(cvt_subseq)
                    elif e.endswith('A') : stn_data[columns[i]].append(cvt_accum(e))
                    else : stn_data[columns[i]].append(e)
        df = pd.DataFrame(stn_data, index=dates)
        all_data[sid] = df
    panel = pd.from_dict(all_data)
    return panel

if __name__ == "__main__":
    p = downloader(climdiv="DE01",date="2011-8",elems="mly_mean_avgt,mly_sum_pcpn")
    print(p)

