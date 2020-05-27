def wyraz_ciagu(n = 1, a1 = 1, q = 1):
    return a1 * pow(q, n-1)

def n_wyrazow_ciagu(n = 1, a1= 1, q = 1):
    if q == 1:
        return a1 * n
    else:
        return a1 * (1 - pow(q, n)) / (1 - q)
