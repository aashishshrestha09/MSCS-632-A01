import os
from jinja2 import Environment, FileSystemLoader


def generate_schedule_from_template(template_file, params):
    """
    Generate a schedule HTML (or text) output by rendering a Jinja2 template.

    Args:
        template_file (str): The filename of the Jinja2 template to use (must exist in the 'templates' directory).
        params (dict): A dictionary of parameters to pass into the template for rendering.

    Returns:
        str: The rendered content as a string (usually HTML).

    Example:
        html = generate_schedule_from_template("schedule_template.html", {"employees": [...], "days": [...]})
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    env = Environment(loader=FileSystemLoader(os.path.join(script_dir, "templates")))
    template = env.get_template(template_file)
    rendered_content = template.render(**params)
    return rendered_content
