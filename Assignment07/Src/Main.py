#Name: Nathan Lowe
#email: lowenc@mail.uc.edu
#Assignment Title: Assignment 07
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: Creating a captcha in python
#Citations: 
#Anything else that's relevant:

from Src.Assignment07 import generate_captcha

result = generate_captcha(6, "test.png")
myCaptcha = result[0]
captcha_string = result[1]
print(">" + captcha_string + "<")
myCaptcha.show()

