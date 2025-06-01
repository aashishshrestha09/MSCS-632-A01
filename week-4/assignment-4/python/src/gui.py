from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QMessageBox,
    QComboBox,
    QGridLayout,
    QFormLayout,
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from scheduler import Scheduler
from config import config
from helpers import generate_schedule_from_template

DAYS = config["days"]
SHIFTS = config["shifts"]


class SchedulerApp(QWidget):
    """
    Employee Shift Scheduler GUI application.

    This class provides a PyQt6-based interface for adding employees with their
    ranked shift preferences and generating a schedule based on those preferences.
    """

    def __init__(self):
        """
        Initialize the SchedulerApp UI, load config values, and set up widgets and layouts.
        """
        super().__init__()
        self.setWindowTitle("Employee Shift Scheduler")
        self.setGeometry(100, 100, 1400, 800)
        self.shift_options = SHIFTS
        self.scheduler = Scheduler()

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(20)

        main_layout.addLayout(self.create_name_input_section())
        main_layout.addWidget(self.create_prefs_label())
        main_layout.addLayout(self.create_prefs_grid())

        # Create buttons and connect signals
        self.add_button = self.create_add_button()
        self.add_button.clicked.connect(self.add_employee)
        main_layout.addWidget(self.add_button)

        self.generate_button = self.create_generate_button()
        self.generate_button.clicked.connect(self.generate_schedule)
        main_layout.addWidget(self.generate_button)

        self.schedule_output = self.create_schedule_output()
        main_layout.addWidget(self.schedule_output)

        self.setLayout(main_layout)

    def create_name_input_section(self):
        """
        Create the employee name input field with a label.

        Returns:
            QFormLayout: A layout containing the name input widget.
        """
        form_layout = QFormLayout()
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)
        form_layout.setFormAlignment(Qt.AlignmentFlag.AlignLeft)
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter employee name")
        self.name_input.setMinimumWidth(300)
        self.name_input.setStyleSheet("padding: 6px; font-size: 14px;")
        form_layout.addRow(QLabel("<b>Employee Name:</b>"), self.name_input)
        return form_layout

    def create_prefs_label(self):
        """
        Create the label for shift preference selection section.

        Returns:
            QLabel: A styled label widget.
        """
        label = QLabel("Select shift preferences (ranked):")
        label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        return label

    def create_prefs_grid(self):
        """
        Create a grid layout containing 3 combo boxes for shift preferences.

        Returns:
            QGridLayout: The layout with labeled combo boxes for preferences.
        """
        pref_grid = QGridLayout()
        pref_grid.setHorizontalSpacing(30)
        pref_grid.setVerticalSpacing(10)

        pref_grid.addWidget(
            QLabel("<b>1st Preference</b>"),
            0,
            0,
            alignment=Qt.AlignmentFlag.AlignCenter,
        )
        pref_grid.addWidget(
            QLabel("<b>2nd Preference</b>"),
            0,
            1,
            alignment=Qt.AlignmentFlag.AlignCenter,
        )
        pref_grid.addWidget(
            QLabel("<b>3rd Preference</b>"),
            0,
            2,
            alignment=Qt.AlignmentFlag.AlignCenter,
        )

        combo_style = """
            QComboBox {
                padding: 6px 10px;
                font-size: 14px;
                border: 1px solid #aaa;
                border-radius: 5px;
                min-width: 100px;
            }
            QComboBox:hover {
                border-color: #0078d7;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 25px;
                border-left-width: 1px;
                border-left-color: #aaa;
                border-left-style: solid;
                border-top-right-radius: 5px;
                border-bottom-right-radius: 5px;
            }
            QComboBox:focus {
                border-color: #005a9e;
                outline: none;
            }
        """

        self.pref1_combo = QComboBox()
        self.pref1_combo.addItems(self.shift_options)
        self.pref1_combo.setStyleSheet(combo_style)
        pref_grid.addWidget(self.pref1_combo, 1, 0)

        self.pref2_combo = QComboBox()
        self.pref2_combo.addItems(self.shift_options)
        self.pref2_combo.setStyleSheet(combo_style)
        pref_grid.addWidget(self.pref2_combo, 1, 1)

        self.pref3_combo = QComboBox()
        self.pref3_combo.addItems(self.shift_options)
        self.pref3_combo.setStyleSheet(combo_style)
        pref_grid.addWidget(self.pref3_combo, 1, 2)

        return pref_grid

    def create_add_button(self):
        """
        Create the 'Add Employee' button with styles applied.

        Returns:
            QPushButton: The styled button.
        """
        btn = QPushButton("Add Employee")
        btn.setStyleSheet(
            """
            QPushButton {
                background-color: #4CAF50; color: white; font-size: 16px; padding: 8px 16px; border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """
        )
        return btn

    def create_generate_button(self):
        """
        Create the 'Generate Schedule' button with styles applied.

        Returns:
            QPushButton: The styled button.
        """
        btn = QPushButton("Generate Schedule")
        btn.setStyleSheet(
            """
            QPushButton {
                background-color: #2196F3; color: white; font-size: 16px; padding: 8px 16px; border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """
        )
        return btn

    def create_schedule_output(self):
        """
        Create a read-only text area to display the generated schedule.

        Returns:
            QTextEdit: The text area widget.
        """
        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setStyleSheet(
            """
            QTextEdit {
                background-color: #f5f5f5; 
                color: #000000;
                font-size: 14px;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
        """
        )
        return text_edit

    def add_employee(self):
        """
        Add a new employee with their ranked shift preferences.

        Validates inputs:
        - Name must not be empty.
        - Shift preferences must be unique.
        - Adds the employee and resets input fields.
        """
        name = self.name_input.text().strip()
        pref1 = self.pref1_combo.currentText()
        pref2 = self.pref2_combo.currentText()
        pref3 = self.pref3_combo.currentText()

        # Validate inputs
        if not name:
            QMessageBox.warning(self, "Input Error", "Please enter the employee name.")
            return

        # Check for duplicate preferences
        prefs = [pref1, pref2, pref3]
        if len(set(prefs)) < 3:
            QMessageBox.warning(
                self, "Input Error", "Please select unique shift preferences."
            )
            return

        # Add employee info to list (or any data structure)
        self.scheduler.add_employee(name, prefs)

        # Confirmation (optional)
        QMessageBox.information(self, "Success", f"Added employee: {name}")

        # Clear input for next
        self.name_input.clear()
        self.pref1_combo.setCurrentIndex(0)
        self.pref2_combo.setCurrentIndex(0)
        self.pref3_combo.setCurrentIndex(0)

    def generate_schedule(self):
        """
        Generate and display a shift schedule based on added employees' preferences.

        - Requires at least 2 employees.
        - Uses Scheduler to assign shifts.
        - Renders an HTML schedule template.
        """
        employees = self.scheduler.get_employees()
        if len(employees) < 2:
            QMessageBox.warning(
                self,
                "Insufficient Employees",
                "Please add at least 2 employees before generating the schedule.",
            )
            return

        self.scheduler.assign_shifts()
        params = {
            "days": DAYS,
            "shifts": SHIFTS,
            "schedule": self.scheduler.get_schedule(),
            "employees": employees,
        }
        html_content = generate_schedule_from_template("schedule_template.html", params)
        self.schedule_output.setHtml(html_content)
