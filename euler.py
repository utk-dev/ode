ACCURACY = 4

def f(x, y):
    return x + y

def isEqual(a, b, threshold = 10**(-ACCURACY)):
    return abs(a - b) < threshold

def euler(f, x, y, h, steps, api = False):
    ''' Euler's Method '''
    result = []
    for i in range(steps):
        dy_dx = round(f(x, y), ACCURACY)
        new_y = round(y + h * dy_dx, ACCURACY)
        result.append((x, y, dy_dx, new_y))
        y = new_y
        x = round(x + h, ACCURACY)
    result.append((x, y, 0, 0))
    if api:
        return result
    else:
        for row in result:
            print("{0:.{4}f} {1:.{4}f} {2:.{4}f} {3:.{4}f}".format(*row, ACCURACY))

def modified_euler(f, x, y, h, steps, api = False):
    ''' Modified Euler's Method '''
    extra = ACCURACY + 1    # calculations are accurate by an additional decimal place
    result = []
    for i in range(steps):
        step = []
        orig_y = y
        dy_dx = round(f(x, y), extra)
        new_y = round(y + h * dy_dx, extra)
        step.append((x, y, dy_dx, dy_dx, new_y))
        x = round(x + h, extra)
        while not isEqual(y, new_y):
            y = new_y
            new_dy_dx = round(f(x, y), extra)
            mean_slope = round((dy_dx + new_dy_dx) / 2, extra)
            new_y = round(orig_y + h * mean_slope, extra)
            step.append((x, y, new_dy_dx, mean_slope, new_y))
        result.append(step)
    if api:
        return result
    else:
        for subtable in result:
            for row in subtable:
                print("{0:.{5}f} {1:.{5}f} {2:.{5}f} {3:.{5}f} {4:.{5}f}".format(*row, ACCURACY))
            print("")
