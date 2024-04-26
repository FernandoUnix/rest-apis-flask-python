size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input) # 5
square_metres = square_feet / 10.8
print(f"{square_feet} square feet is {square_metres} square metres.") #0.4629629629629629
print(f"{square_feet} square feet is {square_metres:.2f} square metres.") #0.46 square metres
