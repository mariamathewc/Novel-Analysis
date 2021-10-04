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
print("Debug env", value)
      
for k, v in sorted(os.environ.items()):
    print(k+':', v)
print('\n')

