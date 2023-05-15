# Creating a nested dictionary
student = {
    'name': 'John Doe',
    'age': 20,
    'grades': {
        'math': 90,
        'science': 85,
        'history': 92
    },
    'address': {
        'street': '123 Main St',
        'city': 'New York',
        'state': 'NY'
    }
}

# Accessing nested dictionary values
print("Student Name:", student['name'])
print("Math Grade:", student['grades']['math'])
print("City:", student['address']['city'])
