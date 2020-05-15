# Euler's Method
def euler(f, x, y, h, steps=1):
    print("EULER'S METHOD")
    for _ in range(steps):
        print("x= {0:.{1}f}, y= {2:.{3}f}".format(x, 2, y, 5), end=', ')
        dy_dx = f(x, y)
        print("f(x,y)= {0:.{1}f}".format(dy_dx, 5), end=', ')
        y = y+h*dy_dx
        print("New_y= {0:.{1}f}".format(y, 5))
        x = x+h
    return y
        
# Modified Euler's Method
def modified_euler(f, x, y, h, steps=1, accuracy=1e-5):
    print("MODIFIED EULER'S METHOD")
    def isEqual(a, b):
        return abs(a-b) < accuracy
    for _ in range(steps):
        print("x= {0:.{1}f}, y= {2:.{3}f}".format(x, 2, y, 5), end=', ')
        dy_dx = f(x, y)
        origy = y
        print("f(x,y)= {0:.{1}f}".format(dy_dx, 5), end=', ')
        newy = y+h*dy_dx
        print("Mean_slope= -------, New_y= {0:.{1}f}".format(y, 5))
        x = x+h
        while(isEqual(y, newy) == False):
            y = newy
            print("x= {0:.{1}f}, y= {2:.{3}f}".format(x, 2, y, 5), end=', ')
            new_dy_dx = f(x, newy)
            print("f(x,y)= {0:.{1}f}".format(dy_dx, 5), end=', ')
            mean_slope = (dy_dx+new_dy_dx)/2
            newy = origy+h*mean_slope
            print("Mean_slope= {0:.{1}f}, New_y= {2:.{3}f}".format(mean_slope, 5, newy, 5))
    return y

# Runge's Method
def runge(f, x, y, h):
    print("RUNGE'S METHOD")
    print("y({0:.{1}f}) = {2:.{3}f}".format(x, 5, y, 5))
    k1 = h*f(x,y)
    k2 = h*f(x+h/2,y+k1/2)
    kprime = h*f(x+h,y+k1)
    k3 = h*f(x+h, y+kprime)
    k = (k1+4*k2+k3)/6
    print("k1 = {0:.{1}f}".format(k1, 5))
    print("k2 = {0:.{1}f}".format(k2, 5))
    print("k' = {0:.{1}f}".format(kprime, 5))
    print("k3 = {0:.{1}f}".format(k3, 5))
    print("k  = {0:.{1}f}".format(k, 5))
    print("y({0:.{1}f}) = {2:.{3}f}".format(x+h, 5, y+k, 5))
    return y+k;

# Runge-Kutta Method
def runge_kutta(f, x, y, h, steps=1):
    print("RUNGE-KUTTA METHOD")
    print("y({0:.{1}f}) = {2:.{3}f}".format(x, 5, y, 5))
    k1 = h*f(x,y)
    k2 = h*f(x+h/2,y+k1/2)
    k3 = h*f(x+h/2,y+k2/2)
    k4 = h*f(x+h,y+k3)
    k = (k1+2*k2+2*k3+k4)/6
    print("k1 = {0:.{1}f}".format(k1, 5))
    print("k2 = {0:.{1}f}".format(k2, 5))
    print("k3 = {0:.{1}f}".format(k3, 5))
    print("k4 = {0:.{1}f}".format(k4, 5))
    print("k  = {0:.{1}f}".format(k, 5))
    print("y({0:.{1}f}) = {2:.{3}f}".format(x+h, 5, y+k, 5))
    return y+k;

# Milne's Method
def milne(f, X, Y, xf, h, accuracy=1e-5):
    print("MILNE'S METHOD")
    def isEqual(a, b):
        return abs(a-b) < accuracy
    F = [f(x,y) for x, y in zip(X,Y)]
    yp = Y[0] + (4*h/3)*(2*F[1]-F[2]+2*F[3])
    print("Predictor: {0:.{1}f}".format(yp, 5))
    f4 = f(xf, yp)
    yc = Y[2] + (h/3)*(F[2]+4*F[3]+f4)
    print("f4: {0:.{1}f}, Corrector: {2:.{3}f}".format(f4, 5, yc, 5))
    while(isEqual(yp, yc) == False):
        yp = yc
        f4 = f(xf, yp)
        yc = Y[2] + (h/3)*(F[2]+4*F[3]+f4)
        print("f4: {0:.{1}f}, Corrector: {2:.{3}f}".format(f4, 5, yc, 5))
    return yc
    
# Adams-Bashforth Method
def adams_bashforth(f, X, Y, xf, h, accuracy=1e-5):
    print("ADAM'S-BASHFORTH METHOD")
    def isEqual(a, b):
        return abs(a-b) < accuracy
    F = [f(x,y) for x, y in zip(X,Y)]
    yp = Y[3] + (h/24)*(55*F[3]-59*F[2]+37*F[1]-9*F[0])
    print("Predictor: {0:.{1}f}".format(yp, 5))
    f1 = f(xf, yp)
    yc = Y[3] + (h/24)*(9*f1+19*F[3]-5*F[2]+F[1])
    print("f1: {0:.{1}f}, Corrector: {2:.{3}f}".format(f1, 5, yc, 5))
    while(isEqual(yp, yc) == False):
        yp = yc
        f1 = f(xf, yp)
        yc = Y[3] + (h/24)*(9*f1+19*F[3]-5*F[2]+F[1])
    print("f1: {0:.{1}f}, Corrector: {2:.{3}f}".format(f1, 5, yc, 5))
    return yc

