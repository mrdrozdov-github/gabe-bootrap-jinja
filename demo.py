import sys
from jinja2 import Environment, PackageLoader, select_autoescape
from bs4 import BeautifulSoup as bs

env = Environment(
    loader=PackageLoader('python_bootstrap', 'templates'),
    # autoescape=select_autoescape(['html', 'xml'])
)

RUN_1 = False


# Demo 1: Print a list.
if RUN_1:
    names = ['Gabe', 'Andrew']
    demo_template_path = 'demo.html'
    demo_template = env.get_template(demo_template_path)
    demo_output = demo_template.render(names=names, best='Dexter')
    soup = bs(demo_output, 'html.parser')
    pretty_demo_output = soup.prettify()
    print(pretty_demo_output)


# Demo 2: Multiple pages that extend the same template.
post_template_path = 'post.html'
about_template_path = 'about.html'

post_template = env.get_template(post_template_path)
about_template = env.get_template(about_template_path)

about_output = about_template.render(subtitle='about')

class Object(object): pass

items = []
for i in range(10):
    d = Object()
    d.date = i
    d.title = 'Title={}'.format(i ** 2)
    items.append(d)

post_output = post_template.render(subtitle='post', items=items)

with open('html/about.html', 'w') as f:
    f.write(about_output)

with open('html/post.html', 'w') as f:
    f.write(post_output)
