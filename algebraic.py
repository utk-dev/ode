from math import sqrt

def isEqual(a, b, threshold = 10**(-4)):
    return abs(a - b) < threshold

def poly_apply(poly, x):
    total = 0
    for p, coeff in enumerate(list(reversed(poly))):
        total += coeff*(pow(x, p))
    return total

def quadratic_solve(a, b, c):
    '''Get both roots of a quadratic equation'''
    D = b*b - 4*a*c
    if D > 0:
        return ((-b + sqrt(D))/(2*a), (-b - sqrt(D))/(2*a))
    elif D == 0:
        return (-b/(2*a), -b/(2*a))
    else:
        im = sqrt(-D)/(2*a)
        re = -b/(2*a)
        return (complex(re, im), complex(re, -im))

def eq_solve(a1, b1, c1, a2, b2, c2):
    '''Solve a pair of linear simultaneous equations'''
    x = b1*c2 - b2*c1
    y = c1*a2 - c2*a1
    den = a1*b2 - a2*b1
    return (x/den, y/den)

def synthetic_divide(X, p, q):
    ''' Fast synthetic division by a quadratic polynomial '''
    result = [X[0], X[1]+p*X[0]]
    for i in range(2, len(X)):
        result.append(X[i]+p*result[i-1]+q*result[i-2])
    return result

def newton_raphson(f, d, x, api = False, ACCURACY = 4):
    '''Newton-Raphson Method'''
    result = [round(x, ACCURACY)]
    new_x = round(x - f(x)/d(x), ACCURACY)
    result.append(new_x)
    while not isEqual(x, new_x, 10**(-ACCURACY)):
        x = new_x
        new_x = round(x - f(x)/d(x), ACCURACY)
        result.append(new_x)
        
    if api:
        return result
    else:
        for ind, val in enumerate(result):
            print("x{0} = {1:.{2}f}".format(ind, val, ACCURACY))

def lin_bairstow(poly, p, q, steps, api = False, ACCURACY = 4):
    "Lin-Bairstow Method"
    result = []
    for i in range(steps):
        B = synthetic_divide(poly, -p, -q)
        C = synthetic_divide(B, -p, -q)
        a1, b1, c1 = C[-3], C[-4], -B[-2]
        a2, b2, c2 = C[-2]-B[-2], C[-3], -B[-1]
        dp, dq = eq_solve(a1, b1, c1, a2, b2, c2)
        p += dp
        q += dq
        Bset = [round(z, ACCURACY) for z in B]
        Cset = [round(z, ACCURACY) for z in C]
        result.append((Bset, Cset, round(p, ACCURACY), round(q, ACCURACY), round(dp, ACCURACY), round(dq, ACCURACY)))
    r1, r2 = quadratic_solve(1, p, q)
    R = synthetic_divide(poly, -p, -q)
    r3, r4 = quadratic_solve(1, R[1], R[2])
    result.append((r1, r2, r3, r4))
    if api:
        return result
    else:
        for B, C, p, q, dp, dq in result[:-1]:
            print("\nb_i: " + str(B))
            print("c_i: " + str(C))
            print("dp: {0:.{2}f}, dq:{1:.{2}f}".format(dp, dq, ACCURACY)) 
            print("Factor: x^2 + ({0:.{2}f})x + ({1:.{2}f})".format(p, q, ACCURACY))
        print("\nRoots: ")
        for root in result[-1]:
            if not isinstance(root, complex):
                print("{0:.{1}f}".format(root, ACCURACY))
            else:
                print("{0:.{2}f} + ({1:.{2}f})i".format(root.real, root.imag, ACCURACY))

def graeffe(poly, api = False, ACCURACY = 4):
    ''' Graeffe's Root Squaring Method '''
    result = [poly]

    # find substituted polynomials
    for i in range(3):
        a, b, c, d = poly
        next_poly = [a**2, 2*a*c-(b**2), (c**2)-2*b*d, -(d**2)]
        result.append(next_poly)
        poly = next_poly
    
    # find γ₁, γ₂ and γ₃
    g1 = -poly[1]
    g2 = -poly[2]/poly[1]
    g3 = -poly[3]/poly[2]

    # find the roots
    ra1 = round(pow(g1, 1/8), ACCURACY)
    ra2 = round(pow(g2, 1/8), ACCURACY)
    ra3 = round(pow(g3, 1/8), ACCURACY)
    result.append([round(g1, ACCURACY), round(g2, ACCURACY), round(g3, ACCURACY)])
    
    # find sign of the roots
    r1 = ra1 if abs(poly_apply(result[0], ra1)) < abs(poly_apply(result[0], -ra1)) else -ra1
    r2 = ra2 if abs(poly_apply(result[0], ra2)) < abs(poly_apply(result[0], -ra2)) else -ra2
    r3 = ra3 if abs(poly_apply(result[0], ra3)) < abs(poly_apply(result[0], -ra3)) else -ra3
    result.append([r1, r2, r3])

    if api:
        return result
    else:
        for row, varname in zip(result[:-2], ['x', 'y', 'z', 'u']):
            print("{0}{4}³ + ({1}){4}² + ({2}){4} + ({3}) = 0".format(*row, varname))
        print("where x² = y, y² = z and z² = u")
        print("γ₁: {0:.{3}f}, γ₂: {1:.{3}f}, γ₃: {2:.{3}f}".format(*result[-2], ACCURACY))
        print("Roots: {0:.{3}f}, {1:.{3}f}, {2:.{3}f}".format(*result[-1], ACCURACY))

graeffe([1, -2, -5, 6])