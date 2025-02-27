# convert string input (even fractions) to float
def string_frac(in_string):
    if "/" in in_string:
        nd = in_string.split("/")  # nd = numerator, denominator
        print(nd)
        n = float(nd[0])
        d = float(nd[1])
        ans = n/d
        print(ans)
    else:
        ans = float(in_string)
        print(ans)

in_string = input("Enter a fraction: ")
string_frac(in_string)