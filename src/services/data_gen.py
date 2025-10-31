"""
Employee Data Generation Service

This module provides functionality for generating synthetic employee data
using the Faker library and random data generation techniques.

Features:
- Generate realistic employee names using Faker
- Random department assignment from predefined list
- Random salary generation within specified range
- Random hire date generation within date range
- Auto-incrementing employee IDs

"""

import random
import logging
import sys
import os
from datetime import date, timedelta
from faker import Faker

# Add the parent directory to the path to enable relative imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.employee import Employee
from utils.constants import DEPARTMENTS, MIN_SALARY, MAX_SALARY, START_DATE, END_DATE


class EmployeeDataGenerator:
    """
    Service class for generating synthetic employee data.

    This class handles the creation of realistic employee records with
    proper data types and validation. It uses Faker for name generation
    and random selection for other fields.

    Attributes:
        fake (Faker): Faker instance for generating realistic names
    """

    def __init__(self):
        """Initialize the data generator with Faker."""
        logging.info("Initializing EmployeeDataGenerator")
        self.fake = Faker()
    
    def generate_random_date(self) -> date:
        """
        Generate a random date between START_DATE and END_DATE.
        
        Returns:
            date: Random date within the specified range
        """
        try:
            days_between = (END_DATE - START_DATE).days
            random_days = random.randint(0, days_between)
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
            employee = Employee(
                emp_id=emp_id,
                full_name=self.fake.name(),
                department=random.choice(DEPARTMENTS),
                salary=round(random.uniform(MIN_SALARY, MAX_SALARY), 2),
                hire_date=self.generate_random_date()
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
            employees = [self.generate_employee(i + 1) for i in range(count)]
            logging.info(f"Successfully generated {count} employees")
            return employees
            
        except Exception as e:
            logging.error(f"Error generating {count} employees: {e}")
            raise