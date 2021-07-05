
import hashlib    
my_input="Hi! I'm Snigdha"
my_result=hashlib.md5(my_input.encode())
print("My Output is : ",my_result)