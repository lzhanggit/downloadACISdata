def check_params(params):
	
	""" 
		This function was originall written by Bill Noon and shared on github:
		https://github.com/bnoon/acis-pandas

		This function was editted and modified by Beichen Zhang for class project

		April 29, 2020

		These parameters are used to make a request to the database of ACIS website. 
		Details of parameters are avaliable at http://www.rcc-acis.org/docs_webservices.html
	"""

	errors = []
	options = {}
	p_dict = dict([(k.lower(),v) for k,v in params.items()])
	p_keys = set(p_dict.keys())

	multi_filter = set(('sids','uids','state','county','climdiv','huc','cwa','bbox'))

	interval_map = dict(dly=(0,0,1), mly=(0,1), yly=(1,))

	#set up stations
	if multi_filter&p_keys:
		print('Import the list of stations...')
	else:
		errors.append('must select stations')
	
	#date range
	if 'date' in p_keys :
		sdate = edate = p_dict['date']
		options['one_date'] = True
	elif len(set(('sdate','edate')) & p_keys) == 2 :
		sdate, edate = p_dict['sdate'], p_dict['edate']
	else :
		errors.append('Missing date range')
	
	if 'elems' in p_keys :
		def parse_interval(yr,mn=0,dy=0) :
			if dy > 0 :
				if yr+mn > 0 : raise ValueError()
				if dy > 1 : return '%dD'%(dy)
				return 'D'
			if mn > 0 :
				if yr > 0 : return '%dM'%(yr*12 + mn)
				elif mn > 1 : return '%dM'%(mn)
				return 'M'
			else :
				if yr > 1 : return '%dA'%(yr)
				return 'A'
		if isinstance(p_dict['elems'], str) :
			base_ts = 'D'
		else :
			base_ts = None
			for e_idx, elem in enumerate(p_dict['elems']) :
				need_reduce = False
				e_interval = elem.get('interval','dly')
				if isinstance(e_interval,str) and e_interval in interval_map :
					e_interval = interval_map[e_interval]

				if not isinstance(e_interval,(list,tuple)) :
					errors.append('Invalid interval elem_%d'%(e_idx))
					continue
				try :
					e_ts = parse_interval(*e_interval)
				except (ValueError, TypeError) :
					errors.append('Invalid interval elem_%d'%(e_idx))
					continue
				if base_ts is None : base_ts = e_ts
				elif base_ts != e_ts :
					errors.append('All elems must use the same interval')
					break
	else : errors.append('Missing elems')
	options['date_freq'] = base_ts
	
	if errors : raise ValueError('\n'.join(errors))
	return p_dict, options
	

