import sys
from jinja2 import Environment, PackageLoader, select_autoescape
from bs4 import BeautifulSoup as bs

demo_template_path = 'demo.html'

env = Environment(
    loader=PackageLoader('python_bootstrap', 'templates'),
    # autoescape=select_autoescape(['html', 'xml'])
)

names = ['Gabe', 'Andrew']

demo_template = env.get_template(demo_template_path)
demo_output = demo_template.render(names=names, best='Dexter')
soup = bs(demo_output, 'html.parser')
pretty_demo_output = soup.prettify()
print(pretty_demo_output)
