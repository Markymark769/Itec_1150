### number formatting
num1 = 123455
num2 = 3.14159

# print(f"{num1}")
#
# # put commas in
# print(f"{num1:,}")
#
# # 0 pad
# print(f"{num1:06d}")
# print(f"{num1:09d}")

# decimal rounding
print(f"{num2:.2f}")  # rounded twice after the decimal point
print(f"{num1 + num2:.4f}")  # rounded four times after the decimal point
