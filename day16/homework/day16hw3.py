correct_pin = "9877"
attempts = 0
pin = ""

while pin != correct_pin:
    pin = input("Enter your PIN code: ")
    attempts += 1

print("PIN accepted.")
print(attempts * 2)