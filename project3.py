
import hashlib    
my_input="Hi! I'm Snigdha"
salt="3g8"
my_string=my_input+salt
for i in range(10):
    my_result=hashlib.md5(my_string.encode())
print("My Output is : ",my_result)