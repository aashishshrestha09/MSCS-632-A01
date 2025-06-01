class Employee:
    """
    Represents an employee with their name, shift preferences, and scheduling state.

    Attributes:
        name (str): The name of the employee.
        preferences (list): A list of shift preferences in ranked order (e.g. ['morning', 'afternoon', 'evening']).
        preference_rank (dict): A mapping of shift to its preference rank (0-based index).
        assigned_days (set): A set of day names or identifiers when the employee is assigned to work.
    """

    def __init__(self, name, preferences):
        self.name = name
        self.preferences = preferences
        self.preference_rank = {shift: rank for rank, shift in enumerate(preferences)}
        self.assigned_days = set()
