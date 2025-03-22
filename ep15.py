# lattic paths for grid with n*n '_'

def factoriel(n):
    p = n
    for j in range(1,n):
        p *= j
    return p


def optimum_lattic_path(n,r):
    # calculating combination(n,r) in order to find lattic paths
    combination = factoriel(n+r) / ( factoriel(r) * factoriel(n) )   
    return combination

print(optimum_lattic_path(20,20))
