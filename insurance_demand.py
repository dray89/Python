python

class insurance_plans: 
    def __init__(self, list_price, intercept = 100):
		self.list_price = list_price
		list_price = self.list_price
		self.intercept = intercept
		intercept = self.intercept
end

python
class uninsured(insurance_plans):
	def __init__(self, list_price, intercept = 100, uninsured_price = 1.00):
		insurance_plans.__init__(self, list_price, intercept)
		self.uninsured_price = uninsured_price

	def quantity(self):
		self.uninsured_quantity = self.intercept - self.uninsured_price*self.list_price
end

python
class full(uninsured):
	def __init__(self, list_price, intercept = 100, self_pay = 0.00):
		uninsured.__init__(self, list_price, intercept)
		self.self_pay = self_pay
	
	def quantity(self):
		self.quantity = self.intercept - self.self_pay*self.list_price
	
	def social_loss(self, uninsured_price = 1, intercept = 100):
		self.social_loss = .5*self.list_price**2*(uninsured_price - self.self_pay)**2

class coinsure(uninsured):
	def __init__(self, list_price, intercept = 100, self_pay = .5):
		uninsured.__init__(self, list_price, intercept)
		self.self_pay = self_pay
	
	def quantity(self):
		self.quantity = self.intercept - self.self_pay*self.list_price
	
	def social_loss(self):
		self.social_loss = .5*(self.list_price*(1-self.self_pay))**2

class copay(uninsured):
	def __init__(self, list_price, intercept = 100, self_pay = 25):
		uninsured.__init__(self, list_price, intercept)
		self.self_pay = self_pay
	
	def quantity(self):
		self.quantity = self.intercept - self.self_pay
	
	def social_loss(self):
		self.social_loss = .5*(self.list_price-self.self_pay)**2

end
