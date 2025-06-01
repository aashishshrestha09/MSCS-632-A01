import os
import json


def load_env_var(name, default_value=None):
    """
    Load an environment variable and parse it as a JSON list of strings.

    Args:
        name (str): The name of the environment variable to load.
        default_value (any, optional): A value to use if the environment variable is not set.

    Returns:
        any: The parsed value from the environment variable, or the default value.

    Raises:
        ValueError: If the environment variable exists but contains invalid JSON.
        EnvironmentError: If the environment variable is not set and no default is provided.
    """
    value = os.getenv(name)
    if value:
        value = value.strip()
        try:
            parsed = json.loads(value)
            if isinstance(parsed, list) and all(
                isinstance(item, str) for item in parsed
            ):
                return parsed
        except json.JSONDecodeError as e:
            raise ValueError(
                f'Environment variable "{name}" contains invalid JSON: {e}'
            )
    if default_value is not None:
        return default_value
    raise EnvironmentError(f'Environment variable "{name}" must be set!')


config = {
    "days": load_env_var(
        "DAYS",
        ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    ),
    "shifts": load_env_var(
        "SHIFTS",
        ["morning", "afternoon", "evening"],
    ),
}
