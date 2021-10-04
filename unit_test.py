# Python program to explain os.getenv() method 
    
  
# Get the value of 'HOME'
# environment variable
# Python program to explain os.getenv() method 
    
# importing os module 
import os
 
 
# Get the value of 'HOME'
# environment variable
key = 'HOME'
value = os.getenv("TEST_KEY")
value_bkp = value
print(f"value_bkp={value_bkp}")
assert value == 'HELLO',"invalid test key"
#import base64
#encoded = base64.b64decode(value)

#print("Debug env", encoded)
      

