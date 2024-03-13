
contacts = {
    'number': 3,
    'students':
        [
            {'name':'Jameson Bos', 'email':'jameson@example.com'},
            {'name':'Emily Lahrs', 'email':'emily@example.com'},
            {'name':'Wayne Gretzky', 'email':'wayne@example.com'}
        ]
}

print('Student emails:')
for student in contacts['students']:
    print(student['email'])
