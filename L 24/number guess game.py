import random
n = random.randint(1,500)


if n%2 == 0 :
    print ("Hint :  the number is even (2,4,6,8,0)")
else:
    print ("Hint :  the number is odd (1,3,5,7,9)")

while True:
    guess = int(input ("guess the number between 1-500 : "))
    if guess > n:
        print("you nedd to guess a number lower than that")
    elif guess < n:
        print ("you need to guess something higher than that")
    else:
        print ("you got it!")
        break

