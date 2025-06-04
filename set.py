# a={1,2,3,4,5,6,7,8,9}
# print(a)

# uber_cities= ["Bangalore", "Tirunelveli", "Chennai", "Salem", "Chennai", "Bangalore"]
#
# unique_cities= set(uber_cities)
# print(unique_cities)

uber_cities1= {"Bangalore", "Tirunelveli", "Chennai"}
uber_cities2= {"Salem", "Hyderabad", "Bangalore"}

print(uber_cities1.union(uber_cities2))
print(uber_cities1.intersection(uber_cities2))
print(uber_cities1.difference(uber_cities2))
print(uber_cities2.difference(uber_cities1))

uber_cities1.add("Karur")
print(uber_cities1)

uber_cities1.remove("Chennai")
uber_cities1.discard("Palani") #remove safe to avoid error when the item is  not in set
print(uber_cities1)
