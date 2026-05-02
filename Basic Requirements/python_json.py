import json
My_dictionary = {	
"name": "John",
"age": 28,
"city": "Chennai"
}
out = json.dumps(My_dictionary)

print(out,type(out))