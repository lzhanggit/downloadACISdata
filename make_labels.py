def make_labels(raw_data) :
    """ 
		This function was coded by Beichen Zhang for class project

		April 29, 2020
	"""
    data = raw_data['data']
    print(data)
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
        data_stn = stn['data']
        data_meta = stn['meta']
        data_uid = data_meta['uid']
        data_ll = str(data_meta['ll'])
        data_sids = str(data_meta['sids'])
        data_state = data_meta['state']
        data_elev = data_meta['elev']
        data_name = data_meta['name']
        output_data.append(data_stn)
        uid_list.append(data_uid)
        ll_list.append(data_ll)
        sids_list.append(data_sids)
        state_list.append(data_state)
        elev_list.append(data_elev)
        name_list.append(data_name)
    
        print(uid_list)
    return uid_list,ll_list,sids_list,state_list,elev_list,output_data