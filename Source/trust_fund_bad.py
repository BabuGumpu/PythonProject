print(
"""
Please Enter the requested,monthly costs
"""
)
car = int(input("Enter Car  -- "))
rent = input("Enter Rent -- " )
food = int(input("Enter Food -- "))

total = int(car) + int(rent) + int(food)

print("\n Grand Total -->",long(float(total)))