# -*- coding: utf-8 -*-
"""
This is a program to calculate attributes belonging to insurance plans.
"""

class InsurancePlans:
    """
    This is a class for insurance plans.
    """
    def __init__(self, list_price, deductible, benefit):
        self.list_price = list_price
        self.deductible = deductible
        self.benefit = benefit

    def uninsured_price(self, uninsured_perc=1.00):
        """
        Calculates the price demanded in uninsured state
        """
        uninsured_price = uninsured_perc*self.list_price
        return uninsured_price

    @classmethod
    def uninsured_qty(cls, intercept=1, slope=1):
        """
        Calculates quantity demanded in uninsured state
        """
        uninsured_quantity = intercept - slope*cls.uninsured_price
        return uninsured_quantity

class Full(InsurancePlans):
    """
    This is a class for full insurance plans.
    """
    def self_pay(self, perc_cov=1):
        """
        Calculates the self_pay amount if different than zero.
        """
        return (1-perc_cov)*self.list_price

    def quantity(self, intercept=100, perc_cov=1):
        """
        This method calculates the quantity demanded of full insurance plans
        """
        return intercept - perc_cov*self.list_price

    def social_loss(self, cls):
        """
        This method calculates the social loss from the uninsured state.
        """
        return .5*self.list_price**2*(cls.uninsured_price - cls.self_pay)**2

    def unfair_premium(self):
        """
        Calculates the unfair full insurance premium
        """
        pass

    def fair_premium(self):
        """
        Calculates the fair full insurance premium
        """
        pass

class Coinsure(InsurancePlans):
    """
    This is a class for coinsurance plans.
    """
    def __init__(self, list_price, deductible, benefit, perc_cover=.5):
        InsurancePlans.__init__(self, list_price, deductible, benefit)
        self.perc_cover = perc_cover
        self.self_pay = 1 - perc_cover

    def quantity(self, intercept=100):
        """
        This method calculates the quantity demanded of coinsurance insurance policies.
        """
        return intercept- self.self_pay*self.list_price

    def social_loss(self):
        """
        This method calculates the social loss from the uninsured state.
        """
        return .5*(self.list_price*(1-self.self_pay))**2

    def unfair_premium(self):
        """
        Calculates the unfair full insurance premium
        """
        pass

    def fair_premium(self):
        """
        Calculates the fair full insurance premium
        """
        pass

class Copay(InsurancePlans):
    """
    This is a class for copay plans.
    """
    def __init__(self, list_price, deductible, benefit, copay=25):
        InsurancePlans.__init__(self, list_price, deductible, benefit)
        self.copay = copay

    def quantity(self, intercept=100):
        """
        This method calculates the quantity demanded of copay insurance policies.
        """
        return intercept - self.copay

    def social_loss(self):
        """
        This method calculates the social loss from the uninsured state.
        """
        return .5*(self.list_price-self.copay)**2

    def unfair_premium(self):
        """
        Calculates the unfair full insurance premium
        """
        pass

    def fair_premium(self):
        """
        Calculates the fair full insurance premium
        """
        pass
    