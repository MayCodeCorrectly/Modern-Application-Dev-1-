from jinja2 import Template
# import class template from jinja2

blue_print = """Hello {{name}} !"""   # this is just blue print of our template

template = Template(blue_print) # converting blue_print to template

print(template.render(name="Sandeep")) # render --> used for substitution
