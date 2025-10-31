"""
Employee Data Generator - Main Window UI

This module contains the main window implementation for the Employee Data Generator application.
The UI provides controls for generating synthetic employee data and exporting it to Excel.

Features:
- Input field for number of employees to generate
- Folder selection for Excel export location
- Buttons for data generation and export
- Status display for user feedback

"""

import logging
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QFileDialog, QMessageBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPalette, QColor
from utils.constants import DEFAULT_EMPLOYEE_COUNT


class MainWindow(QMainWindow):
    """
    Main application window for the Employee Data Generator.

    This class creates and manages the user interface components including:
    - Employee count input field
    - Folder selection controls
    - Action buttons (Generate Data, Export to Excel)
    - Status display area

    Attributes:
        employee_count_input (QLineEdit): Input field for number of employees
        folder_path_label (QLabel): Display for selected folder path
        status_label (QLabel): Status message display
        generate_button (QPushButton): Button to generate employee data
        export_button (QPushButton): Button to export data to Excel
        select_folder_button (QPushButton): Button to choose export folder
        selected_folder (str): Currently selected folder path for export
        employee_data (list): Generated employee data (Employee objects)
    """

    def __init__(self):
        """
        Initialize the main window and set up the UI components.
        """
        super().__init__()
        logging.info("Initializing MainWindow")

        # Initialize data storage
        self.selected_folder = ""
        self.employee_data = []

        # Set up window properties
        self.setWindowTitle("Employee Data Generator")
        self.setGeometry(100, 100, 500, 300)
        self.setMinimumSize(450, 250)

        # Set up the central widget and layout
        self._setup_ui()

        # Connect button signals to slots
        self._connect_signals()

        self.employee_count_input.setText(str(DEFAULT_EMPLOYEE_COUNT))

        logging.info("MainWindow initialized successfully")

    def _setup_ui(self):
        """
        Set up the user interface components and layout.
        """
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main vertical layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Title
        title_label = QLabel("Employee Data Generator")
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # Employee count input section
        count_layout = QHBoxLayout()
        count_label = QLabel("Number of Employees:")
        count_label.setMinimumWidth(150)
        self.employee_count_input = QLineEdit()
        self.employee_count_input.setPlaceholderText("Enter number (1-1000)")
        self.employee_count_input.setMaximumWidth(200)
        count_layout.addWidget(count_label)
        count_layout.addWidget(self.employee_count_input)
        count_layout.addStretch()
        main_layout.addLayout(count_layout)

        # Folder selection section
        folder_layout = QHBoxLayout()
        folder_label = QLabel("Export Folder:")
        folder_label.setMinimumWidth(150)
        self.folder_path_label = QLabel("No folder selected")
        self.folder_path_label.setStyleSheet("border: 1px solid #ccc; padding: 5px; background-color: #f9f9f9;")
        self.select_folder_button = QPushButton("Select Folder")
        self.select_folder_button.setMaximumWidth(100)
        folder_layout.addWidget(folder_label)
        folder_layout.addWidget(self.folder_path_label, 1)
        folder_layout.addWidget(self.select_folder_button)
        main_layout.addLayout(folder_layout)

        # Action buttons section
        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch()

        self.generate_button = QPushButton("Generate Data")
        self.generate_button.setMinimumWidth(120)
        self.generate_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 8px 16px;
                border: none;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:disabled {
                background-color: #cccccc;
            }
        """)

        self.export_button = QPushButton("Export to Excel")
        self.export_button.setMinimumWidth(120)
        self.export_button.setEnabled(False)  # Initially disabled
        self.export_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                padding: 8px 16px;
                border: none;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
            QPushButton:disabled {
                background-color: #cccccc;
            }
        """)

        buttons_layout.addWidget(self.generate_button)
        buttons_layout.addWidget(self.export_button)
        buttons_layout.addStretch()
        main_layout.addLayout(buttons_layout)

        # Status display section
        status_title = QLabel("Status:")
        status_title.setStyleSheet("font-weight: bold;")
        main_layout.addWidget(status_title)

        self.status_label = QLabel("Ready to generate employee data")
        self.status_label.setStyleSheet("""
            QLabel {
                border: 1px solid #ddd;
                padding: 10px;
                background-color: #f0f8ff;
                border-radius: 4px;
                min-height: 20px;
            }
        """)
        self.status_label.setWordWrap(True)
        main_layout.addWidget(self.status_label)

        # Add stretch to push everything to the top
        main_layout.addStretch()

    def _connect_signals(self):
        """
        Connect UI signals to their respective slot methods.
        """
        self.select_folder_button.clicked.connect(self._select_folder)
        self.generate_button.clicked.connect(self._generate_data)
        self.export_button.clicked.connect(self._export_to_excel)

    def _select_folder(self):
        """
        Open a folder selection dialog and update the selected folder path.
        """
        try:
            folder = QFileDialog.getExistingDirectory(
                self,
                "Select Export Folder",
                self.selected_folder or ""
            )

            if folder:
                self.selected_folder = folder
                # Display only the folder name for brevity
                import os
                folder_name = os.path.basename(folder)
                self.folder_path_label.setText(f"{folder_name}/")
                self.folder_path_label.setToolTip(folder)  # Full path as tooltip

                # Enable export button if we have data
                if self.employee_data:
                    self.export_button.setEnabled(True)

                self._update_status("Folder selected successfully")
                logging.info(f"Folder selected: {folder}")

        except Exception as e:
            logging.error(f"Error selecting folder: {e}")
            self._update_status("Error selecting folder", error=True)

    def _generate_data(self):
        """
        Generate employee data based on user input.
        """
        try:
            # Get and validate employee count
            count_text = self.employee_count_input.text().strip()
            
            if not count_text:
                QMessageBox.warning(self, "Input Error", "Please enter the number of employees to generate.")
                return

            try:
                count = int(count_text)
                if count < 1 or count > 1000:
                    QMessageBox.warning(self, "Input Error", "Please enter a number between 1 and 1000.")
                    return
            except ValueError:
                QMessageBox.warning(self, "Input Error", "Please enter a valid number.")
                return

            # Import and use data generator
            from services.data_gen import EmployeeDataGenerator
            
            # Generate data
            self._update_status("Generating employee data...")
            generator = EmployeeDataGenerator()
            self.employee_data = generator.generate_employees(count)
            
            # Update UI
            self._update_status(f"Successfully generated {count} employees")
            
            # Enable export button if folder is selected
            if self.selected_folder:
                self.export_button.setEnabled(True)

            logging.info(f"Data generation completed for {count} employees")

        except Exception as e:
            logging.error(f"Error in data generation: {e}")
            self._update_status("Error generating data", error=True)
            QMessageBox.critical(self, "Generation Error", f"Failed to generate employee data:\n{str(e)}")

    def _export_to_excel(self):
        """
        Export employee data to Excel file.
        """
        if not self.employee_data:
            QMessageBox.warning(self, "No Data", "Please generate employee data first.")
            return

        if not self.selected_folder:
            QMessageBox.warning(self, "No Folder", "Please select an export folder first.")
            return

        try:
            # Import and use Excel exporter
            from services.excel_export import ExcelExporter
            
            # Update status
            self._update_status("Exporting to Excel...")
            
            # Create exporter and export
            exporter = ExcelExporter()
            file_path = exporter.export_to_excel(self.employee_data, self.selected_folder)
            
            # Update status with success message
            file_name = os.path.basename(file_path)
            self._update_status(f"File '{file_name}' exported successfully!")
            
            # Show success message
            QMessageBox.information(
                self, 
                "Export Complete", 
                f"Employee data has been exported to:\n{file_path}\n\nGenerated {len(self.employee_data)} employee records."
            )
            
            logging.info(f"Excel export completed: {file_path}")

        except Exception as e:
            logging.error(f"Error in Excel export: {e}")
            self._update_status("Export failed", error=True)
            QMessageBox.critical(
                self, 
                "Export Error", 
                f"Failed to export data to Excel:\n{str(e)}"
            )

    def _update_status(self, message, error=False):
        """
        Update the status label with a message.

        Args:
            message (str): Status message to display
            error (bool): Whether this is an error message
        """
        self.status_label.setText(message)

        if error:
            self.status_label.setStyleSheet("""
                QLabel {
                    border: 1px solid #ff6b6b;
                    padding: 10px;
                    background-color: #ffebee;
                    border-radius: 4px;
                    min-height: 20px;
                    color: #c62828;
                }
            """)
        else:
            self.status_label.setStyleSheet("""
                QLabel {
                    border: 1px solid #ddd;
                    padding: 10px;
                    background-color: #f0f8ff;
                    border-radius: 4px;
                    min-height: 20px;
                    color: #000000;
                }
            """)