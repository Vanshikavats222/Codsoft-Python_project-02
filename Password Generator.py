import string
import random

s1 = string.ascii_lowercase
#print(s1)
s2= string.ascii_uppercase
#print(s2)
s3= string.digits
#print(s2)
s4= string.punctuation
#print(s4)

password = int(input("Enter the password Length /n"))
s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
random.shuffle(s)
#print(s)
print("Enter the Password you want":)
print("".join(s[0:password]))

