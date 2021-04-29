# Program Simulasi Inventory RPG
# Tugas Besar Daspro
# 16520166 - Thio Triansyah Putra

import os
import argparse

def menus():
    print("Welcome to magic pocket program! type /help for info")
    menu = str(input())
    if menu == "/help":
        print("======== HELP ========")
        print("register - to register new user")
        print("login - to log in to the system")
        print("newitem - to input new item")
        print("exit - to exit the program")
    elif menu == "register":
        reg()
    elif menu == "login":
        login()
    elif menu == "newitem":
        newItem()
    elif menu == "exit":
        pass
    else:
        print("Command is not understood")
        menus()

def reg():
    print("Enter your information below to complete your registration")
    name = input("Enter your fullname : ")
    user = input("Enter your username : ")
    password = input("Enter your password : ")
    address = input("Enter your address : ")
    validateReg(name,user,password,address)

def validateReg(name,user,password,address):
    if name.isalpha():
        if user != "":
            if password != "":
                if address != "":
                    print("Registration success! Welcome to magic pocket!")
                else:
                    print("Your address is empty!")
                    reg()
            else:
                print("Your password is empty!")
                reg()
        else:
            print("Your username is empty!")
            reg()
    else:
        print("Your name is empty!")
        reg()

def login():
    print("Enter your data to log in!")
    user = input("Enter your username : ")
    password = input("Enter your password : ")
    validateLogin()

def parseCSV (csvString):
    arr = []
    lines = explode(csvString, "\n")
    for line in lines:
        arr.append(explode(line, ";"))
    arr.pop(0)
    return arr
def explode(string, separator):
    arr = []
    el = ""
    for char in string:
        if char != separator:
            el += char
        else:
            arr.append(el)
            el = ""
    arr.append(el)
    return arr
def stringifyCSV(data):
    lines = []
    for charArr in data:
        lines.append(";".join(charArr))
    csvString = "\n".join(lines)
    return csvString

def loadCSV (path):
    f = open(path)
    csvString = f.read()
    return parseCSV(csvString)
def loadData():
    global userData, gadgetData, consumableData, consumableWithdrawData, gadgetBorrowData, gadgetReturnData
    parser = argparse.ArgumentParser()
    parser.add_argument("echo")
    dirPath = parser.parse_args().echo
    if (os.path.isdir(dirPath)):
        userData = loadCSV(dirPath + "/user.csv")
        gadgetData = loadCSV(dirPath + "/gadget.csv")
        gadgetBorrowData = loadCSV(dirPath + "/gadget_borrow.csv")
        gadgetReturnData = loadCSV(dirPath + "/gadget_return.csv")
        consumableData = loadCSV(dirPath + "/consumable.csv")
        consumableWithdrawData = loadCSV(dirPath + "/consumable_withdraw.csv")

def saveCSV(data, path):
    f = open(path, "w")
    csvString = stringifyCSV(data)
    f.write(csvString)
    f.close()
def saveData():
    saveCSV(userData, dirPath + "/user.csv")
    saveCSV(gadgetData, dirPath + "/gadget.csv")
    saveCSV(gadgetBorrowData, dirPath + "/gadget_borrow.csv")
    saveCSV(gadgetReturnData, dirPath + "/gadgetoh_return.csv")
    saveCSV(consumableData, dirPath + "/consumable.csv")
    saveCSV(consumableWithdrawData, dirPath + "/consumable_withdraw.csv")



menus()




















