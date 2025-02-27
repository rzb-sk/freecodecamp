# To find out one of the value in the proportion, we indicate it with value 0.
n1 = 1
d1 = 2
n2 = 4  # unknown value
d2 = 0

if n2 == 0:
    answer = d2 * (n1 / d1)
    print("n2 =", answer)

if d2 == 0:
    answer = d1 * (n2 / n1)
    print("d2 =", answer)

