from string import Template

blue_print = """The course name is $course_name and it is $difficulty"""
template = Template(blue_print)
print(template.safe_substitute(course_name = "DBMS", difficulty = "Easy"))

