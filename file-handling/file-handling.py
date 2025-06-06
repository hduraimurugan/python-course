import csv

# file= open("notes.txt","w")
# file.write("Welcome to file handling\n")
# file.write("This is a new file\n")
# file.close()

# file=open("notes.txt","r")
# content= file.read()
# print("File content:\n",content)
# file.close()

# file = open("notes.txt","a") #instead of a if u use w it will overwrite
# file.write("Adding new line \n")
# file.close()

# with open("notes.txt","r") as file:
#     for line in file:
#         print(line.strip())

# with open("notes.txt","a") as file:
#     file.write("Adding new 2nd line \n")

# with open("data.txt","r") as file:
#     print(file.readline().strip())
#     print(file.readline().strip())
#     print(file.readline().strip())

# with open("data.txt", "r") as f:
#     for _ in range(10):
#         print(f.readline().strip())

# with open("input.csv", "r") as infile, open("output.csv", "w") as outfile:
#     for line in infile:
#         print(line.strip())
#         outfile.write(line)

# with open("input.csv", "r") as file:
#     reader=csv.DictReader(file)
#     print(reader)
#     for row in reader:
#         print(row)
#         print(row["age"])

with open("input.csv", "r") as file:
    lines=file.readlines()
    # print(lines)
    for line in lines[0:]:
        # print(line)
        columns= line.strip().split(",")
        print(columns[2])
