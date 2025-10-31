# Employee Data Generator

A PySide6 desktop application for generating synthetic employee data and exporting it to Excel format.

## Features

- **Data Generation**: Generate realistic employee data including names, departments, salaries, and hire dates
- **Excel Export**: Export data to Excel with both detailed employee sheet and summary statistics
- **User-Friendly GUI**: Intuitive interface for easy operation
- **Folder Selection**: Choose custom export locations
- **Data Validation**: Input validation and error handling

## Requirements

- Python 3.8+
- PySide6
- pandas
- openpyxl
- faker

## Installation 

1. Download the executable
    - Download the pre-built EmployeeApp.exe file from the repository or provided link.

2. Run the application
    - Double-click EmployeeApp.exe to launch the app.
    - No Python installation or dependencies are required on the user machine.
   

## How to use app

1. **Enter Employee Count**: Input the number of employees to generate (1-1000)
2. **Select Folder**: Choose the export destination folder
3. **Generate Data**: Click "Generate Data" to create synthetic employee records
4. **Export to Excel**: Click "Export to Excel" to save the data

## Data in Excel

- **emp_id**: Auto-incrementing integer starting from 1
- **full_name**: Realistic full name generated using Faker
- **department**: Random selection from 5 departments (IT, HR, Operations, Administration, Finance)
- **salary**: Random value between 25,000 and 120,000
- **hire_date**: Random date between 2020-01-01 and today

## Excel Output

The application creates `employees.xlsx` with two sheets:

### Employees Sheet
Contains all generated employee data in tabular format.

### Summary Sheet
Shows average salary per department plus export timestamp.

## Project Structure

```
Employee_App/
├── src/
│   ├── main.py                 # Application entry point
│   ├── ui/
│   │   └── main_window.py      # Main GUI window
│   ├── models/
│   │   └── employee.py         # Employee data model
│   ├── services/
│   │   ├── data_gen.py         # Data generation service
│   │   └── excel_export.py     # Excel export service
│   ├── utils/
│   │   └── constants.py        # Application constants
│   └── tests/                  # Unit tests
├── README.md                   # This file
└── .gitignore
```

## Architecture

- **MVC Pattern**: Separates data (models), presentation (ui), and business logic (services)
- **Modular Design**: Each component has a single responsibility
- **Error Handling**: Comprehensive logging and user-friendly error messages
- **Extensible**: Easy to add new features or modify existing functionality

## Development

The application is built with:
- **PySide6**: Modern Qt bindings for Python
- **Dataclasses**: For clean data model definitions
- **Logging**: Comprehensive application logging
- **Type Hints**: Full type annotation for better code maintainability

## License

This project is open source. Feel free to use and modify as needed.

## Author

Rolando Celeste
