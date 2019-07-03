#This Is Calculator Projects
import os
import math

print("Welcome To My First Simple Project(Calculator using Python3)")

while True:
    print("\n0 - Addition \n1 - Substraction \n2 - Multiplication \n3 - Division \n4 - Modulo \n5 - Raising to a power "
          "\n6 - Square root \n7 - Logarithm \n8 - Sine \n9 - Cosin \n10 - Tangent")

    oper = input("\Your option from the menus : ")

    #Addition
    if oper=="0":
        val1 = float(input("\nFirst Value :"))
        val2 = float(input("\nSecond Value :"))

        print("\nThe result is : ", val1, "+", val2, "=", val1 + val2, "\n")

        back = input("\nRecount?  (y =recount; n = main menu)")

        if back == 'y':
            continue
        else:
            break


