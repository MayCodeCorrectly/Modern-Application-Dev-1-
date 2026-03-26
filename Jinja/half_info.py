from jinja2 import Template

temp = "My name is {{name}} and i am currently working on my {{course_name}} course"
make_template = Template(temp)
print(make_template.render(name = "Alice")) # unsubstituted variables display with blank space

from string import Template

temp = "My name is $name and i am currently working on my $course_name course"
make_template = Template(temp)
# print(make_template.substitute(name = "Bob")) # This throws error since course_name is not given
print(make_template.safe_substitute(name = "Bob"))