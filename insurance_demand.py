python 

insured = calc_quantity(0, 70)
coinsurance = calc_quantity(.5*list_price)
copay = calc_quantity(25)

insured.quantity
coinsurance.quantity
copay.quantity

python 

class insurance_plans: 
	
	def __init__(self, self_pay, list_price):
		self.self_pay = self_pay
		__self_pay = self.self_pay
		self.list_price = list_price
		__list_price = self.list_price

end 

python

class uninsured(insurance_plans):
	def uninsured_quantity(self):
		uninsured_quantity = calc_quantity(self_pay = self.list_price)
		self.uninsured_quantity = uninsured_quantity
	
	def uninsured_price(self):
		uninsured_price = calc_price(self_pay = self.list_price)
		self.uninsured_price = uninsured_price
		
end 

	def calc_quantity(self, __self_pay):
		self.self_pay = __self_pay
		
		self.quantity = 100 - __self_pay
		self_quantity = self.quantity
		
	def calc_price(self, self_pay):
		self.price = self_pay
		
	def social_loss(self_pay, self_quantity):
		chg_price = lambda chg_price:  uninsured_price - self_pay  
		chg_qt = lambda chg_qt: quantity - self.uninsured_quantity 
		self.social_loss = lambda social_loss: (chg_price*chg_qt)/2

end

python 

uninsured = dict(insurance_type = "uninsured", quantity = calc_quantity(list_price)),self_pay = list_price, list_price = list_price, price = list_price)

end 