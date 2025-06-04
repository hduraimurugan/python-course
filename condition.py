# age=30
#
# if age>= 18 :
#     print("You can vote")
# else:
#     print("You cant vote")



# marks=75
#
# if marks>= 90:
#     print("Grade A")
# elif marks>=70:
#     print("Grade B")
# elif marks>= 50:
#     print("Grade C")
# else:
#     print("Fail")


# age=18
# has_license="yes"
#
# if age>=18:
#     if has_license=="yes":
#         print("You can drive")
#     else:
#         print("Take license first")
# else:
#     print("You are too young to drive")



# mark=75
# attendance=80
#
# if mark>=50 and attendance>=70:
#     print("Allowed for exams")
# else:
#     print("Not allowed")



# recharge_amount=366
# data_balance=1.5
#
# if recharge_amount >= 399 or data_balance>=1:
#     print("You are eligible for bonus data")
# else:
#     print("you are not eligible")


order_amount=520
days ="sat"
membership='no'

if (order_amount>=500 and days in['sat','sun']) or membership=="gold":
    print("20% discount")
else:
    print("No discount")