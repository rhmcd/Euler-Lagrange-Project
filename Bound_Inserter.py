## Note that the first set of 6 values are, essentially, an example. Nonetheles, it is important to note that 
## regardless of the numerical values, it is useful to note thee state of the structure needed to insert the bounds. 
## Each DFT value is stored as a polynomial function of some unknown coefficient alpha. Likeiwse, these idividual arrays
## are used as a coefficient inside of a larger polynomial, ie. the inverse DFT representation of the true solution.
## The purpose of this function is to transform this unweildy equation, a polynomial of polynomials almost, into 
## A single polynomial using one of the boundary conditions. This allows for the remaining variable, alpha, to
## be solved for by Laguerre's method. 


b0 = [0, 1]  ## ie. y(a)=b --> (a,b)
bn = [1, 2]

DFTval_1 = [1,0] ## ie. Y(k) = a + b * alpha + c * alpha^2 + d* alpha^3 --> [a,b, c, d]
DFTval_2 = [2,3, 1] ## 2 + 3 * alpha
DFTval_3 = [2,1]

DFTVals = [ DFTval_1, DFTval_2, DFTval_3 ] ## ie. y(x) ~= lim n -> inf ( sum i = 0 - n Y(i) )

def insert_bound(b_n, DFT_vals):
    shifted_DFT_vals = DFT_vals
    shifted_DFT_vals[0][0] = b_n[1] + shifted_DFT_vals[0][0]
    i = 1
    j = 0
    while i < len(DFT_vals):
        j = 0
        while j < len(DFT_vals[i]):
            shifted_DFT_vals[i][j] = b_n[0] * shifted_DFT_vals[i][j]
            j +=1
        i +=1
    return shifted_DFT_vals


def combine_values( DFT_vals):
    final_polynomial = []
    maxlen = 0
    for i in DFT_vals:
        #print(len(i))
        if len(i)> maxlen:
            maxlen = len(i)

    j = 0
    while j < maxlen:
        jthsum = 0
        for i in DFT_vals:
            if len(i) > j:
                jthsum += i[j]
        final_polynomial.append(jthsum)
        j += 1

print( combine_values(DFTVals) )
