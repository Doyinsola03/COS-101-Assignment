principal = float(input("Enter amount: "))
time = float(input("Enter time: "))
rate = float(input("Enter rate: "))
simple_interest = (principal*time*rate)/100
compound_interest = principal * ( (1+rate/100)*time -1)
print("simple interest is : %f" % (simple_interest))
print("compound interest is: %f" % (compound_interest))
print("Yusuf and Sons")