#-------------------------------------------------------------------------------
# Name:        Structural Programming Modules
# Purpose:     Praktikum Pengantar Teknologi Informasi I (2020/2021)
#
# Author:      Timotius Haniel
#
# Created:     12/10/2020
# Copyright:   (c) Timotius Haniel 2020
# Licence:     No License
#-------------------------------------------------------------------------------

global appetizerCount;
global mainCourseCount;
global dessertCount;
global drinksCount;

def displayMenu():
    print("***********************************************");
    print("*        Welcome to MIT & MT Restaurant       *");
    print("*     Created by (your name) using Python     *");
    print("***********************************************\n");
    print("Do you want to order something delicious? (y/n)\n");
    print("***********************************************\n");

def appetizerMenu():
    print("***********************************************");
    print("*        Welcome to MIT & MT Restaurant       *");
    print("*     Created by (your name) using Python     *");
    print("***********************************************\n");
    print("MIT & MT Restaurant Appetizer Menu: ");
    print("1. Mussels Marinara - Rp. 80.000");
    print("2. Garlic Bread with Cheese - Rp. 45.000");
    print("3. Grilled Asparagus in Prosciutto - Rp. 100.000\n");
    print("99. Next to Main Course\n");
    print("Enter your order (1-3 or 99):");

def appetizerPrice(appetizerOption):
    global appetizerCount;
    appPrice = 0;
    if(appetizerOption == 1):
        appPrice = 80000
        appetizerCount = 1;
    elif(appetizerOption == 2):
        appPrice = 45000
        appetizerCount = 1;
    elif(appetizerOption == 3):
        appPrice = 100000
        appetizerCount = 1;
    else:
        appPrice = 0;
        appetizerCount = 0;
    return appPrice;

def mainCourseMenu():
    print("***********************************************");
    print("*        Welcome to MIT & MT Restaurant       *");
    print("*     Created by (your name) using Python     *");
    print("***********************************************\n");
    print("MIT & MT Restaurant Main Course Menu: ");
    print("1. Seafood Risotto - Rp. 150.000");
    print("2. Vegetable Lasagna - Rp. 90.000");
    print("3. Grilled Chicken - Rp. 120.000\n");
    print("99. Next to Dessert\n");
    print("Enter your order (1-3 or 99):");

def mainCoursePrice(mainCourseOption):
    global mainCourseCount;
    mainCoursePrice = 0;
    if(mainCourseOption == 1):
        mainCourseCount = 1;
        mainCoursePrice = 150000
    elif(mainCourseOption == 2):
        mainCourseCount = 1;
        mainCoursePrice = 90000
    elif(mainCourseOption == 3):
        mainCourseCount = 1;
        mainCoursePrice = 120000
    else:
        mainCourseCount = 0;
        mainCoursePrice = 0;
    return mainCoursePrice;

def dessertMenu():
    print("***********************************************");
    print("*        Welcome to MIT & MT Restaurant       *");
    print("*     Created by (your name) using Python     *");
    print("***********************************************\n");
    print("MIT & MT Restaurant Dessert Menu: ");
    print("1. Raspberry Panna Cotta - Rp. 70.000");
    print("2. Classic Chocolate Cake - Rp. 80.000");
    print("3. Signature Tiramisu - Rp. 60.000\n");
    print("99. Next to Drinks \n");
    print("Enter your order (1-3 or 99):");

def dessertPrice(dessertOption):
    global dessertCount;
    dessertPrice = 0;
    if(dessertOption == 1):
        dessertCount = 1;
        dessertPrice = 70000;
    elif(dessertOption == 2):
        dessertCount = 1;
        dessertPrice = 80000
    elif(dessertOption == 3):
        dessertCount = 1;
        dessertPrice = 60000
    else:
        dessertCount = 0;
        dessertPrice = 0;
    return dessertPrice;

def drinksMenu():
    print("***********************************************");
    print("*        Welcome to MIT & MT Restaurant       *");
    print("*     Created by (your name) using Python     *");
    print("***********************************************\n");
    print("MIT & MT Restaurant Drinks Option: ");
    print("1. Mineral Water - Rp. 50.000");
    print("2. Coke - Rp. 80.000");
    print("3. Sparkling Water - Rp. 70.000\n");
    print("99. Next to Drinks \n");
    print("Enter your order (1-3 or 99):");

def drinkstPrice(drinksOption):
    global drinksCount;
    drinkstPrice = 0;
    if(drinksOption == 1):
        drinksCount = 1;
        drinkstPrice = 50000
    elif(drinksOption == 2):
        drinksCount = 1;
        drinkstPrice = 80000
    elif(drinksOption == 3):
        drinksCount = 1;
        drinkstPrice = 70000
    else:
        drinksCount = 0;
        drinkstPrice = 0;
    return drinkstPrice;

def invoiceDisplay(itemTotal, totalPrice):
    print("\n**************************************************");
    print("*   Thank you for visiting MIT & MT Restaurant   *");
    print("**************************************************\n");
    print("Total Item: "+str(itemTotal));
    print("Total Price: Rp. "+str(totalPrice));
    print("**************************************************");
    print("*   Please review us on any website that exists  *")
    print("**************************************************");
    return;

def countQuantity(appetizerCount, mainCourseCount, dessertCount, drinksCount):
    itemTotal = appetizerCount + mainCourseCount + dessertCount + drinksCount
    return itemTotal

def totalPrice(appetizerPrice, mainCoursePrice, dessertPrice, drinkstPrice):
    totalPrice = appetizerPrice + mainCoursePrice + dessertPrice + drinkstPrice
    return totalPrice

displayMenu();
displayMenuInput = str(input("Input"));
if(displayMenuInput=="y"):
    appetizerMenu();
    appetizerMenuInput = int(input("Input"));
    a = appetizerPrice(appetizerMenuInput)

    mainCourseMenu();
    mainCourseMenuInput = int(input("Input"));
    b = mainCoursePrice(mainCourseMenuInput)

    dessertMenu();
    dessertMenuInput = int(input("Input"));
    c = dessertPrice(dessertMenuInput)

    drinksMenu();
    drinksMenuInput = int(input("Input"));
    d = drinkstPrice(drinksMenuInput)

    itemTotal = countQuantity(appetizerCount, mainCourseCount, dessertCount, drinksCount)
    priceTotal = totalPrice(a,b,c,d)

    invoiceDisplay(itemTotal, priceTotal)