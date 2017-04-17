from bangazon import *

class HumanResources(Department):
    """Class for representing Human Resources department

    Methods: __init__, add_policy, get_policy, etc.
    """

    def __init__(self, name, supervisor, employee_count, meet):
        super().__init__()      #do I need to add anything here in the ()?
        self.policies = set()

    def add_policy(self, policy_name, policy_text):
    """Adds a policy, as a tuple, to the set of policies

    Arguments:
    policy_name (string)
    policy_text (string)
    """

        self.policies.add((policy_name, policy_text))

##########################################################################################################

class InformationTechnology(Department):
    """Class for representing the IT department

    Methods: __init__, standard_response_to_all_incoming_tickets, number_of_tickets_submitted  
    """

    def __init__(self, name, supervisor, employee_count, location, meet):
        super().__init__(name, supervisor, employee_count, location, meet)
        self.name = name
        self.supervisor = supervisor
        self.employee_count = employee_count
        self.location = location

    def standard_response_to_all_incoming_tickets(self):
        print("Did you reboot your computer?  Could you please?")

    def number_of_tickets_submitted(self, ticket_count):
        if not isinstance(ticket_count, int):
            raise TypeError('Please provide a number for the ticket count!')
        print("We have {} tickets to close".format(self.ticket_count))

##########################################################################################################

class Sales(Department):
"""Class for representing the Sales department

Methods: __init__, number_of_sales_this_month
"""

    def __init__(self, name, supervisor, employee_count, location, meet):
        super().__init__(name, supervisor, employee_count, location, meet)
        self.name = name
        self.supervisor = supervisor
        self.employee_count = employee_count
        self.location = location

    def number_of_sales_this_month(self, number):
        if not isinstance(number, int):
            raise TypeError('Please provide a number for the employees being investigated!')
        print("{} sales!  That\'s it?".format(self.number))

    def meet(self):
        """This is my override"""
        print("On second thought, let\'s have our meeting at Starbucks!")


##########################################################################################################

class InternalAudit(Department):
"""Class for representing the Internal Audit department

Methods: __init__, number_of_employees_being_investigated
"""

    def __init__(self, name, supervisor, employee_count, location):
        super().__init__(name, supervisor, employee_count, location)
        self.name = name
        self.supervisor = supervisor
        self.employee_count = employee_count
        self.location = location

    def number_of_employees_being_investigated(self, number):
        if not isinstance(number, int):
            raise TypeError('Please provide a number for the employees being investigated!')
        print("{} people have been stealing from the company".format(self.number))

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