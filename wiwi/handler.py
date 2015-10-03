

from wsgiref.simple_server import make_server
from wiwi.core.service import api

def server(port):
	port = int(port)
	httpd = make_server('0.0.0.0', port, api)
	print("Serving on port %s..."%port)
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		print('Goodbye.')
