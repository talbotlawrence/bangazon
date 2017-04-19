from bangazon import *
import random

class HumanResources(Department, PartTime):
    """Class for representing Human Resources department

    Methods: __init__, add_policy, get_policy, etc.
    """

    def __init__(self, name, supervisor, employee_count, location, meet):
        super().__init__(name, supervisor, employee_count, location, meet)
        self.policies = set()
        PartTime.__init__(self)

    def add_policy(self, policy_name, policy_text):
        """Adds a policy, as a tuple, to the set of policies

        Arguments:
        policy_name (string)
        policy_text (string)
        """
        self.policies.add((policy_name, policy_text))

    def meet(self):
        """This is my override"""
        print("Everybody meet in Jerry\'s office.")

    def get_budget(self):
        self.budget = super().get_budget() - 500000
        print("You guys don\'t need that much money!")

##########################################################################################################

class InformationTechnology(Department, FullTime):
    """Class for representing the IT department

    Methods: __init__, standard_response_to_all_incoming_tickets, number_of_tickets_submitted  
    """

    def __init__(self, name, supervisor, employee_count, location, meet):
        super().__init__(name, supervisor, employee_count, location, meet)
        FullTime.__init__(self)

    def standard_response_to_all_incoming_tickets(self):
        print("Did you reboot your computer?  Could you please?")

    def number_of_tickets_submitted(self, ticket_count):
        if not isinstance(ticket_count, int):
            raise TypeError('Please provide a number for the ticket count!')
        print("We have {} tickets to close".format(self.ticket_count))

    def meet(self):
        """This is my override"""
        print("We don\'t have meetings; we improvise!!!")

    def get_budget(self):
        self.budget = super().get_budget() + 10000
        print("Spend it all!")

##########################################################################################################

class Sales(Department, FullTime):
"""Class for representing the Sales department

Methods: __init__, number_of_sales_this_month
"""

    def __init__(self, name, supervisor, employee_count, location, meet):
        super().__init__(name, supervisor, employee_count, location, meet)
        FullTime.__init__(self)

    def number_of_sales_this_month(self, number):
        if not isinstance(number, int):
            raise TypeError('Please provide a number for the employees being investigated!')
        print("{} sales!  That\'s it?".format(self.number))

    def meet(self):
        """This is my override"""
        print("On second thought, let\'s have our meeting at Starbucks!")

    def get_budget(self):
        self.budget = super().get_budget() + 10000
        print("Always be closing with your new iPads.")


##########################################################################################################

class InternalAudit(Department, PartTime)
"""Class for representing the Internal Audit department

Methods: __init__, number_of_employees_being_investigated
"""

    def __init__(self, name, supervisor, employee_count, location, meet):
        super().__init__(name, supervisor, employee_count, location, meet)
        PartTime.__init__(self)

    def number_of_employees_being_investigated(self, number):
        if not isinstance(number, int):
            raise TypeError('Please provide a number for the employees being investigated!')
        print("{} people have been stealing from the company".format(self.number))

    def meet(self):
        """This is my override"""
        print("Meetings are a waste of time: throw all comments into chat!")

    def get_budget(self):
        self.budget = super().get_budget() + 2000
        print("Pays for the licensing for the CatchYourAss software!")



##########################################################################################################

class Employee(Department):
    """Class representing the individual employee"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name + " " + self.last_name

#This method below is not working
    def eat(self, food=None, *companions):
        restaurant = ['J. Alexander\'s', 'Ruth\'s Chris', 'Stoney River', 'The Waffle House', 'Burger King']
        one_restaurant = random.choice(restaurant)
        if food and companions:
            print("{} is at {}, has ordered {}, and {} is dining there as well".format(full_name, one_restaurant, food, companions[0]))
        elif food is not None and companions is None:
            print("{} took his {} back to the office".format(full_name, food))
        elif food is None and companions is not None:
            print("{} is at {} and {} will be joining".format(full_name, one_restaurant, companions))
        else:
            print("{} is eating at {} right this very minute!!!".format(full_name, one_restaurant))
        return one_restaurant

##########################################################################################################

class FullTime():
  """Describes full-time employees"""
  
  def __init__(self):
    self.hours_per_week = 40


class PartTime():
  """Describes part-time employees"""

  def __init__(self):
    self.hours_per_week = 24

##########################################################################################################

class SecurityAccess():
    """Describes which employees can get in the building and which ones cannot"""

    def __init__(self):
        self.clearance = True

    def granted(self, name):
        self.clearance = True
        self.name = name
        print("{} has access to the War Room".format(self.name))

    def denied(self, name):
        self.name = name
        print("{} does not have access!".format(self.name))


##########################################################################################################

if __name__ == '__main__':
    hr = HumanResources('Talbot', 'Gilbert', 15)
    hr.add_policy('No Smoking', 'You cannot smoke at this company unless your name is Steve!')
    it = InformationTechnology('Jen', 'Meg', 98, 'The War Room')
    it.standard_response_to_all_incoming_tickets()
    it.number_of_tickets_submitted(8)
    sales = Sales('Maddie', 'Brenda', 3, 'The Boiler Room')
    sales.number_of_sales_this_month(1000)
    ia = InternalAudit('Jen', 'The boss', 12, 'The White House')
    ia.number_of_employees_being_investigated(34)