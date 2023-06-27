import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['~','`','!', '@','#', '$', '%', '&', '(', ')', '*', '+',':',';','/','|','<','>','[',']','-']


def genPassword():
    letterPrompt = int(input("How many letters do you want in your password?\n"))
    numberPrompt = int(input(f"How many numbers?\n"))
    symbolPrompt= int(input(f"How many symbols? \n"))

    password_list = []

    for char in range(1, letterPrompt + 1):
        password_list.append(random.choice(letters))

    for char in range(1, numberPrompt + 1):
        password_list += random.choice(numbers)

    for char in range(1, symbolPrompt + 1):
        password_list += random.choice(symbols)
      
    random.shuffle(password_list)
   
    password = ""
    for char in password_list:
        password += char

    print(f"Your password is: {password}")  
       
# Menu
print('''

-----------------------PYTHON PASSWORD GENERATOR------------------------------
	
	Make a Choice to Begin! 
	
	1. Generate a Password
	2. Quit
 ------------------------------------------------------------------------------
	
	''')
userchoice = int(input("\n=>"))
	
if userchoice == 1:         
    genPassword()

    print(''' 
    
    Do you want to generate another password?

    1. Yes, Please!
    2. No, I'm Good :)

    ''')
    userchoice = int(input("\n=>"))

    if userchoice == 1:
        genPassword()
                
    else:
        programmRunning = False
        print("See you next time!")     

elif userchoice == 2:
		programmRunning = False
		print("Bye!")
else:
		print("invalid entry!!")
	
