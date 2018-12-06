#!/usr/bin/env python
import json
# f = open('data.json')
# data = json.load(f)
# f.close()

with open('sample.json') as data_file:    
    data = json.load(data_file)
    for record in data['records']:
    	mod = {}
    	mod['put'] = 'id:reservation:reservation::' + record['id']
    	mod['fields'] = record
    	print json.dumps(mod, indent=4, sort_keys=True)
#         print data ['restaurants'][0]['restaurant']['name']
        