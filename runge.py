ACCURACY = 4

def f(x, y):
    return x + y

def runge(f, x, y, h, steps = 1, api = False):
    ''' Third Order Runge-Kutta Method '''
    extra = ACCURACY + 1    # calculations are accurate by an additional decimal place
    result = []
    for i in range(steps):
        k1 = round(h * f(x, y), extra)
        k2 = round(h * f(x + h/2, y + k1/2), extra)
        kp = round(h * f(x + h, y + k1), extra)
        k3 = round(h * f(x + h, y + kp), extra)
        k = round((k1 + 4 * k2 + k3) / 6, extra)
        y = round(y + k, extra)
        x = round(x + h, extra)
        result.append([[k1, k2, kp, k3, k], x, y])
    if api:
        return result
    else:
        for step in result:
            print("k1 = {0:.{5}f}\nk2 = {1:.{5}f}\nk' = {2:.{5}f}\nk3 = {3:.{5}f}\nk  = {4:.{5}f}".format(*step[0], ACCURACY))
            print("x  = {0:.{2}f}, y  = {1:.{2}f}".format(step[1], step[2], ACCURACY))
                  
                  
def runge_kutta(f, x, y, h, steps = 1, api = False):
    ''' Fourth Order Runge-Kutta Method '''
    extra = ACCURACY + 1    # calculations are accurate by an additional decimal place
    result = []
    for i in range(steps):
        k1 = round(h * f(x, y), extra)
        k2 = round(h * f(x + h/2, y + k1/2), extra)
        k3 = round(h * f(x + h/2, y + k2/2), extra)
        k4 = round(h * f(x + h, y + k3), extra)
        k = round((k1 + 2 * k2 + 2 * k3 + k4) / 6, extra)
        y = round(y + k, extra)
        x = round(x + h, extra)
        result.append([[k1, k2, k3, k4, k], x, y])
    if api:
        return result
    else:
        for step in result:
            print("k1 = {0:.{5}f}\nk2 = {1:.{5}f}\nk3 = {2:.{5}f}\nk4 = {3:.{5}f}\nk  = {4:.{5}f}".format(*step[0], ACCURACY))
            print("x  = {0:.{2}f}, y  = {1:.{2}f}\n".format(step[1], step[2], ACCURACY))
    
