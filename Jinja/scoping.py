from jinja2 import Template

temp = """{% set numbers = [11,5,4,2,9,8,7] %}
    {% for num in numbers|sort -%}
    {%- endfor %}
    {{num}}
    """

temp2 = """
    {% set var =0 %}
    {% set numbers = [11,5,4,2,9,8,7] %}
    {% for num in numbers|sort -%}
    {% set var = num %}
    {%- endfor %}
    {{num}}
    {{var}}
    """

new_temp  = Template(temp2)
print(new_temp.render())