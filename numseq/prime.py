def is_prime(m):
    if m <= 1:
        return False
    for i in range(2, m):
        if m % i == 0:
            return False
    return True

def prime(n):
    plist = []
    for i in range(2, n):
        if is_prime(i):
            plist.append(i)
    return plist