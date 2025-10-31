"""
Unit Tests for Employee Data Generator

This module contains unit tests for the employee data generation functionality.
Tests cover data generation, validation, and integration with the main application.

Run with: python -m pytest src/tests/test_gen.py -v

"""

import sys
import os
import pytest
from datetime import date
from unittest.mock import patch, MagicMock

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from models.employee import Employee
from services.data_gen import EmployeeDataGenerator
from utils.constants import (
    DEPARTMENTS, MIN_SALARY, MAX_SALARY,
    START_DATE, END_DATE, MIN_EMPLOYEES, MAX_EMPLOYEES
)


class TestEmployeeDataGenerator:
    """Test cases for EmployeeDataGenerator class."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.generator = EmployeeDataGenerator()

    def test_initialization(self):
        """Test that generator initializes correctly."""
        assert self.generator.fake is not None
        assert hasattr(self.generator, 'generate_random_date')
        assert hasattr(self.generator, 'generate_employee')
        assert hasattr(self.generator, 'generate_employees')

    def test_generate_random_date(self):
        """Test random date generation within valid range."""
        test_date = self.generator.generate_random_date()

        assert isinstance(test_date, date)
        assert START_DATE <= test_date <= END_DATE

    def test_generate_employee(self):
        """Test single employee generation."""
        emp_id = 1
        employee = self.generator.generate_employee(emp_id)

        assert isinstance(employee, Employee)
        assert employee.emp_id == emp_id
        assert isinstance(employee.full_name, str)
        assert len(employee.full_name) > 0
        assert employee.department in DEPARTMENTS
        assert MIN_SALARY <= employee.salary <= MAX_SALARY
        assert START_DATE <= employee.hire_date <= END_DATE

    def test_generate_employees(self):
        """Test bulk employee generation."""
        count = 5
        employees = self.generator.generate_employees(count)

        assert len(employees) == count
        assert all(isinstance(emp, Employee) for emp in employees)

        # Check IDs are sequential starting from 1
        ids = [emp.emp_id for emp in employees]
        assert ids == list(range(1, count + 1))

    def test_generate_employees_large_count(self):
        """Test generation with maximum allowed count."""
        count = 100
        employees = self.generator.generate_employees(count)

        assert len(employees) == count
        assert all(emp.emp_id == i + 1 for i, emp in enumerate(employees))

    def test_employee_data_variety(self):
        """Test that generated data has variety."""
        count = 50
        employees = self.generator.generate_employees(count)

        # Check that we get different names
        names = [emp.full_name for emp in employees]
        assert len(set(names)) > len(names) * 0.8  # At least 80% unique names

        # Check department distribution
        departments = [emp.department for emp in employees]
        assert len(set(departments)) > 1  # Multiple departments used

    def test_salary_range(self):
        """Test that salaries are within specified range."""
        count = 20
        employees = self.generator.generate_employees(count)

        salaries = [emp.salary for emp in employees]
        assert all(MIN_SALARY <= salary <= MAX_SALARY for salary in salaries)

        # Check salary precision (should be rounded to 2 decimal places)
        assert all(salary == round(salary, 2) for salary in salaries)

    def test_hire_date_range(self):
        """Test that hire dates are within specified range."""
        count = 20
        employees = self.generator.generate_employees(count)

        hire_dates = [emp.hire_date for emp in employees]
        assert all(START_DATE <= hire_date <= END_DATE for hire_date in hire_dates)


class TestEmployeeModel:
    """Test cases for Employee dataclass."""

    def test_employee_creation(self):
        """Test Employee object creation."""
        emp = Employee(
            emp_id=1,
            full_name="John Doe",
            department="IT",
            salary=75000.50,
            hire_date=date(2023, 1, 15)
        )

        assert emp.emp_id == 1
        assert emp.full_name == "John Doe"
        assert emp.department == "IT"
        assert emp.salary == 75000.50
        assert emp.hire_date == date(2023, 1, 15)

    def test_employee_to_dict(self):
        """Test Employee to_dict conversion."""
        emp = Employee(
            emp_id=1,
            full_name="John Doe",
            department="IT",
            salary=75000.50,
            hire_date=date(2023, 1, 15)
        )

        data = emp.to_dict()
        expected = {
            'emp_id': 1,
            'full_name': "John Doe",
            'department': "IT",
            'salary': 75000.50,
            'hire_date': date(2023, 1, 15)
        }

        assert data == expected


class TestIntegration:
    """Integration tests combining multiple components."""

    def test_full_workflow(self):
        """Test complete data generation workflow."""
        generator = EmployeeDataGenerator()
        employees = generator.generate_employees(10)

        assert len(employees) == 10

        # Test that all employees can be converted to dict
        for emp in employees:
            data = emp.to_dict()
            assert isinstance(data, dict)
            assert 'emp_id' in data
            assert 'full_name' in data
            assert 'department' in data
            assert 'salary' in data
            assert 'hire_date' in data


if __name__ == '__main__':
    # Run tests if executed directly
    pytest.main([__file__, '-v'])