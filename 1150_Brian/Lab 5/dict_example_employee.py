"""
Mark Porraz
employee data example
"""

employee_data = {
    'name': 'Ahmed Developer',
    'employee_number': 123456,
    'location':{
        'city': 'Minneapolis',
        'office': 'T.1234',
        'phone': '612-123-4567',
        },
    'roles':['python developer', 'server administrator']}

# How can you read and modify Ahmed's office?
# Changen Ahmed's office to M.4567
employee_data['location']['office'] = 'M.4567'

# Print Ahmed's phone
print(employee_data['location']['phone'])

#Add a new role for Ahmed
employee_data['roles'].append('web developer')

# How's everything look?
print(employee_data)
