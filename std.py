'''
Name : 
Class : XII

Computer Science Project

'''
# importing important modules
import os
import time
import webbrowser
import datetime
import os.path

# list storing the animations
a = ['[̲̅_̲̅_̲̅_̲̅_̲̅_̲̅] 1O%','[̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅] 2O%','[̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅] 3O%','[̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅] 4O%','[̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅] 5O%','[̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅] 6O%','[̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅] 7O%','[̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅] 8O%','[̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅] 9O%',
'[̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅_̲̅] 100%']

# wishes the user
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        print("Good Morning !!")
    elif hour >= 12 and hour < 18:
        print("Good Afternoon")
    else:
        print("Good Evening") 

    print("Welcome to the student database !! Please follow further instructions")
# animation loads
def loading():
    for i in range(0,10):
        os.system("clear||cls")
        print("Loading : ")
        print(a[i])
        time.sleep(0.2)
        os.system("clear||cls")
# logging the data for security purposes
def logs():
    global charmander
    current_time = datetime.datetime.now()
    charmander = str(current_time)
    logs = open("logs/logs.txt","a")
    logs.write("Accessed on :")
    logs.write('\n')
    logs.write(charmander)
    logs.write('\n')
    logs.close()
# function to convert
def squirtle():  # the login function
    os.system("clear||cls")
    time.sleep(1)
    print(" Logging in ")
    time.sleep(0.1)
    print(" Please enter your username and password when asked ")
    global gengar
    gengar = 'db_data/'
    gengar += input(" Input username ( without spaces ) ")
    gengar += '.txt'
    light = os.path.isfile(gengar) # Checks for existence of user
    
    # checks for users password
    def eren():
        print("\n")
        yeager = input("Please enter your password : ")
        grisha = open(gengar)
        carla = grisha.read()
        if yeager == carla:
            print("succesful login ~~ ")
            attack()
        else:
            print("wrong password entered")
    
    # conditons check    
    if light == True:
        print("User found !!")
        eren()

    elif light == False:
        print("Sorry you aren't registered")
        print("Redirecting to registeration....")
        bulbasaur()

    else:
        print("Invalid Input ..... Exiting")

    # condtions check over
    
def bulbasaur():  # the register functions
    os.system("clear||cls")
    print("Registration Page")
    charizard = 'db_data/'
    charizard += input(" Please enter your name (without spaces): ")
    charizard += '.txt'
    mewto = input("Please enter the password which you would like to keep : ")
    mew = open(charizard,"a")
    mew.write(mewto)
    mew.close()
    print("Successfully registered")

def attack():
    print("~        Welcome to Student Report Database            ~")
    time.sleep(2)
    os.system("clear||cls")
    if gengar == "db_data/admin.txt":
        print(" Welcome Administrator  ")
        print(" Please note the following ")
        print('''
        1. If you are not the admin please don't use it and report to a admin about the password leak
        2. Please don't misuse the database
        3. With great power comes great responsibility
        ''')
        print("\n")
        print("Accessing Admin Panel")
        time.sleep(2)
        os.system("clear||cls")
        print( " Admin Dashboard ")
        print("Please select a valid option ")
        print("Admin Session                 Last Acessed : ", charmander)

        print('''
        Press 1 for acessing (read only) student's profile \n
        Press 2 for viewing marks (read only) of student's \n
        Press 3 to change/enter student's marks \n
        Press 4 to make a report card \n
        Press 5 to send student's a message \n
        Press 6 to exit \n   
        ''')

        mikasa = int(input("    :    "))
        # if and elif mega loops
        if mikasa == 1:
            Itoshiteru()
        elif mikasa == 2:
            Konpyuta()
        elif mikasa == 3:
            Furukiyokijidai()
        elif mikasa == 4:
            pass
        elif mikasa == 5:
            pass
        elif mikasa == 6:
            wishMe()
        else:
            print("Invalid Input")
        
    else:
        print("Welcome ", gengar)
        print(" Please note the following ")
        print('''
        1. If you are not the owner of this account please don't use it and report to a admin about the password leak
        2. Please don't misuse the database
        3. With great power comes great responsibility
        ''')
        print("\n")
        print("Accessing Your Dashboard .....")
        time.sleep(2)
        os.system("clear||cls")
        print('''
        Type 1 to make your profile \n
        Type 2 to view your profile
        ''')

        giyu = int(input("    :     "))
        # if else mega function
        if giyu == 1:
            Konnichiwa()
        if giyu == 2:
            Omoshiroi()

def Konnichiwa():  # profile maker
    print("Please input carefully it cannot be re-edited due to security issues \n \n")
    print("Enter everything in lowercase only")
    print("\n")
    print("\n")
    tanjiro = input("Your Full Name : \n")
    zenitsu = input("Your Roll No. : \n")
    innosuke = input("Your Grade/Class : \n")
    nezuko = input("Your contact number : \n")
    muzan = input("Birthdate in letters only ( e.g. 17 may ): \n")
    rengoku = input("Your Stream (None if not class 11-12) : \n")
    #define path
    global kanao
    kanao = innosuke
    kanao += '/'
    kanao += tanjiro
    kanao += '.txt'

    shinobu = open(kanao,"a")
    shinobu.write(tanjiro)
    shinobu.write('\n')
    shinobu.write(zenitsu)
    shinobu.write('\n')
    shinobu.write(innosuke)
    shinobu.write('\n')
    shinobu.write('\n')
    shinobu.write(nezuko)
    shinobu.write('\n')
    shinobu.write(rengoku)
    shinobu.write('\n')
    shinobu.write('------------------------------------------   END OF FILE  ---------------------------------------')
    shinobu.close()

    print(" Thank You ..  Going Back")
    attack()

def Omoshiroi(): # profile viewer for students
    tanjiro = input("Your Full Name : \n")
    innosuke = input("Your Grade/Class : \n")
    #define path
    global kanao
    kanao = innosuke
    kanao += '/'
    kanao += tanjiro
    kanao += '.txt'
    k = open(kanao,"r")
    list_of_lines = k.readlines()
    for line in list_of_lines:
        print(line)

    k.close()
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    jinx = int(input("Enter 1 When You Are Done Reading"))
    if jinx == 1:
        attack()
    else:
        print("invalid input")

def Itoshiteru(): # profile viewer for teachers
    pew = input("Enter student name : ")
    die = input("Enter class name : ")
    pie = "/"

    global loli
    loli = die
    loli += pie
    loli += pew
    loli += '.txt'

    isee = open(loli,"r")
    list_of_lines = isee.readlines()
    for line in list_of_lines:
        print(line)

    isee.close()
    powder = int(input("Enter 1 When You Are Done Reading"))
    if powder == 1:
        attack()
    else:
        print("invalid input")

def Konpyuta(): # result viewer 
    pewd = input("Enter student name : ")
    die = input("Enter exam name : ")
    coco = input(" Enter grade in whcih student is : ")
    pie = "/"

    

    global sasagayo
    sasagayo = coco
    sasagayo += pie
    sasagayo += pewd
    sasagayo += '_'
    sasagayo += die
    sasagayo += '.txt'

    misa = os.path.isfile(sasagayo)
    if misa == True:
        iee = open(sasagayo,"r")
        list_of_line = iee.readlines()
        for line in list_of_line:
            print(line)

        iee.close()
        power = int(input("Enter 1 When You Are Done Reading"))
        if power == 1:
            attack()
        else:
            print("invalid input")
    if misa == False:
        print("The student's marks isn't generated")
        time.sleep(5)
        attack()

def Furukiyokijidai(): # result maker
    print("Student's Result Maker")
    Otona = input("Exam Name : ")
    Nemurenai = input("Enter Student's Full Name : ")
    Gakko = input("Grade in which student is : ")

    global Kanojo
    Kanojo = Gakko
    Kanojo += '/'
    Kanojo += Nemurenai
    Kanojo += '_'
    Kanojo += Otona
    Kanojo += '.txt'


    print(" Now Loading .......")
    time.sleep(3)
    
    os.system("cls||clear")
    sugoi = input(" Please enter the subject:marks in this format seperated by space (subject:marks)")

    Akua = open(Kanojo,"w")
    Akua.write(sugoi)
    Akua.write("\n")
    Akua.write(f"Changed on {charmander}")
    Akua.close()

    print(f"Thank You Marksheet made for {Nemurenai}")
    time.sleep(5)
    attack()

# load functions and print essentials
wishMe()
time.sleep(3)
logs()
print("Loading database and other accessories")
time.sleep(5)
loading()
print("LOADED")
print("Please select an option to continue :      ")  

print(" Enter 1 to register to the system  ")
print("\n")
print(" Enter 2 to login to the system")
print("\n")

a = int(input("     :   "))
if a == 1:
    bulbasaur() # calling function to make it accessible
    squirtle()
    
elif a == 2:
    squirtle()

else:
    print("invalid input exiting ......................")


