#In this file, I'll try implementing Newton's Rootfinding Algorithm.
#If this succeeds, I'll try writing it in C++.


def x2_minus2(m):
    return (m**2) -2

def d(f, x):
    h=0.1
    f_left = f(x-h)
    f_right = f(x+h)
    return (f_right - f_left)/(2*h)

def newton(f,x):
    derv = d(f,x)
    return x - (f(x)/derv)

abscissa = float(input("Enter the abscissa to calculate the derivative of x^2 : "))

print(f"Derivative of f(x)=x^2 -2 at x = {abscissa} = ", f"{d(x2_minus2, abscissa):.3f} \n")

# x_new = x_old - (f(x)/f'(x))
step = abs(abscissa - newton(x2_minus2, abscissa))
abscissa = newton(x2_minus2, abscissa)

print(f"New X after Newton's Step is = {abscissa} \n")
print(f"Newton's Step = {step}")
next = input("Proceed Next ? (Press Enter)")

print("---------------------------------")

while next == "":
    print("---------------------------------")
    #Keep printing the derivative at the last abscissa
    print(f"Derivative of f(x)=x^2 at x = {abscissa} = ", f"{d(x2_minus2, abscissa):.3f} \n")
    
    #Update the step and abscissa every loop
    step = abs(abscissa - newton(x2_minus2, abscissa))
    abscissa = newton(x2_minus2, abscissa)

    #Keep printing the new abscissa
    print(f"New X after Newton's Step is = {abscissa} \n")
    print(f"Newton's Step = {step}")
    

    #Ask if the user wants to calculate further:
    next = input("Proceed Next ? (Press Enter)\n Any other input+enter will close the program \n")

    if next != "":
        break