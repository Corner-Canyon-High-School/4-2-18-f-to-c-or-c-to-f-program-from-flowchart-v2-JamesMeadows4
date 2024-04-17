temp = int(input("Enter the temperature: ").strip())
choice = int(input("Type 1 for C -> F or type 2 for F -> C: ").strip())
if choice == 1:
    newTemp = (9 / 5 * temp) + 32
    print(f"Temperature in fahrenheit: {newTemp}")
elif choice == 2:
    newTemp = (5 / 9) * (temp - 32)
    print(f"Temperature in centigrade: {newTemp}")
else:
    print("Invalid input. Try again.")
