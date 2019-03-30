# 输入身份证号，进行识别
# by ZENG Jinzhe
from datetime import date
import time
IDnumber = input("Please input your ID number:")
if len(IDnumber) != 18:
    print("Error! The length of your ID number is wrong.")
elif IDnumber[0:17].isdigit() and (IDnumber[17].isdigit or IDnumber[17] == "X"):
    IDyear = int(IDnumber[6:10])
    IDmonth = int(IDnumber[10:12])
    IDday = int(IDnumber[12:14])
    IDsex = int(IDnumber[16])
    if IDmonth == 2:
        if IDyear % 4 == 0:
            if IDyear % 100 == 0:
                if IDyear % 400 == 0:
                    run = 1
                else:
                    run = 0
            else:
                run = 1
        else:
            run = 0
        if (run == 1 and IDday > 29)or(run == 0 and IDday > 28):
            error = 1
        else:
            error = 0
    elif IDmonth == 1 or IDmonth == 3 or IDmonth == 5 or IDmonth == 7 or IDmonth == 8 or IDmonth == 10 or IDmonth==12:
        if IDday > 31:
            error = 1
        else:
            error = 0
    elif IDmonth == 4 or IDmonth == 6 or IDmonth == 9 or IDmonth == 11:
        if IDday > 30:
            error = 1
        else:
            error = 0
    else:
        error = 1
    if error == 1:
        print("Error! Your ID number is wrong.")
    else:
        if date.today().year < IDyear:
            err = 1
        elif date.today().year == IDyear and date.today().month < IDmonth:
            err = 1
        elif date.today().month == IDmonth and date.today().day < IDday:
            err = 1
        else:
            err = 0
        if err == 1:
            print("Error! You haven't been born, have you?")
        else:
            print("Your date of birth is ", IDyear,
                  "/", IDmonth, "/", IDday, ".")
            if IDsex % 2 == 0:
                print("Your gender is female.")
            else:
                print("Your gender is male.")
else:
    print("Error! You didn't type a number.")
