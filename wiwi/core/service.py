


import falcon
import json
import os
import glob
import imp
import inspect
api = falcon.API()

clsnames = ['on_get', 'on_post', 'on_delete', 'on_put', 'on_options']


cfiles = glob.glob('controllers/*.py')
print('*')*60
print('* Exposing:\n*')

for i in cfiles:
	mname = os.path.basename(i).split('.')[0]
	target = imp.load_source(mname, i)
	for each in dir(target):
		if each.startswith('_'):
			continue

		cs = getattr(target, each)
		if not any([(x in dir(cs)) for x in clsnames]):
			continue
		api_path = '/%s/%s'%(mname, each.lower())
		print('*\t'+api_path)
		api.add_route(api_path, cs())

print('*')*60
print ('\n')
