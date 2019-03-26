class Department:

    def __init__(self, name, director, employees, number):
        """
        This method represents a Department object and its attributes
        :param name: str
        :param director: str
        :param empolyees: list of Emploees objects
        :param location: tuple of number of building and name of derpartment
        """
        self.name = name
        self.directior = director
        self.employees = employees
        self.location = Location(number, name)

    def sum_salary(self):
        total = 0
        for emp in self.employees:
            total += emp.get_paid()
        return total


class Location():

    def __init__(self, number, name):
        self.number = number
        self.name = name

    def get_room(self):
        return self.number

    @property
    def get_department(self):
        return self.name

    def __str__(self):
        return "Room {}. Department: {}".format(self.number, self.name)

    def get_location(self):
        return str(self)


class Employee:

    def __init__(self, name, address, birthday, position):
        self.name = name
        self.address = address
        self.birthday = birthday
        self.position = position


class Salaried_emp(Employee):

    def __init__(self, name, address, birthday, position, salary):
        super().__init__(name, address, birthday, position)
        self.salary = salary

    def get_paid(self):
        self.total = self.salary
        return self.total

    def __str__(self):
        return f"{self.__class__.__name__}<{self.name} " + \
            f"lives in {self.address} street. Position: {self.position}. " + \
                f"Birthday: {self.birthday}. Salary per month: ${self.salary}"



class Hourly_emp(Employee):

    def __init__(self, name, adress, birthday, position, hours, pay):
        super().__init__(name, adress, birthday, position)
        self.worked_h = hours
        self.salary_p_h = pay

    def get_paid(self):
        self.total = self.hours * self.pay
        return self.total

    def __repr__(self):
        line = "Hourly_emp<{0} lives in {1}. Position: {2}. Birthday: {3}.".format(self.name,
                                                                                   self.address,
                                                                                   self.position,
                                                                                   self.birthday)
        line += "Salary per hour: ${}. Worked hours per day: {}".format(self.salary_p_h, self.worked_h)
        return line
