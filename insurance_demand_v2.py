# -*- coding: utf-8 -*-
"""
This is a program to calculate attributes belonging to insurance plans.
"""

class InsurancePlans:
    """
    This is a class for insurance plans.    
    Attributes: 
        list price (float): The price at which the service is offered.
        intercept (float): The intercept of the demand function.
    """
    def __init__(self, list_price, intercept=100, perc_coverage=1.00):
        self.list_price = list_price
        self.intercept = intercept
        self.perc_coverage = perc_coverage

    def uninsured(self, list_price, uninsured_perc=1.00):
        """ 
        This is a method to define and calculate the base state - uninsured.
        Attributes:
            uninsured_price (float)
            uninsured_quantity (int)
            uninsured_perc (float)
            """
        uninsured_price = uninsured_perc*list_price
        uninsured_quantity = self.intercept - self.uninsured_price*self.list_price
        
    def demand_function(x_value, intercept=100, slope=1):
        intercept = intercept
        slope = slope
        x_value = x_value
        y_value = intercept + slope*x_value
        return y_value
    
class Full(InsurancePlans):
    """ 
    This is a class for full insurance plans.
    Attributes:
            price (float)
            intercept (float)
            uninsured_perc (float)
    """
    
    def __init__(self, list_price, intercept=100, self_pay=0.00):
        InsurancePlans.__init__(self, list_price, intercept)
        self.self_pay = self_pay

    def quantity(self):
        quantity = self.intercept - self.self_pay*self.list_price
        return quantity
    
    def social_loss(self):
        social_loss = .5*self.list_price**2*(self.uninsured_price - self.self_pay)**2
        return social_loss
    
class Coinsure(InsurancePlans):
    """ 
    This is a class for coinsurance plans.
    Attributes:
            price (float)
            intercept (float)
            uninsured_perc (float)
    """
    
    def __init__(self, list_price, intercept=100, self_pay=.5):
        InsurancePlans.__init__(self, list_price, intercept)
        self.self_pay = self_pay

    def calc_quantity(self):
        quantity = self.intercept - self.self_pay*self.list_price
        return quantity
    
    def social_loss(self):
        social_loss = .5*(self.list_price*(1-self.self_pay))**2
        return social_loss
    
class Copay(InsurancePlans):
    """ 
    This is a class for copay plans.    
    """

    def __init__(self, list_price, intercept=100, self_pay=25):
        InsurancePlans.__init__(self, list_price, intercept)
        self.self_pay = self_pay

    def quantity(self):
        quantity = self.intercept - self.self_pay
        return quantity
    
    def social_loss(self):
        social_loss = .5*(self.list_price-self.self_pay)**2
        return social_loss