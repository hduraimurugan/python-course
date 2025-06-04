import sys

# Check if name argument is provided
# if len(sys.argv) == 2:
#     print("⚠️  Please provide your full name and last name as a command-line argument.")
#     print("💡 Example: python testapp.py Durai Murugan")
#     sys.exit(1)

# full_name =sys.argv[1]
# # last_name =sys.argv[2]
#
# # Format the name
# email = full_name.lower().replace(" ", ".")+ "@company.com"
#
# # Output
# print("\n ---Your Profile----")
# print("Full name:", full_name )
# print("Generated email:", email)

full_name =" ".join(sys.argv[1:])
print(full_name)
# last_name =sys.argv[2]

# Format the name
email = full_name.lower().replace(" ", ".")+ "@company.com"

# Output
print("\n ---Your Profile----")
print("Full name:", full_name )
print("Generated email:", email)