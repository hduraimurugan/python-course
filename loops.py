
# # For loop
# names =["sachin", "Moeen ali", "Musheer Ahmed", "Dhoni", "Kohli", "Virupaji", "Harpaji"]
#
# for test in names:
#     print(test.upper())

# While loop
# correct_pin="1234"
# entered_pin=""
#
# while entered_pin != correct_pin:
#     print("...Access Denied...")
#     entered_pin= input("Enter your pin: ")
#
# print("Access Granted✅")


# for i in range (10):
#     if i==5:
#         break
#     print(i) # 0 1 2 3 4
#
# for i in range (10):
#     if i==5:
#         continue
#     print(i) # 0 1 2 3 4 6 7 8 9

# n=[10,-5,7,-9,11]
#
# for num in n:
#     if num < 0:
#         continue
#     print(num)


# count = 5
#
# while count > 0:
#     print(f"Countdown: {count}")
#     count -= 1
#
# print("Time's up ⌛")


items=[]

while True:
    item = input("Add item (type 'done')...")
    if item.lower()== "done":
        break
    items.append(item)

print("Items in cart view: ", items)
