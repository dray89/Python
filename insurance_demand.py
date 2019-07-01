list_price = 70
uninsured = uninsured(list_price)
insured = full(list_price)
coinsurance = fifty_percent(list_price)

coinsurance = calc_quantity(list_price)
copay = calc_quantity(25)

insured.quantity
coinsurance.quantity
copay.quantity

class insurance_plans: 
	
	def __init__(self, self_pay, list_price):
		self.self_pay = self_pay
		self_pay = self.self_pay
		self.list_price = list_price
		list_price = self.list_price
	
	@property
	def get_self_pay(self)
		return self.self_pay
	
	@get_self_pay.setter
	def set_self_pay(self, self_pay):
		self.self_pay = self_pay
		amount = self.self_pay
	
	@property
	def get_list_price(self):
		return list_price
	
	@get_list_price.setter
	def set_list_price(self, list_price):
		self.list_price = list_price
		list_price = self.list_price
	
		
class uninsured(insurance_plans):
	def uninsured_quantity(self):
		uninsured_quantity = calc_quantity(self_pay = self.list_price)
		self.uninsured_quantity = uninsured_quantity
	
	def uninsured_price(self):
		uninsured_price = calc_price(self_pay = self.list_price)
		self.uninsured_price = uninsured_price

class full(insurance_plans):
	def calc_quantity(self):
		self.self_pay = 0
		self.quantity = 100 - self_pay
		self_quantity = self.quantity
		
	def calc_price(self, self_pay):
		self.price = self_pay
		
	def social_loss(self_pay, self_quantity):
		self.chg_price = lambda chg_price:  uninsured_price - self_pay  
		self.chg_qt = lambda chg_qt: quantity - self.uninsured_quantity 
		self.social_loss = lambda social_loss: (chg_price*chg_qt)/2

class fifty_percent(insurance_plans):
	def calc_quantity(self):
		self.self_pay = .5*list_price
		self_pay = self.self_pay
		
		self.quantity = 100 - self_pay
		self_quantity = self.quantity
		
	def calc_price(self, self_pay):
		self.price = self_pay
		
	def social_loss(self_pay, self_quantity):
		self.chg_price = lambda chg_price:  uninsured_price - self_pay  
		self.chg_qt = lambda chg_qt: quantity - self.uninsured_quantity 
		self.social_loss = lambda social_loss: (chg_price*chg_qt)/2
end

uninsured = dict(insurance_type = "uninsured", quantity = calc_quantity(list_price)),self_pay = list_price, list_price = list_price, price = list_price)