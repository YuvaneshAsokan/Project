#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re

Register = input("Create your Google Account: Enter Your UserName: ")
Credential1 = input("Credential: Enter Your Favourite City: ")

if re.match('[A-Za-z0-9]+@[A-Za-z]+\.[A-Za-z]+$', Register):
    print("valid mail")
    
else:
    print("Invalid")
      
while True:

    user_input = input("Enter your password : ")
    is_valid = False 

    if (len(user_input)<5 or len(user_input)>16):

        print("Not valid ! Total characters should be between 6 and 12")
        continue
    elif not re.search("[A-Z]",user_input):
        print("Not valid ! It should contain one letter between [A-Z]")
        continue
    elif not re.search("[a-z]",user_input):

        print("Not valid ! It should contain one letter between [a-z]")
        continue
    elif not re.search("[1-9]",user_input):

        print("Not valid ! It should contain one letter between [1-9]")
        continue
    elif not re.search("[~!@#$%^&*]",user_input):
        print("Not valid ! It should contain at least one letter in [~!@#$%^&*]")
        continue
    elif re.search("[\s]",user_input):

        print("Not valid ! It should not contain any space")
        continue
    else:
        is_valid = True
        break

if(is_valid):
    print("Password is valid")
    
while True:
    login_input = input("Sign in to your Google Account: ")
    
    if login_input == Register:
        print("Welcome to Gmail")
        break
    else:
        print("Register your gmail")
        break
while True:
        Password = input("Enter your password: ")
        if Password == user_input:
            print("Successfully Login")
            break
        else:
            Action = input("Are your Forget the Password(Type Yes - if you forgot): ")
            if Action == "Yes":
                Credential = input('Enter Your Favourite City and Set New Password')
                if Credential == Credential1:
                    print("Set New Password")
        break
            
            


# In[ ]:




