def make_labels(elems) :
    """ 
		This function was originall written by Bill Noon and shared on github:
		https://github.com/bnoon/acis-pandas

		This function was editted and modified by Beichen Zhang for class project

		April 29, 2020
	"""
    labels = []
    counts = {}
    if isinstance(elems,str) :
        elems = elems.split(',')
    for elem in elems :
        if isinstance(elem,str) :
            name = elem
        elif isinstance(elem,int) :
            name = str(elem)
        elif isinstance(elem,dict) :
            if 'label' in elem : name = elem.pop('label')
            elif 'name' in elem : name = elem['name']
            elif 'vX' in elem : name = str(elem['vX'])
            else : name = 'elem'
        else : raise ValueError("Invalid elem in elems")
        cnt = counts.setdefault(name,0)
        if cnt == 0 : labels.append(name)
        else : labels.append('%s_%d'%(name,cnt))
        counts[name] += 1
    return labels