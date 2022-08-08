'''
Questions:
1. How do I load multiple elements from
   a pickle file?
2. How do I check for entered credentials 
   in the pickle file?
3. Why does a pickle file not work when its 
   empty?
4. How to check for existing credentials
   when making a new account?
'''



def password(p):
    '''
    Makes the password of the user with valid input
    
    Str -> Str
    '''
    
    special_chars = "!@#$%^&*()_-=+{[]}':'<>,?/\|`~" + '""'
    upper_let = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_let = "abcdefghijklmnopqrstuvwxyz"
    numbers = "123456789"
    
    bool_pass_1 = False
    bool_pass_2 = False
    bool_pass_3 = False
    bool_pass_4 = False
    
    storage = {}
    if len(p) > 5 and len(p) < 16:
        for s in range(len(p)):
            if p[s] in special_chars and p.count(p[s]) >= 1:
                bool_pass_1 = True
                
            if p[s] in upper_let and p.count(p[s]) >= 1:
                    bool_pass_2 = True
            if p[s] in lower_let and p.count(p[s]) >= 1:
                    bool_pass_3 = True        
            if p[s] in numbers and p.count(p[s]) >= 1:
                    bool_pass_4 = True                                
    
    if bool_pass_1 and bool_pass_2 and bool_pass_3 and bool_pass_4:
            return p
            
    else:
        print("Invalid format! Try agaian")
        
    
    
        

def login(email_id):
    '''
    With login credentials correct, this function helps in making
    the user id and asks for password belonging to the user id
    
    Str -> Dictof Str
    '''
    
    #print("Hello! This is an automated website! Please enter your email id.")
    login_credentials = {}
    
    
    special_chars = "!@#$%^&*()_-=+{[]}':'<>,?/\|`~" + '""'
    is_bool_before = False
    is_bool_after = False
    is_bool = False
    
    
    for i in range(len(email_id)):
        if email_id[i] not in special_chars:
            is_bool = True
        
        if email_id[i] == "@":
            temp = i
            if len(email_id[:i]) >=3:
                is_bool_before = True
            
        if email_id[i] == "." and email_id.endswith(".com"):
            if len(email_id[temp+1:i]) >= 4:
                is_bool_after = True
                
        
    if is_bool and is_bool_before and is_bool_after:
        passkey = password(input("Please enter a password\n"))
        login_credentials[email_id] = passkey
        return login_credentials, passkey
                    
    else:
        print("Oops! You have entered an incorrect email address. Try again!\n")



import pickle
import pandas as pd


def from_file(file, file_dict):
    '''
    This function appends the credentials of a 
    user in a pickle file.
    
    Str -> Listof Dict
    '''    
    pickle_list = []
    with open(file, "ab") as f:
        file=[pickle.dump(file_dict, f)]
        
    
def get_all(file):
    '''
    Returns the length of the 
    list of elements in a 
    file.
    
    Str -> Listof 
    '''
    pickle_list = []
    with open(file, "rb") as f:
        data = [pickle.load(f)]
    return data

def main():
    '''
    Driver code for the functions
    '''
    
    print("Welcome!")
    
    ques = input("Make a new account or login with an existing account\n")
        
    if ques == "new":
        print("Hello! This is an automated website. Please enter your email id")
        login_creds, password = login(input())
        
        from_file("credential", login_creds)
        print("Great! Your credentials have been stored")
        
    else:
        if ques == "existing":
            pickle_list = get_all("credential")
            forgot = int(input("Forgot your password?\n"))
            if forgot == 1:
                print("Enter your credentials")
                login_creds, passw = login(input())
                if login_creds in pickle_list:
                    print("Your account uses the exact password")
                else:
                    print("Here is your password", passw)
                
            else:
                if forgot == 0:
                    print("Enter your email id and password")
                    login_creds, password = login(input())
                    if login_creds in pickle_list:
                        print("You have logged in")
                    else:
                        print("Invalid credentials. Try again!")
        else:
            print("Invalid input. Try Again")
    main()
                
                
        
        
        
                   
               
          
        
            
    
    