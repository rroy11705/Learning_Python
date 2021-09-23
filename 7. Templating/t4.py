from jinja2 import Environment, FileSystemLoader


persons = [
    {'name': 'andre', 'age': 21},
    {'name': 'raj', 'age': 24},
    {'name': 'rohit', 'age': 27},
    {'name': 'Lucky', 'age': 21},
]

file_loader = FileSystemLoader('templates')

env = Environment(loader=file_loader)
template = env.get_template("show-person.txt")

output = template.render(persons=persons)
print(output)
