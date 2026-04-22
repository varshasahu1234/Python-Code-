#======================== CHAI CODE =============================

# total = 0

# while True:
#     print("\n------Tea Menu-------")
#     print("1. Small Tea - ₹15")
#     print("2. Medium Tea - ₹30")
#     print("3. Large Tea - ₹45")

# #======== Enter the Choice of Cup ================
#     choice = input("Enter cup size (small/medium/large): ").lower()
#     Quantity = int(input("Enter quantity: "))       # Enter the qunatity of cup

# # if else statement ===============
#     if choice == "small":
#         price = 15
#     elif choice == "medium":
#         price = 30
#     elif choice == "large":
#         price = 45
#     else:
#         print("Invalid choice! Try again.")
#         continue

#     amount = price * Quantity
#     total += amount

#     print("Added ₹", amount, "to total bill.")

#     more = input("Do you want to order more? (yes/no): ").lower()
#     if more != "yes":
#         break

# print("\n--------- Final bill ----------")
# print("Total Amount to Pay: ₹",total)
# if total > 1000:
#     x = str(input("Enter your coupen code: ")).lower()
#     if x == "ayush":
#         print("You got 25% Discount",total/100*25)
#         print("Total Amount to Pay: ₹",total-total/100*25) 
# print("Thank you! Visit Again!")
