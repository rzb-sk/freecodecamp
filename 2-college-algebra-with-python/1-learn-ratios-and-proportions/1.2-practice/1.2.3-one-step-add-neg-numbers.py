# one-step addition with negative numbers
# So basically subtraction?

def one_step_subtract():
    import random
    # Creating two variables and assigning a random value for subtraction
    a = random.randint(-19,-1)
    b = random.randint(2,24)
    # printing the problem to be solved in the terminal
    print(a, "+ x =", b)
    # prompting the user to enter the answer
    ans = float(input("x = "))
    # the actual answer
    answer = b - a
    # testing the input
    if ans == answer:
        print("Correct! \n")
    else:
        print("Try again!")
        print("The correct answer is", answer, "\n")
    
one_step_subtract()
one_step_subtract()
