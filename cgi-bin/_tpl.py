"""
"""

from jinja2 import Environment, FileSystemLoader

env = None

# -----------------------------------------------------------------------------
def set_tpl_dir(tpl_dir):
    """
    """
    global env

    env = Environment(loader=FileSystemLoader(tpl_dir))


# -----------------------------------------------------------------------------
def render(tpl_file, vars_dict):
    """
    """

    tpl = env.get_template(tpl_file)
    rendered = tpl.render(vars_dict)

    return rendered
