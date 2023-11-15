#!/usr/bin/env python
# coding: utf-8

# In[15]:


import string

def length(password):
    """
    Function to check if the lenght of password is at least 9 but not more than 17.
    
    returns
    
    bool
    
    parameter: string
    
    """

    len_password=len(password)
    if 9<=len_password<=17: #length of password should be at least 9 but not more than 17
        return True
    else:
        print('Password must be between 9 and 17 characters')
        return False
              
              
def alpha(password):
    """
    Function to check if password has at least 5 alphabets, 3 of which are at least uppercase and 2 are at least lowercase.
    
    returns
    
    bool
    
    parameter: string
    """
    uppercase = 0
    lowercase = 0

    for char in password:
        if char.isalpha() and char == char.upper(): # checking if password has alphabet and uppercase increment
            uppercase += 1

        if char.isalpha() and char == char.lower():  # checking if password has alphabet and lowercase increment
            lowercase+=1

    total_alpha = uppercase + lowercase


    if all([total_alpha >= 5,  uppercase >= 3, lowercase >=2]): #checking if passowrd has at least each at the right amount.
        return True 
    else:
        print('Password must contain at least 3 uppercase and 2 lowercase')
        return False

def number(password):
    """
    Function to check if password has at least 2 different numbers.
    
    returns
    
    bool
    
    parameter: string
    """
    
    count=0
    num=[]
    
    #checking if password has 2 different numbers
    for char in password:
        if char.isnumeric(): 
            nums=char
            if nums != num:
                count+=1
                num = nums    
    if count>=2:
        return True
    else:
        print('Password must contain at least 2 different numbers')
        return False
    


def punctuation(password):
    """
    Function to check if password has at least 2 different punctations.
    
    returns
    
    bool
    
    parameter: string
    """
    
    count=0
    num=[]
    punctuations=string.punctuation #(!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~)
    
    #checking if password has 2 different punctuations
    for char in password:
        if char in punctuations: 
            new_punc=char
            if new_punc != num:
                count+=1
                num = new_punc
                
    if count>=2:
        return True
    else:
        print('Password must contain at least 2 different punctuations')
        return False
    
    
def first_character(password):
    """
    Function to check if password begins with punctuation as the first character.
    
    returns
    
    bool
    
    parameter: string
    
    """
    
    punctuations = string.punctuation  #(!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~)
    if password[0] in punctuations: #check if first character of password is punctuation
        print('Password cannot begin with punctuations')
        return False
    else:
        return True

    
def space(password):
    """
    Function to check if password has space.
    
    returns
    
    bool
    
    parameter: string
    
    """
    
    if " " in password: #check if password has space
        print('Passwords must not have space')
        return False 
    else:
        return True
    
    
    
def isGoodPwd():
    
    """Function to check if password has at least 2 different punctations.
    
    returns
    
    bool
    
    parameter: string"""
    
    password=input('input password to check its validity \n password must be between 9 and 17 characters \n contain at least 3 uppercase and 2 lowercase \n contain at least 2 different numbers \n contain at least 2 different punctuations \n must not contain space \n Entered password is: ' )


    if all([length(password), space(password), first_character(password), alpha(password), number(password),punctuation(password)]):
        return True
    return False
    


isGoodPwd()


# In[ ]:





# In[ ]:




