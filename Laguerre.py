## This represents the final step of the differential transofrm method. This final step is actually 
## Another algorithm entirely, designed to compute the roots of a polynomial. In this case, we have a
## polynomial in terms of aplha which is equal to zero. Thus, it follows that alpha occurs at the roots of 
## said function. Once the roots have been computed, one can plug the aplha value into the previously
## mentioned "poynomial of polynomials" to ge ta taylor series approximation of the solution to the 
## functional. 



# import numpy as np

# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set_theme()
import math

G = [-0.5, 1, 0, 1/6, 0, 1/120]
# Polynomials will be stored as a list, containing the coefficients ordered from lowest to highest power.
# For example, this would be 1-2x-5x^2


def take_poly_derivative(a):
    b = []
    for i in range(1, len(a)):
        j = a[i]*i
        b.append(j)
    return b


def get_estimate(a):
    c = a[len(a)-1]
    a_scaled = [ val / c for val in a  ]
    return 1 + max(a_scaled)


def evaluate(a, x_o):
    c = a[len(a)-1]
    for i in range(1, len(a)):
        d = a[len(a)-1-i] + c*x_o
        c = d
    return c


def Laguerres_method(a):
    zo = get_estimate(a)
    a_p = take_poly_derivative(a)
    a_pp = take_poly_derivative(a_p)

    a_zo = evaluate(a, zo)
    a_p_zo = evaluate(a_p, zo)
    a_pp_zo = evaluate(a_pp, zo)

    d = len(a)
    print("ran")

    i = 0
    while i <100:
        i = i+1
        a_zo = evaluate(a, zo)
        a_p_zo = evaluate(a_p, zo)
        a_pp_zo = evaluate(a_pp, zo)

        delta = (a_zo / a_p_zo) * ( (1/d) + ( (d-1)/d )*( 1 - ( (d-1)/d )*( (a_zo * a_pp_zo)/a_p_zo ) )**0.5 )**(-1)
        zo = zo - delta
        print(delta)
        if abs(delta) < math.e**(-10):
            print(i)
            return zo
    print(zo)
    return zo

print(get_estimate(G))

print(Laguerres_method(G) )



