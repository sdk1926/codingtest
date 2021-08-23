import re
password = 'wow12!'

print(re.match('^(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d@$!%*#?&]{8,}$', password))
print(re.match('^(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%^&*])[a-zA-Z\d!@#$%^&*]{8,}$', password))

                