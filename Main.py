# -*- coding: utf-8 -*-
"""
Created on Mon May  3 23:01:25 2021

@author: sneha
"""

import UserLogin

print("Welcome!")

print("Choose one of the following")
print("1. Login")
print("2. Sign up")
i = 0
i = int(input ("input:"))

if i==1:
    UserLogin.login()
elif i==2:
    UserLogin.sign_up()
else:
    print("invalid Input")
        