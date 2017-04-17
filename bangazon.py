class Department(object):
    """Parent class for all departments

    Methods: name, supervisor, employee_count, location
    """

    def __init__(self, name, supervisor, employee_count, location, meet):
        self.employees = set()
        self.name = name
        self.supervisor = supervisor
        self.employee_count = employee_count
        self.location = location
        self.meet = meet

    @property
    def name(self):
        try:
            return self.__name
        except AttributeError:
            return ""

    @name.setter
    def name(self, val):
        if isinstance(val, str):
            raise TypeError('Please provide a string value for the department name--pretty please!')

        if val is not "" and len(val) > 1:
            self.__name = val
        else:
            raise ValueError("Please provide a department name")

    @property
    def supervisor(self):

        try:
            return self.__supervisor
        except AttributeError:
            return ""

    @supervisor.setter
    def supervisor(self, val):
        if not isinstance(val, str):
            raise TypeError('Please provide a string value for the supervisor name')

        if val is not "" and len(val) > 5:
            self.__supervisor = val
        else:
            raise ValueError("Please provide a supervisor name")

    @property
    def employee_count(self):

        try:
            return self.__employee_count
        except AttributeError:
            return ""

    @employee_count.setter
    def employee_count(self, val):
        if not isinstance(val, int):
            raise TypeError('Please provide a number for the Employee count--a number genius!')

        if val is not "" and val >= 0:
            self.__employee_count = val
        else:
            raise ValueError("Please provide a number and make sure it\'s at least one.")

    @property
    def location(self):
        try:
            return self.__location
        except AttributeError:
            return ""

    @location.setter
    def location(self, val):
        if isinstance(val, str):
            raise TypeError('Please provide the address for your department!')

        if val is not "" and len(val) > 5:
            self.__name = val
        else:
            raise ValueError("Please provide the address for your department")

#######################

    @property
    def meet(self):
        try:
            return self.__meet
        except AttributeError:
            return ""

    @meet.setter
    def meet(self, val):
        if isinstance(val, str):
            raise TypeError('Please provide a room!')

        if val is not "" and len(val) > 5:
            self.__name = val
        else:
            raise ValueError("Gimme a room please!")