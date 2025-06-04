# Local -> Enclosing -> Global -> Built-In

# Local
# def order():
#     food="Chicken Biryani"
#     print("Your Order is:",food)
#
# order()

# Enclosing
# def card():
#     discount=10 #Enclosed
#
#     def checkout():
#         print("applying discount:", discount)
#
#     checkout()
# card()

# Global
# user_id= "Santosh H"
#
# def homepage():
#     print("Welcome", user_id)
#
# def profile():
#     print("Welcome to the profile", user_id)
#
# homepage()
# profile()
