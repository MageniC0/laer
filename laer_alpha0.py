def pos(x,y,z):
    m = 9 - 3 * x - 3 * y
    n = 12 + x + y - 4 * z
    return m * 2, n * 2

def e(c):
    r,g,b = c
    r = r // 4 + r // 2
    g = g // 4 + g // 2
    b = b // 4 + b // 2
    return (r,g,b)

for z in range(4):
    for y in range(4):
        for x in range(4):
            if tr_r[z][y][x]:
                m,n = pos(x,y,z)
                a,b = tr_c[z][y][x]
                c = e(a)
                d = e(b)
                n = tr_n[z][y][x]
                for i in range(12):
                    for j in range(12):
                        if bl[i][j]:
                            B[m+i][n+j] = 0
                if n[4]:
                    for i in range(12):
                        for j in range(3):
                            if up[i][j]:
                                A[m+i][n+j] = a
                        if n[0]:
                            for i in range(7):
                                for j in range(3):
                                    if lp[i][j]:
                                        A[m+i][n+j+2] = b
                        if n[1]:
                            for i in range(7):
                                for j in range(3):
                                    if lp[i][j]:
                                        B[m+i+6][n+j] = 1
                        if n[2]:
                            for i in range(7):
                                for j in range(3):
                                    if rp[i][j]:
                                        A[m+i+6][n+j+2] = b
                        if n[3]:
                            for i in range(7):
                                for j in range(3):
                                    if rp[i][j]:
                                        B[m+i][n+j] = 1
                if n[5]:
                    if n[1]:
                        for i in range(6):
                            for j in range(3):
                                if lp[i][j]:
                                    B[m+i][n+j+10] = 1
                    if n[3]:
                        for i in range(6):
                            for j in range(3):
                                if rp[i][j]:
                                    B[m+i+6][n+j+10] = 1
