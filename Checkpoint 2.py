# Question 1
Fname = input("Please Enter Your First Name :")
Lname = input("Please Enter Your Last Name :")
print(str(Lname) + ' ' + str(Fname))

# Question 2
P1 = str(input('Please Enter an Integer Value :'))
P2 = P1 + P1
P3 = P1 + P1 + P1
print(str(int(P1) + int(P2) + int(P3)) + ' (' + P1 + '+' + P2 + '+' + P3+')')

# Question 3
given_number = int(input("Please Enter an Integer Value :"))
mod = given_number % 2
if mod == 0:
    print("The given number is even.")
else:
    print("The given number is odd.")

# Question 4
result = ''
for x in range(2000, 3201):
    if not x % 5 == 0:
        if x % 7 == 0:
            result += str(x)
print(result)

# Question 5
given_number = int(input("""FACTORIAL CALCULATOR
Please Enter an Integer Value : """))

if given_number == 0:
    print(str(given_number) + '! = ' + str(1))
elif given_number > 0:
    result = 1
    while given_number > 1:
        result *= given_number
        given_number -= 1

    print("The Result is " + str(result) + ".")
else:
    print("Please Enter A +ve Integer Value !")


# Question 6
input_string = str(input("Please Enter Your String : "))
result = ''
for x in range(len(input_string)):
    if input_string[x] != ' ' and (x+1) % 2 != 0:
        result += input_string[x]
print(result)

# Question 7
# Get Price by input Function


def get_price():
    try:
        price = float(input("Please Enter Your Price : "))
        if price == 0:
            print("Please Enter Value Greater than 0.")
        else:
            return price
    except:
        print("Please Enter a Valid Value.")


price = 0.0

# Loop in case of invalid input

while not price:
    price = get_price()

if price >= 500:

    # discount 50% if value >= 500
    value_after_discount = price*(1-0.5)

elif price >= 200 and price < 500:

    # discount 30% if value between 200 and 500 (200 included)
    value_after_discount = price*(1-0.3)

else:

    # discount 10% if value < 200
    value_after_discount = price*(1-0.1)

print("The Value after discount = " + str(value_after_discount) + '$.')
