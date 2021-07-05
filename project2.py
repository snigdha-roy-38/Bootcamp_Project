
import hashlib    
my_input="Hi! I'm Snigdha"
my_result1=hashlib.md5(my_input.encode())
print("My Output is : ",my_result1)
my_result2=hashlib.sha1(my_input.encode())
print("My Output is : ",my_result2)
my_result3=hashlib.shake_256(my_input.encode())
print("My Output is : ",my_result3)