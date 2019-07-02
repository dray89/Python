python

class insurance_plans: 
    def __init__(self, list_price):
        self.list_price = list_price
        list_price = self.list_price

class uninsured(insurance_plans):
	def __init__(self, list_price, uninsured_price = 1):
		insurance_plans.__init__(self, list_price)
		self.uninsured_price = uninsured_price

	def quantity(self, intercept = 100):
		self.uninsured_quantity = intercept - self.uninsured_price*self.list_price

class full(uninsured):
	def __init__(self, list_price, self_pay = 0):
		uninsured.__init__(self, list_price)
		self.self_pay = self_pay
	
	def quantity(self, intercept = 100):
		self.quantity = intercept - self.self_pay*self.list_price
	
	def social_loss(self, uninsured_price = 1, intercept = 100):
		self.uninsured_pay = uninsured_price*self.list_price
		self.uninsured_quantity = intercept - self.uninsured_pay
		self.social_loss = (self.uninsured_pay - self.self_pay*self.list_price)*(self.quantity - self.uninsured_quantity)/2

class coinsure(uninsured):
	def __init__(self, list_price, self_pay = .5):
		uninsured.__init__(self, list_price)
		self.self_pay = self_pay
	
	def quantity(self, intercept = 100):
		self.quantity = intercept - self.self_pay*self.list_price
	
	def social_loss(self, uninsured_price = 1, intercept = 100):
		self.uninsured_pay = uninsured_price*self.list_price
		self.uninsured_p = intercept - self.quantity
		self.uninsured_quantity = intercept - self.uninsured_pay
		self.social_loss = (self.list_price - self.uninsured_p)*(self.quantity - self.uninsured_quantity)/2

class copay(uninsured):
	def __init__(self, list_price, self_pay = 25):
		uninsured.__init__(self, list_price)
		self.self_pay = self_pay
	
	def quantity(self, intercept = 100):
		self.quantity = intercept - self.self_pay
	
	def social_loss(self, uninsured_price = 1, intercept = 100):
		self.uninsured_pay = uninsured_price*self.list_price
		self.uninsured_quantity = intercept - self.uninsured_pay
		self.social_loss = (self.uninsured_pay - self.self_pay)*(self.quantity - self.uninsured_quantity)/2

end
