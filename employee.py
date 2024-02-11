from Departments import Departments


class Employee(Exception):
    emp_department = ""

    def __init__(self, emp_id: int, emp_name: str, hourly_rate: int):
        if hasattr(emp_id) and hasattr(emp_name) and hasattr(hourly_rate):
            self.emp_id = emp_id
            self.emp_name = emp_name
            self.hourly_rate = hourly_rate
        else:
            raise ValueError("You must enter your name,id, and hourly rate")

    def emp_assign_department(self, ):
        self.emp_department = Departments.CUSTOMER_CARE.value
        return self.emp_department

    def set_employee_name(self, emp_name: str):
        self.emp_name = emp_name

    def get_employee_name(self, ):
        return self.emp_name

    def set_employee_id(self, emp_id: int):
        self.emp_id = emp_id

    def get_employee_id(self):
        return self.emp_id

    def set_number_of_hours_worked(self, number_hours_worked: int):
        if number_hours_worked > 200:
            raise ValueError("hours worked must be less than or equal to 200")
        return number_hours_worked

    def calculate_emp_salary(self, number_of_hours_worked):
        number_of_hours_worked = self.set_number_of_hours_worked(number_of_hours_worked)
        if number_of_hours_worked <= 0:
            return 0
        else:
            return self.hourly_rate * number_of_hours_worked

    def __str__(self):
        return f"""Employee ID:{self.get_employee_id()}
               \nEmployee Name :{self.get_employee_name()}
        """


employee = Employee(2, "Abby", 500)

print(employee.emp_assign_department())
