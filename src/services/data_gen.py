import random
import logging
from datetime import date, timedelta
from faker import Faker
from models.employee import Employee
from utils.constants import DEPARTMENTS, MIN_SALARY, MAX_SALARY, START_DATE, END_DATE

class EmployeeDataGenerator:
    def __init__(self):
        logging.info("Initializing Employee Data Generator")
        self.fake = Faker()

    def generate_random_date(self) -> date:
        """
        Generate a random date between START_DATE and END_DATE.
        
        Returns:
            date: Random date within the specified range
        """
        try:
            # Calculate total days between start and end
            days_between = (END_DATE - START_DATE).days
            
            # Generate random number of days to add
            random_days = random.randint(0, days_between)
            
            # Return the calculated date
            return START_DATE + timedelta(days=random_days)
        except Exception as e:
            logging.error(f"Error generating random date: {e}")
            raise

    def generate_employee(self, emp_id: int) -> Employee:
        """
        Generate a single employee with the specified ID.
        
        Args:
            emp_id (int): The employee ID to assign
            
        Returns:
            Employee: A new Employee object with generated data
        """
        try:
            # Generate random data
            full_name = self.fake.name()
            department = random.choice(DEPARTMENTS)
            salary = round(random.uniform(MIN_SALARY, MAX_SALARY), 2)
            hire_date = self.generate_random_date()
            
            # Create Employee object
            employee = Employee(
                emp_id=emp_id,
                full_name=full_name,
                department=department,
                salary=salary,
                hire_date=hire_date
            )
            
            logging.debug(f"Generated employee: {employee.full_name} (ID: {emp_id})")
            return employee
            
        except Exception as e:
            logging.error(f"Error generating employee {emp_id}: {e}")
            raise
    
    def generate_employees(self, count: int) -> list[Employee]:
        """
        Generate multiple employees.
        
        Args:
            count (int): Number of employees to generate
            
        Returns:
            list[Employee]: List of generated Employee objects
        """
        try:
            # Generate employees with IDs starting from 1
            employees = [self.generate_employee(i + 1) for i in range(count)]
            
            logging.info(f"Successfully generated {count} employees")
            return employees
            
        except Exception as e:
            logging.error(f"Error generating {count} employees: {e}")
            raise
