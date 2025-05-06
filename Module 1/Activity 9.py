amount = int(input("Please Enter Amount for Withdrawal :"))
# Calculating the number of notes for each denomination
note500 = amount // 500
amount %= 500
note200 = amount // 200
amount %= 200
note100 = amount // 100
amount %= 100
note50 = amount // 50
amount %= 50
note20 = amount // 20
amount %= 20
note10 = amount // 10
amount %= 10
# Printing results
print("Notes of ₹500:", note500)
print("Notes of ₹200:", note200)
print("Notes of ₹100:", note100)
print("Notes of ₹50:", note50)
print("Notes of ₹20:", note20)
print("Notes of ₹10:", note10)
print("Remaining amount (if any): ₹", amount)