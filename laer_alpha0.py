def pos(x,y,z):
    m = 9 - 3 * x - 3 * y
    n = 12 + x + y - 4 * z
    retern 2*m,2*n

def e(co):
    r,g,b = co
    r = r // 4 * 3
    g = g // 4 * 3
    b = b // 4 * 3
    return (r,g,b)

for z in range(4):
    for y in range(4):
        for x in range(4):
            if tr_r[z][y][x]:
                m,n = pos(x,y,z)
                a,b = tr_c[z][y][x]
                c = e(a)
                d = e(b)
                for i in range(12):
                    for j in range(12):
                        if bl[i][j]:
                            B[m+i][n+j] = 0
                if tr_n[z][y][x][4]:
                    for i in range(12):
                        for j in range(3):
                            if up[i][j]:
                                A[m+i][n+j] = a
                        if tr_n[z][y][x][0]:
                            for i in range(7):
                                for j in range(3):
                                    if lp[i][j]:
                                        A[m+i][n+j+2] = b
                        if tr_n[z][y][x][1]:
                            for i in range(7):
                                for j in range(3):
                                    if lp[i][j]:
                                        B[m+i+6][n+j+2] = 1
                        if tr_n[z][y][x][0]:
                            for i in range(7):
                                for j in range(3):
                                    if lp[i][j]:
                                        A[m+i+6][n+j+2] = b
                        if tr_n[z][y][x][1]:
                            for i in range(7):
                                for j in range(3):
                                    if lp[i][j]:
                                        B[m+i][n+j] = 1
