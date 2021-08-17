import re
email = 'ds+.a-f_s@naver.com'

goodmail = re.match('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$', email)

print(goodmail)
password = "123sde1#234"
goodpassword=re.match("^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,2048}$", password)
print(goodpassword)