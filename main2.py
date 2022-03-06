def newton(f,Df,x0,epsilon,max_iter):

    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Znaleziono wynik')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
    print('Exceeded maximum iterations. No solution found.')
    return None

p = lambda x: x**3-x-4.5
Dp = lambda x: 3*x**2 - 1
approx = newton(p,Dp,1,1e-10,10)
print(approx)
