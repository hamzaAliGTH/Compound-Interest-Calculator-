principle = 0
rate = 0
time = 0
while principle <=0:
    principle = float(input("Enter your initial Investment: "))
    if(principle<=0):
        print("Initial Investment can't be zero")
print(principle)
while rate <=0:
    rate = float(input("Enter interest rate: "))
    if(rate<=0):
        print("Intrest rate can't be zero")
print(rate)
while time <=0:
    time = int(input("Enter the time in years: "))
    if(time<=0):
        print("Time can't be zero")
print(time)

total = principle * pow((1 + rate/100),time)
print(f"The Compound Interest of your {principle} after {time} years/s is ${total:.2f} ")