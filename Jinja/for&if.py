from jinja2 import Template

items = ["Apple","Banana","Cherry","Dragon fruit"]
temp = "{% for item in items -%} " \
        "{{item}}, " \
        "{%- endfor %}"

temp2 = """{% for item in data -%}
        {{item}}, 
        {% endfor %}"""

# temp = "{% for item in items -%} {{item}}, {% endfor %}" # Does same thing as upper blue_print

template = Template(temp)
final = template.render(items=items)
print(final)

template = Template(temp2)
final = template.render(data=items)
print(final)

numbers = [i for i in range(10)]
odd_list = "{% for num in numbers if num%2==1 %}{{num}} {% endfor %}"
desired_list = Template(odd_list)

output = desired_list.render(numbers = numbers)
print(output)

"""
{% if %}
    block- 1
{% elif %}
    block- N
{% else %}
    Catch all
{% endif %}

"""

even_list = """
    {%- for num in number -%}
    {% if num%2==0 -%} 
    {{num}}, {% elif num==3 %}{{num}}, {% endif %} 
    {%- endfor %}"""

desired_list= Template(even_list)
output = desired_list.render(number= numbers)
print(output)
