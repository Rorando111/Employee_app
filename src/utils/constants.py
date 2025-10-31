"""
Application Constants

This module contains all constant values used throughout the Employee Data Generator application.
Centralizing constants here makes them easy to maintain and modify.

Author: Kilo Code
"""

from datetime import date

# Employee data generation constants
DEPARTMENTS = ["IT", "HR", "Operations", "Administration", "Finance"]
"""
List of available departments for employee assignment.
These are the 5 fixed departments as specified in requirements.
"""

MIN_SALARY = 25000.0
"""
Minimum salary value for random salary generation.
"""

MAX_SALARY = 120000.0
"""
Maximum salary value for random salary generation.
"""

START_DATE = date(2020, 1, 1)
"""
Start date for random hire date generation.
"""

END_DATE = date.today()
"""
End date for random hire date generation (current date).
"""

# UI constants
MAX_EMPLOYEES = 1000
"""
Maximum number of employees that can be generated in a single operation.
"""

MIN_EMPLOYEES = 1
"""
Minimum number of employees that can be generated.
"""

# File and export constants
EXCEL_FILENAME = "employees.xlsx"
"""
Default filename for the exported Excel file.
"""

EMPLOYEES_SHEET_NAME = "Employees"
"""
Name of the main data sheet in the Excel file.
"""

SUMMARY_SHEET_NAME = "Summary"
"""
Name of the summary sheet with department averages.
"""

# Logging
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
"""
Format string for logging messages.
"""

LOG_LEVEL = 'DEBUG'
"""
Default logging level for the application.
"""