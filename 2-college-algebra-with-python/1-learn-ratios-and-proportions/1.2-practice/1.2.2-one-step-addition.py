# Simplest one-step addition

def one_step_add():
    import random
    # Display problem
    a = random.randint(-4,10)
    b = random.randint(2,24)
    print("x +", a, "=", b)
    # prompting for the answer
    ans = float(input("x = "))
    # answer calculated
    answer = b - a
    # test input
    if ans == answer:
        print("Correct! \n")
    else:
        print("Try again")
        print("the correct answer is ", answer, "\n")


one_step_add()