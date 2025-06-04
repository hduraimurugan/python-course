trip_summary= ("Uber Go", "Chennai", "Airport", 450.00, "Completed" )

# print(trip_summary)
# print(trip_summary[0])

for item in trip_summary:
    print(item)

# print(len(trip_summary))
# print(trip_summary.count("Completed")) #no of items in tuple
# print(trip_summary.index("Airport"))

# trip_summary[1]= "Karur" #error
# Traceback (most recent call last):
#   File "D:\Code-Projects\Python\python-12hr-course\tuples.py", line 13, in <module>
#     trip_summary[1]= "Karur"
#     ~~~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment