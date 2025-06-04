from pyexpat.errors import messages

driver_name="Santosh H"
mobile="9566672654"
masked= "+91 " + mobile[:2] + "******" +mobile[-2:]

print(driver_name.lower())
print(driver_name.upper())
print(driver_name.capitalize())
print(masked)

song="Shape OF you"
artist="DURAI h"

formatted=f"{song.title()} - {artist.title()}"
print(formatted)

location="chennai east"
fixed_location=location.replace("chennai east","Tirunelveli")
print(fixed_location)

message="Your ola booking ID is: OLA566854.Please do not share this to anyone except the driver"
booking_id=message.split(":")[1].split(".")[0].strip()
print(booking_id)

promo_msg="use zomato100 to get 100 off on your first order"
if "zomato100" in promo_msg:
    print("offer applied")

feedback="the driver was polite and the ride was smooth"
print("Position is:",feedback.find("polite"))

name="Durai Murugan H"
initials= "".join([word[0].upper() for word in name.split(" ")])
print(initials)

# dirty_input="   airport    "
# clean=dirty_input.strip()
# print(clean)

dirty_input = "   a  ir  p   or  t    "
# dirty_input="this is a test"
clean = ''.join(dirty_input.split())
print(clean)


word1="The trip was amazing and the car was clean"
word_count=len(word1.split())
print(word_count)