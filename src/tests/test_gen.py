import sys
import random
from datetime import date, timedelta
from dataclasses import dataclass
from faker import Faker
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, 
    QPushButton, QSpinBox, QLabel, QFileDialog
)

# Constants
DEPARTMENTS = ['IT', 'HR', 'Operations', 'Administration', 'Finance']
MIN_SALARY = 25000
MAX_SALARY = 120000
START_DATE = date(2020, 1, 1)
END_DATE = date.today()

@dataclass
class Employee:
    emp_id: int
    full_name: str
    department: str
    salary: float
    hire_date: date
    
    def to_dict(self):
        return vars(self)

class EmployeeDataGenerator:
    def __init__(self):
        self.fake = Faker()
    
    def generate_random_date(self) -> date:
        days_between = (END_DATE - START_DATE).days
        random_days = random.randint(0, days_between)
        return START_DATE + timedelta(days=random_days)
    
    def generate_employees(self, count: int) -> list[Employee]:
        return [
            Employee(
                emp_id=i+1,
                full_name=self.fake.name(),
                department=random.choice(DEPARTMENTS),
                salary=round(random.uniform(MIN_SALARY, MAX_SALARY), 2),
                hire_date=self.generate_random_date()
            ) for i in range(count)
        ]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Employee Data Generator")
        self.setMinimumSize(400, 200)
        
        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        
        # Number of employees input
        self.count_input = QSpinBox()
        self.count_input.setRange(1, 1000)
        self.count_input.setValue(10)
        layout.addWidget(QLabel("Number of Employees:"))
        layout.addWidget(self.count_input)
        
        # Generate button
        self.generate_btn = QPushButton("Generate Data")
        self.generate_btn.clicked.connect(self.generate_data)
        layout.addWidget(self.generate_btn)
        
        # Status label
        self.status_label = QLabel("")
        layout.addWidget(self.status_label)
        
        # Initialize generator
        self.generator = EmployeeDataGenerator()
        self.employees = []

    def generate_data(self):
        count = self.count_input.value()
        self.employees = self.generator.generate_employees(count)
        self.status_label.setText(f"Generated {count} employee records")
        
        # Print sample data (for testing)
        for emp in self.employees[:5]:  # Show first 5 employees
            print(f"\nEmployee ID: {emp.emp_id}")
            print(f"Name: {emp.full_name}")
            print(f"Department: {emp.department}")
            print(f"Salary: ${emp.salary:,.2f}")
            print(f"Hire Date: {emp.hire_date}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()