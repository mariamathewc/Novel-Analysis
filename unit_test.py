# Python program to explain os.getenv() method 
    
  
# Get the value of 'HOME'
# environment variable
# Python program to explain os.getenv() method 
    
# importing os module 
import os
 
 
# Get the value of 'HOME'
# environment variable
key = 'HOME'
value = os.getenv("test_key")
import base64
encoded = base64.b64decode(value)

print("Debug env", encoded)
      

