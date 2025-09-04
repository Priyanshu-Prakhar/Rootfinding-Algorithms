#In this file, I'll try implementing Newton's Rootfinding Algorithm.
#If this succeeds, I'll try writing it in C++.

def x2_minus2(m):
    return (m**2) -2

def derivative(f, x):
    h=0.1
    f_left = f(x-h)
    f_right = f(x+h)
    return (f_right - f_left)/(2*h)

abscissa = int(input("Enter the abscissa to calculate the derivative of x^2 : "))

print(f"Derivative of f(x)=x^2 at x = {abscissa} = ", f"{derivative(x2_minus2, abscissa):.3f}")
#guess = input("Enter your best guess of where the root may be nearby : ")
