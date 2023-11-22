#!/usr/bin/python3
def magic_calculation(a, b):
    reslt = 0
    for j in range(1, 3):
        try:
            if j > a:
                raise Exception('Too far')
            else:
                reslt += a ** b / j
        except Exception:
            reslt = b + a
            break
    return (reslt)
