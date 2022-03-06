# Defining Function
def f(x):
    return x**3-x-4.5

def bisection(x0, x1, e):
    step = 1
    print('\n\n*** Metoda bisekcji implementacja ***')
    condition = True
    while condition:
        x2 = (x0 + x1) / 2
        print('Iteracja-%d, x2 = %0.6f i f(x2) = %0.6f' % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        step = step + 1
        condition = abs(f(x2)) > e

    print('\nWynik to : %0.8f' % x2)

x0 = input('Pierwszy strzal: ')
x1 = input('Drugi strzal: ')
e = input('Epsilon: ')

x0 = float(x0)
x1 = float(x1)
e = float(e)

if f(x0) * f(x1) > 0.0:
    print('Z tych wartosci nie da sie obliczyc bisekcji')
    print('Sprobuj z innymi wartosciami')
else:
    bisection(x0, x1, e)