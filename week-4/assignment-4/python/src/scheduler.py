import random
from models import Employee
from config import config

DAYS = config["days"]
SHIFTS = config["shifts"]


class Scheduler:
    def __init__(self):
        """
        Initialize scheduler with empty employee and schedule structures.
        Also validates the configuration for required keys.
        """
        self.employees = {}
        self.schedule = {day: {shift: [] for shift in SHIFTS} for day in DAYS}

    def add_employee(self, name, preferences):
        """
        Add an employee with shift preferences.

        Args:
            name (str): Name of the employee.
            preferences (list): List of preferred shifts for the employee.
        """
        self.employees[name] = Employee(name, preferences)

    def get_schedule(self):
        """
        Retrieve the current shift schedule.

        Returns:
            dict: Nested dict of days and their corresponding shifts and assigned employee names.
        """
        return self.schedule

    def get_employees(self):
        """
        Retrieve the list of employees.

        Returns:
            dict: Dictionary of employee names to Employee objects.
        """
        return self.employees

    def reset_schedule_and_employee_counters(self):
        """Reset the shift schedule and all employee assignment counters."""
        self.schedule = {day: {shift: [] for shift in SHIFTS} for day in DAYS}
        for employee in self.employees.values():
            employee.assigned_days = set()

    def get_eligible_employees_for_day(self, day):
        """
        Get a list of employees eligible to work on a given day.

        Args:
            day (str): The day to check availability for.

        Returns:
            list: List of eligible Employee objects.
        """
        return [
            employee
            for employee in self.employees.values()
            if len(employee.assigned_days) < 5 and day not in employee.assigned_days
        ]

    def sorted_employees_by_preference_and_days_assigned(self, day, shift):
        """
        Get eligible employees for a shift on a day, sorted by fewest days assigned and preference rank.

        Args:
            day (str): The day to assign.
            shift (str): The shift name.

        Returns:
            list: Sorted list of tuples (days_assigned, preference_rank, Employee)
        """
        available_employees = [
            (
                len(employee.assigned_days),
                employee.preference_rank.get(shift, 99),
                employee,
            )
            for employee in self.get_eligible_employees_for_day(day)
        ]
        # Sort by days_assigned ascending, then preference_rank ascending
        return sorted(available_employees, key=lambda x: (x[0], x[1]))

    def assign_employee(self, employee, day, shift):
        """
        Assign a specific employee to a shift on a given day.

        Args:
            employee (Employee): The Employee object.
            day (str): The day of assignment.
            shift (str): The shift name.
        """
        self.schedule[day][shift].append(employee.name)
        employee.assigned_days.add(day)

    def assign_shifts(self):
        """Assign employees to shifts while respecting preferences and constraints."""
        self.reset_schedule_and_employee_counters()

        for day_index, day in enumerate(DAYS):
            for shift in SHIFTS:
                available_employees = (
                    self.sorted_employees_by_preference_and_days_assigned(day, shift)
                )

                # Assign top preferred employees
                while len(self.schedule[day][shift]) < 2 and available_employees:
                    chosen_employee = available_employees.pop(0)[2]
                    self.assign_employee(chosen_employee, day, shift)

                # If still unfilled, assign random eligible employees
                if len(self.schedule[day][shift]) < 2:
                    eligible_employees = self.get_eligible_employees_for_day(day)
                    random.shuffle(eligible_employees)
                    for employee in eligible_employees:
                        if len(self.schedule[day][shift]) < 2:
                            self.assign_employee(employee, day, shift)

            # Handle any unassigned employees for this day
            unassigned_employees = self.get_eligible_employees_for_day(day)

            for employee in unassigned_employees:
                shift_assigned = False
                for shift in employee.preferences:
                    if len(self.schedule[day][shift]) < 2:
                        self.assign_employee(employee, day, shift)
                        shift_assigned = True
                        break

                if not shift_assigned:
                    # Try next day's preferred shifts if current day is full
                    for offset in range(1, len(DAYS)):
                        next_day = DAYS[(day_index + offset) % len(DAYS)]
                        for shift in employee.preferences:
                            if (
                                len(self.schedule[next_day][shift]) < 2
                                and next_day not in employee.assigned_days
                            ):
                                self.assign_employee(employee, next_day, shift)
                                shift_assigned = True
                                break
                        if shift_assigned:
                            break
