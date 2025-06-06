feedback = input("Enter your feedback: ")

with open("feedback.txt", "a") as log:
    log.write(feedback + "\n")

print("Thanks for your feedback, Response saved")