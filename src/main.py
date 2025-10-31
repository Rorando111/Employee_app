"""
Employee Data Generator - Main Application Entry Point

This is the main entry point for the Employee Data Generator desktop application.
It initializes the PySide6 application, sets up logging, and launches the main window.

The application provides functionality to:
- Generate synthetic employee data
- Export data to Excel with summary statistics
- User-friendly GUI for data management

"""

import sys
import logging
import os
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from utils.constants import LOG_FORMAT, LOG_LEVEL


def setup_logging():
    """
    Configure application logging based on constants.

    Sets up logging to console with the specified format and level.
    """
    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL),
        format=LOG_FORMAT
    )


def main():
    """
    Main application entry point.

    Initializes logging, creates the QApplication instance,
    sets up the main window, and starts the event loop.
    """
    setup_logging()
    logging.info("Starting Employee Data Generator application")

    try:
        # Create QApplication instance
        app = QApplication(sys.argv)
        app.setApplicationName("Employee Data Generator")
        app.setApplicationVersion("1.0.0")
        app.setOrganizationName("Company A")
        logging.info("QApplication created successfully")

        # Create and show main window
        window = MainWindow()
        logging.info("MainWindow created successfully")
        window.show()
        logging.info("Application window displayed")

        # Start event loop
        sys.exit(app.exec())

    except Exception as e:
        logging.error(f"Critical error in main application: {e}")
        raise


if __name__ == '__main__':
    main()