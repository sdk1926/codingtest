import re
email = 'dsafsnaver.com'

# print(not re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email))

r = re.compile('[\w]+[@][\w]+[.][\w]+')

if r.match('wegjkn@gmail.com'):
    print('True')
else:
    print(False)