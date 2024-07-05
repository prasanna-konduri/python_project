import re

def check_password_strength(password):
   """
   Checks for the password Strength based on the criteria
   1. Password should be minimum of 8 char
   2. Atleast one uppercase, one lowercase, one number and one special char should be present

   Parameters:
    password(string): password string to check 
    
   """
   
   #checks if the password is minimum 8 char
   if len(password)<8:
      return False
   #checks if the password contains atleast one uppercase letter
   elif not re.search(r'[A-Z]', password):
        return False
   #checks if the password contains atleast one lowercase letter
   elif not re.search(r'[a-z]',password):
       return False
   #checks if the password contains atleast one number
   elif not re.search(r'[0-9]',password):
       return False
   #checks if the password contains atleast one special charector
   elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
       return False
   else:
       return True


def main():
    password = input("Please Enter your password: ")
    if check_password_strength(password):
        print("The password is strong.")
    else:
        print("The password is weak. It should be at least 8 characters long, contain both uppercase and lowercase letters, include at least one digit, and have at least one special character.")



if __name__ == "__main__":
    main()