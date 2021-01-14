#Devin Hale
#Project 1
#Dictionary/Brute force attack

import random



pw = input("Please enter a password for the computer to guess:")
pwminlength = int(input("Please enter minimum length for password: (cannot be 0) "))
pwlength = [1,2,3,4,5,6,7,8,9]



pwlist = list(pw)

pwk = []
dictpwk = []

index = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !@'
numindex = '1234567890!@'
indexl = list(index)
numindexl = list(numindex)

attempt = 0

choice = "y"

with open("password.txt", 'r') as dictionary:

    while attempt < 7092:
 
        for line in dictionary:
            dictpass = dictionary.readline()
            dictpwk = list(dictpass.strip())
            dictlength = len(dictpwk) 
            addonamount = pwminlength - dictlength # if dictioned word is below minimum password length, adds this many characters
            attempt += 1

            while addonamount > 0:
                dictaddon = random.choice(numindexl) 
                dictpwk.append(dictaddon)
                addonamount -= 1

            if dictpwk != pwlist:
                dictpwk = ''.join(dictpwk)
                dictpwk = dictpwk.capitalize()
                dictpwk = list(dictpwk)
                attempt += 1

                if dictpwk != pwlist:
                    dictpwk =''.join(dictpwk)
                    dictpwk = dictpwk.lower()
                    dictpwk = list(dictpwk) 
                    attempt += 1

                    if dictpwk != pwlist:
                        dictpwk = ''.join(dictpwk)
                        dictpwk = dictpwk.upper()
                        dictpwk = list(dictpwk)
                        attempt += 1
                        

            if dictpwk == pwlist:
                print("Your password: '" + pw +  "' was dictionated in " + str(attempt) + " attempts")
                break



print("Dictionary Attack Failed - Attempting Brute Force...")

if choice == "y":

    while pwk != pwlist and dictpwk != pwlist:
        length = random.randrange(pwlength[pwminlength - 1], 10) #will only generate a password between minimum password length and 10
        while length > 0: 
            tgpw = random.choice(indexl)  
            pwk.append(tgpw)
            length -= 1 
            
        if pwlist != pwk:
            attempt += 1
            pwk = []

        if attempt == 65000:
            choice = input("You have attempted to generate this password 65000 times.. Continue forever? (y/n)")
            if choice != 'y':
                print("Password generation failure...")
                break



if dictpwk != pwlist and pwk == pwlist:     
    print("Your password: '"+ pw + "' was generated in " + str(attempt) + " attempts")


# Grade: 118/125
# A lot of good stuff in here. A few logic errors and a couple of
# head-scratchers. But overall a very nice project. Well done!
