playlist= ["Naa ready Dhaa", "Feel it", "Run it up!", "OG Sambavam"]
favourite_foods= ["Pizza", "Mutton Biryani", "Idly", "Dosa"]
recent_locations= ["Bangalore", "Tirunelveli", "Chennai", "Salem"]

# print("Spotify List", playlist)
# print("Zomato food", favourite_foods)
print("Uber locs", recent_locations)

# List methods
# playlist.append("Pathikichu")
# print("After append:", playlist)
#
# playlist.insert(2,"Kanimma")
# print("After insert:", playlist)
#
# playlist.remove("Kanimma")
# print("After remove:", playlist)
#
# playlist.pop()
# print("After pop:", playlist)
#
# playlist.reverse()
# print("After reverse:", playlist)
#
# print("Count:", playlist.count("OG Sambavam"))

# List slice
# print("Top 2 songs", playlist[0:2])
#
# print("Recent locations", recent_locations[-2:])

# List iterations

# for food in favourite_foods:
#     print("All food", food)
#
# for song in playlist:
#     print(f"{song} - song by: Durai ")

# favourite_foods[1]="Puri"
# print(favourite_foods)

for i,location in enumerate(recent_locations):
    print(f"location {i+1}: {location}")