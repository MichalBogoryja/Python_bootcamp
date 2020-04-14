a = 1
b = -2
c = 5

def main(a,b,c):
    delta = b**2 - 4*a*c
    if delta < 0:
        result = "Brak rozwiązań"
        return result
    elif delta == 0:
        x0 = -b/(2*a)
        return x0
    elif delta > 0:
        x1 = (-b - delta**0.5) / (2*a)
        x2 = (-b + delta**0.5) / (2*a)
        return x1, x2
    pass

main(a,b,c)