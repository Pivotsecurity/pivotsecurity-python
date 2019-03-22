from api import Api

if __name__ == '__main__':
	a = Api('f6074a20b7be4199b3300adf9a2c6efd','d48f21a6e0c94880b61daa2b9e5a2327')
	r = a.info("A13","");
	print (r)
	r = a.validate_auth("A13","","123");
	print (r)
	r = a.lock("A13","");
	print (r)
	r = a.unlock("A13","");
	print (r)
