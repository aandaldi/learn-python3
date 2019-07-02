#This Is Calculator Projects
import os
import math

print("Welcome To My First Simple Project(Calculator using Python3)")
list_menu = ["Addition",
                 "Substraction",
                 "Multiplication",
                 "Division",
                 "Modulo",
                 "Raising to a power",
                 "Square root",
                 "Logarithm",
                 "Sine",
                 "Cosin",
                 "Tangent"]
# Menus
def choose_menu():
    os.system('clear')
    x=0
    for i in list_menu:
        print(x, i)
        x +=1
    choose = int(input("\nInsert number to select your operation : "))
    return choose

# Choose The Number
def calculator_function(number):
    if number >10 :
        choose_menu()
    else:
        val1 = int(input("\nInsert Val1 : "))
        val2 = int(input("\nInsert Val1 : "))

        #Addition
        if number == 0 :
            print("\nThe result is : ",val1,"+", val2, "=", val1+val2, "\n")
            back = input("\nRecount?  (y =recount; n = main menu;  q=quit )")
            if back=='y':
                calculator_function(number)
            elif back=='n':
                print("\n")
                a=choose_menu()
                calculator_function(a)
            else:
                print("See You next later")

#run
a = choose_menu()
calculator_function(a)
