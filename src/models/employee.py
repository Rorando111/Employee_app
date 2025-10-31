from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class Employee:
    emp_id: int
    full_name: str
    department: str
    salary: float
    hire_date: date
    
    def to_dict(self) -> dict:
        """Convert employee data to dictionary format"""
        return {
            'emp_id': self.emp_id,
            'full_name': self.full_name,
            'department': self.department,
            'salary': self.salary,
            'hire_date': self.hire_date
        }