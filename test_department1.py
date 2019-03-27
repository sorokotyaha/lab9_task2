import unittest
from department import Department, Salaried_emp, Hourly_emp, Employee, Location


class TestSquare_preceding(unittest.TestCase):
	def test_ini(self): #тут був __init__ замість test_init
		emp_1 = Salaried_emp("Denis", "Shevchenka", "06.09.2001",
							 "head", 120000)
		emp_2 = Hourly_emp("Viktor", "Stryiska", "24.04.2001",
						   "analyst", 12, 180)
		self.employees = (emp_1, emp_2)
		self.location = Location(8, "BA")
		self.department = Department("BA", "Denis", self.location, self.employees)

	def test_all_in_one(self):
		loc_1 = Location(8, "BA")
		assert ("Room 8. Department: BA" == str(loc_1))
		assert (8 == loc_1.get_room())
		assert (loc_1.get_department == "BA")

		emp_1 = Salaried_emp("Denis", "Shevchenka", "06.09.2001",
							 "head", 120000)
		emp_2 = Hourly_emp("Viktor", "Stryiska", "24.04.2001",
						   "analyst", 12, 180)

		assert (isinstance(emp_1, Employee))
		assert (isinstance(emp_2, Employee))
		assert (emp_1.name == "Denis")
		assert ("Shevchenka" == emp_1.address)
		assert ("06.09.2001" == emp_1.birthday)
		assert ("head" == emp_1.position)
		assert (120000 == emp_1.salary)
		assert (12 == emp_2.worked_h)
		assert (180 == emp_2.salary_p_h)
		assert ((str(
			emp_1) == "Salaried_emp<Denis lives in Shevchenka street. Position: head. Birthday: 06.09.2001. Salary per month: $120000"))
		assert ((str(
			emp_1) == "Hourly_emp<Viktor lives in Stryiska street. Position: analyst. Birthday: 24.04.2001. Salary per hour: $180. Worked hours per day: 12")) # changes to 180

		employee_list = (emp_1, emp_2)

		dep_1 = Department("BA", "Denis", loc_1, employee_list)
		# workers should be in tuple
		assert (isinstance(dep_1.workers, tuple))
		# location must be instance of Location class
		assert (isinstance(dep_1.location, Location))
		assert (dep_1.get_location() == "Room 8. Department: BA")
		assert (dep_1.sum_salary() == 60000)
		assert (dep_1.get_inf_workers() == "Denis lives in Shevchenka street. Position: manager. Birthday: 06.09.2001. Salary per month: $30000\nHourly_emp<Viktor lives in Stryiska street. Position: analyst. Birthday: 24.04.2001. Salary per hour: $180. Worked hours per day: $1000")



if __name__ == '__main__':
    unittest.main()