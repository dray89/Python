
python

plans = insurance_plans(70)
plans

insured = full(list_price)
coinsurance = coinsurance(list_price)
copay = copay(list_price)
end
uninsured.quantity
insured.quantity
coinsurance.quantity
copay.quantity

uninsured.social_loss
insured.social_loss
coinsurance.social_loss
copay.social_loss

class insurance_plans: 
	def __init__(self, list_price):
		self.list_price = list_price
		list_price = self.list_price
	
	def uninsured(insurance_plans, self_pay = 1):
		self.self_pay = self_pay*list_price
		self_pay = self.self_pay
		self.quantity = 100 - self_pay
	
	def uninsured_price(self, self_pay = 1):
		uninsured_price = self_pay*list_price
		self.uninsured_price = uninsured_price
		
class full(insurance_plans):
    def full(self, list_price, self_pay = 0):
        self.price = self_pay*list_price
        self.quantity = 100 - price
        self.social_loss = lambda self: ((uninsured_price - self_pay)*(quantity -self.uninsured_quantity)/2)

end

class coinsurance(insurance_plans):
	def quantity(self):
		self.self_pay = .5*list_price
		self_pay = self.self_pay
		self.quantity = 100 - self_pay
		quantity = self.quantity
		
	def price(self, self_pay = .5):
		self.coin_price = self_pay
		self_pay = self.coin_price
		
	def social_loss(self_pay = .5, quantity = quantity):
		self.chg_price = lambda chg_price:  uninsured_price - self_pay  
		self.chg_qt = lambda chg_qt: quantity - self.uninsured_quantity 
		self.social_loss = lambda social_loss: (chg_price*chg_qt)/2

class copay(insurance_plans):
	def quantity(self, self_pay = 25):
		self.self_pay = self_pay
		self_pay = self.self_pay
		self.quantity = 100 - self_pay
		quantity = self.quantity
		
	def price(self, self_pay = 25):
		self.price = self_pay
		self_pay = self.price
		
	def social_loss(self_pay = 25, quantity = quantity):
		self.chg_price = lambda chg_price: uninsured_price - self_pay  
		self.chg_qt = lambda chg_qt: quantity - self.uninsured_quantity 
		self.social_loss = lambda social_loss: (chg_price*chg_qt)/2
end

uninsured = dict(insurance_type = "uninsured", quantity = calc_quantity(list_price)),self_pay = list_price, list_price = list_price, price = list_price)