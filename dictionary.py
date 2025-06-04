# trip={
#     "trip_id": "UB12345",
#     "pickup": "Chennai Central",
#     "drop":["Tirunelveli", "Thoothukudi", "Nanguneri"],
#     "fare" : 41500.20,
#     "driver": "Maridas",
#     "status": "completed"
# }
# print(trip["pickup"])
# print(trip.get("pickup"))
#
# print(trip.keys())
# print(trip.values())
# print(trip.items())
#
# for key,value in trip.items():
#     print( key,":" ,value)
#
# # print(trip["drop"][0])
#
# for location in trip["drop"]:
#     print(location)

# trip.update({"car_model": "Tata M"})
# print(trip)
#
# trip.pop("car_model")
# print(trip)


# trips=[
#     {"trip_id": "UB52345", "pickup": "Chennai","drop":"Tirunelveli","fare" : 41500.20,"status": "completed"},
#     {"trip_id": "UB52848", "pickup": "Trichy", "drop": "Nagercoil", "fare": 41500.20, "status": "pending"},
#     {"trip_id": "UB52375", "pickup": "Kodaikanal", "drop": "Ooty", "fare": 41500.20, "status": "completed"},
#     {"trip_id": "UB52345", "pickup": "Chennai", "drop": "Karur", "fare": 41500.20, "status": "canceled"}
# ]
#
# for trip in trips:
#     print(trip["trip_id"])


trips={
 "UB52345": {"trip_id": "UB52345", "pickup": "Chennai","drop":"Tirunelveli","fare" : 41500.20,"status": "completed"},
 "UB52848": {"trip_id": "UB52848", "pickup": "Trichy", "drop": "Nagercoil", "fare": 41500.20, "status": "pending"},
 "UB52375": {"trip_id": "UB52375", "pickup": "Kodaikanal", "drop": "Ooty", "fare": 41500.20, "status": "completed"},
 "UB52365": {"trip_id": "UB52365", "pickup": "Chennai", "drop": "Karur", "fare": 41500.20, "status": "canceled"}
}

for trip_id, details in trips.items():
    print("Trip_id:",trip_id,"- From:", details["pickup"],"To:", details["drop"] )