import re 
    # Input
password = input ("Enter the password: ")
    # Criteria For Min 8 charcter Password
while(len(password)<8):
    password=input("Enter min 8 character password: ")
    if (len(password)>=8):
        password=password
        break

    #checking for upper case
for_lower=re.search(r'[a-z]',password)
    #checking for lower case
for_upper=re.search(r'[A-Z]',password)
    #checking for number
for_num=re.search(r'\d',password)
    #checking for special character
for_specialchar=re.search(r'[\W]',password)

    # Finally divide them as required
if for_upper and for_lower and for_num and for_specialchar:
    print("Strong Password")
elif for_num and for_upper and for_lower :
    print("Modrate Password")
elif for_upper and for_lower:
   print("weak Password")
else:
    print("weak Password")
