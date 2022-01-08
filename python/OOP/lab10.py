class person:
	def __init__(self,name, address, phone_number):
		self.name = name
		self.address = address
		self.phone_number = phone_number
	def get_name(self):
		return self.name
	def get_address(self):
		return self.address
	def get_phone_number(self):
		return self.phone_number
class Customer(person):
	def __init__(self,name, address, phone_number,cust_number,on_list_flag ):
		super().__init__(name, address, phone_number)
		self.cust_number = cust_number
		self.on_list_flag = on_list_flag
	def get_cust_number(self):
		return self.cust_number
	def get_on_list(self):
		return self.on_list_flag
	
