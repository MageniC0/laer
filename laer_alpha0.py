






bl = [[0,0,0,0,0,1,1,1,0,0,0,0,0],
      [0,0,1,1,1,1,1,1,1,1,1,0,0],
      [1,1,1,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1,1,1,1,1],
      [0,0,1,1,1,1,1,1,1,1,1,0,0],
      [0,0,0,0,0,1,1,1,0,0,0,0,0]]

up = [[0,0,0,1,1,1,0,0,0],
      [1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1],
      [0,0,0,1,1,1,0,0,0]]

lp = [[1,1,0,0,0,0,0],
      [0,0,1,1,1,0,0],
      [0,0,0,0,0,1,1]]

rp = [[0,0,0,0,0,1,1],
      [0,0,1,1,1,0,0],
      [1,1,0,0,0,0,0]]








def pos(x,y,z):
    m = 9 - 3 * x - 3 * y
    n = 12 + x + y - 4 * z
    return m * 2, n * 2

def e(c):
    r,g,b = c
    r = r * 75 // 100
    g = r * 75 // 100
    b = r * 75 // 100
    return (r,g,b)

for z in range(4):
    for y in range(4):
        for x in range(4):
            if tr_r[z][y][x]:
                m,n = pos(x,y,z)
                a,b = tr_c[z][y][x]
                c = e(a)
                d = e(b)
                r = tr_n[z][y][x]
                for i in range(12):
                    for j in range(12):
                        if bl[i][j]:
                            B[m+i][n+j] = 0
                if r[4]:
                    for i in range(9):
                        for j in range(4):
                            if up[i][j]:
                                A[m+i+2][n+j] = a
                        if r[0]:
                            for i in range(7):
                                for j in range(3):
                                    if lp[i][j]:
                                        A[m+i][n+j+2] = b
                        if r[1]:
                            for i in range(7):
                                for j in range(3):
                                    if lp[i][j]:
                                        B[m+i+6][n+j] = 1
                        if r[2]:
                            for i in range(7):
                                for j in range(3):
                                    if rp[i][j]:
                                        A[m+i+6][n+j+2] = b
                        if r[3]:
                            for i in range(7):
                                for j in range(3):
                                    if rp[i][j]:
                                        B[m+i][n+j] = 1
                if r[5]:
                    if r[1]:
                        for i in range(7):
                            for j in range(3):
                                if lp[i][j]:
                                    B[m+i][n+j+10] = 1
                    if r[3]:
                        for i in range(7):
                            for j in range(3):
                                if rp[i][j]:
                                    B[m+i+6][n+j+10] = 1
                if r[0]:
                    for i in range(6):
                        for j in range(10):
                            if fl[i][j]:
                                A[m+i][n+j+3] = a
                    if r[4] == 1 and r[6] == 1:
                        for k in range(8):
                            B[m][n+k+3] = 1
                if r[2]:
                    for i in range(6):
                        for j in range(10):
                            if fr[i][j]:
                                A[m+i+7][n+j+3] = a
                    if r[2] == 1 and r[7] == 1:
                        for k in range(8):
                            B[m+12][n+k+3] = 1