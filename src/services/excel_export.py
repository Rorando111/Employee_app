"""
Excel Export Service

This module handles exporting employee data to Excel format with
summary statistics and proper formatting.

Features:
- Export employee data to Excel with proper formatting
- Create summary sheet with department averages
- Add export timestamp for audit trail
- Handle large datasets efficiently

Author: Kilo Code
"""

import logging
import os
import sys
from datetime import datetime
from typing import List
import pandas as pd

# Add the parent directory to the path to enable relative imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.employee import Employee
from utils.constants import EXCEL_FILENAME, EMPLOYEES_SHEET_NAME, SUMMARY_SHEET_NAME

class ExcelExporter:
    """
    Handles exporting employee data to Excel format with summary statistics.
    """
    
    def __init__(self):
        logging.info("Initializing ExcelExporter")

    def _employees_to_dataframe(self, employees: List[Employee]) -> pd.DataFrame:
        """
        Convert list of Employee objects to pandas DataFrame.
        
        Args:
            employees: List of Employee objects
            
        Returns:
            pd.DataFrame: DataFrame with employee data
        """
        try:
            # Convert each employee to dictionary using the to_dict method
            data = [emp.to_dict() for emp in employees]
            
            # Create DataFrame
            df = pd.DataFrame(data)
            
            # Ensure proper column order
            df = df[['emp_id', 'full_name', 'department', 'salary', 'hire_date']]
            
            logging.debug(f"Created DataFrame with {len(df)} rows")
            return df
            
        except Exception as e:
            logging.error(f"Error converting employees to DataFrame: {e}")
            raise
    
    def _create_summary_data(self, employees: List[Employee]) -> pd.DataFrame:
        """
        Create summary statistics showing average salary per department.
        
        Args:
            employees: List of Employee objects
            
        Returns:
            pd.DataFrame: Summary DataFrame with department averages
        """
        try:
            # Convert to DataFrame first
            df = self._employees_to_dataframe(employees)
            
            # Group by department and calculate average salary
            summary = df.groupby('department')['salary'].agg(['mean', 'count']).round(2)
            summary = summary.rename(columns={'mean': 'avg_salary', 'count': 'employee_count'})
            summary = summary.reset_index()
            
            # Sort by department name
            summary = summary.sort_values('department')
            
            # Add export timestamp
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            timestamp_row = pd.DataFrame({
                'department': ['Export Timestamp'],
                'avg_salary': [None],
                'employee_count': [timestamp]
            })
            
            # Combine summary with timestamp
            summary = pd.concat([summary, timestamp_row], ignore_index=True)
            
            logging.debug("Created summary data")
            return summary
            
        except Exception as e:
            logging.error(f"Error creating summary data: {e}")
            raise
    
    def export_to_excel(self, employees: List[Employee], folder_path: str) -> str:
        """
        Export employee data to Excel file with two sheets.
        
        Args:
            employees: List of Employee objects to export
            folder_path: Directory path where to save the Excel file
            
        Returns:
            str: Full path to the created Excel file
            
        Raises:
            Exception: If export fails
        """
        try:
            if not employees:
                raise ValueError("No employee data to export")
            
            # Create file path
            file_path = os.path.join(folder_path, EXCEL_FILENAME)
            
            logging.info(f"Starting Excel export to: {file_path}")
            
            # Create DataFrames
            employees_df = self._employees_to_dataframe(employees)
            summary_df = self._create_summary_data(employees)
            
            # Create Excel writer
            with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
                # Write Employees sheet
                employees_df.to_excel(
                    writer, 
                    sheet_name=EMPLOYEES_SHEET_NAME, 
                    index=False,
                    startrow=0
                )
                
                # Write Summary sheet
                summary_df.to_excel(
                    writer, 
                    sheet_name=SUMMARY_SHEET_NAME, 
                    index=False,
                    startrow=0
                )
            
            logging.info(f"Successfully exported {len(employees)} employees to {file_path}")
            return file_path
            
        except Exception as e:
            logging.error(f"Error exporting to Excel: {e}")
            raise
