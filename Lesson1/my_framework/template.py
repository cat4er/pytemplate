import os
from jinja2 import Template


def render(template_name, folder='pages', **kwargs):
    page_path = os.path.join(folder, template_name)
    with open(page_path, encoding='utf-8') as pp:
        template = Template(pp.read())

    return template.render(**kwargs)
