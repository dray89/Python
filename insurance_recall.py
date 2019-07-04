python

class Insurance_plans: 
    def __init__(self, intercept = 100, self_perc = 1, list_price = 0):
		self.list_price = list_price
		self.intercept = intercept

class Uninsured(Insurance_plans):
	def __init__(self, list_price, intercept = 100, self_perc = 1.00):
		Insurance_plans.__init__(self, list_price, intercept, self_perc)
		self.uninsured_perc = self_perc
		self.uninsured_quantity = self.intercept - self.uninsured_perc*self.list_price
end

python
class Full(Uninsured):
	def __init__(self, list_price, intercept = 100, uninsured_perc = 1.00, self_perc = 0.00):
		Uninsured.__init__(self, list_price, intercept, uninsured_perc = self.uninsured_perc)
		self.self_pay = self.self_perc*self.list_price
		self.quantity = self.intercept - self.self_pay
	
	def social_loss(self):
		self.social_loss = .5*self.list_price**2*(uninsured_price - self.self_pay)**2
end
class Coinsure(Uninsured):
	def __init__(self, list_price, intercept = 100, self_pay = .5):
		Uninsured.__init__(self, list_price, intercept)
		self.self_pay = self_pay
	
	def quantity(self):
		self.quantity = self.intercept - self.self_pay*self.list_price
	
	def social_loss(self):
		self.social_loss = .5*(self.list_price*(1-self.self_pay))**2

class Copay(Uninsured):
	def __init__(self, list_price, intercept = 100, self_pay = 25):
		Uninsured.__init__(self, list_price, intercept)
		self.self_pay = self_pay
	
	def quantity(self):
		self.quantity = self.intercept - self.self_pay
	
	def social_loss(self):
		self.social_loss = .5*(self.list_price-self.self_pay)**2

end
