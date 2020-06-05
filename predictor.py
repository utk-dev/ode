ACCURACY = 4

def f(x, y):
    return (x*x)*(1+y)

def isEqual(a, b, threshold = 10**(-ACCURACY)):
    return abs(a - b) < threshold

def milne(f, X, Y, h, api = False):
    "Milne's Method"
    extra = ACCURACY + 1    # calculations are accurate by an additional decimal place
    result = []
    F = [round(f(x, y), extra) for x, y in zip(X, Y)]    # initial function values
    x4 = round(X[3] + h, extra)
    yp = round(Y[0] + (4*h/3)*(2*F[1]-F[2]+2*F[3]), extra)    # predictor expression
    result.append(yp)
    f4 = round(f(x4, yp), extra)
    yc = round(Y[2] + (h/3)*(F[2]+4*F[3]+f4), extra)          # corrector expression
    result.append((f4, yc))
    while not isEqual(yp, yc):
        yp = yc
        f4 = round(f(x4, yp), extra)
        yc = round(Y[2] + (h/3)*(F[2]+4*F[3]+f4), extra)
        result.append((f4, yc))
    if api:
        return result
    else:
        print("y_predictor = {0:.{1}f}".format(result[0], ACCURACY))
        for corrector in result[1:]:
            print("y4 = {0:.{2}f}, y_corrector = {1:.{2}f}".format(*corrector, ACCURACY))

def adams_bashforth(f, X, Y, h, api = False):
    "Adams-Bashforth Method"
    extra = ACCURACY + 1    # calculations are accurate by an additional decimal place
    result = []
    F = [round(f(x, y), extra) for x, y in zip(X, Y)]    # initial function values
    x1 = round(X[3] + h, extra)
    yp = round(Y[3] + (h/24)*(55*F[3]-59*F[2]+37*F[1]-9*F[0]), extra)    # predictor expression
    result.append(yp)
    f1 = round(f(x1, yp), extra)
    yc = round(Y[3] + (h/24)*(9*f1+19*F[3]-5*F[2]+F[1]), extra)          # corrector expression
    result.append((f1, yc))
    while not isEqual(yp, yc):
        yp = yc
        f1 = round(f(x1, yp), extra)
        yc = round(Y[3] + (h/24)*(9*f1+19*F[3]-5*F[2]+F[1]), extra)
        result.append((f1, yc))
    if api:
        return result
    else:
        print("y_predictor = {0:.{1}f}".format(result[0], ACCURACY))
        for corrector in result[1:]:
            print("y4 = {0:.{2}f}, y_corrector = {1:.{2}f}".format(*corrector, ACCURACY))