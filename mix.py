def pixel(pixel1, pixel2,):
    r1, g1, b1, a1 = pixel1
    r2, g2, b2, a2 = pixel2
    a = a1 + (a2 * (1.0 - a1 / 255.0))
    a_out = a / 255.0
    r = int(r1 * (1 - a2 / 255.0) + r2 * a_out)
    g = int(g1 * (1 - a2 / 255.0) + g2 * a_out)
    b = int(b1 * (1 - a2 / 255.0) + b2 * a_out)  
    r = max(0, min(r, 255))
    g = max(0, min(g, 255))
    b = max(0, min(b, 255))
    a = int(max(0, min(a, 255)))
    return r, g, b, a
u1 = int(input("A.r:"))
u2 = int(input("A.g:"))
u3 = int(input("A.b:"))
u4 = int(input("A.a:"))
v1 = int(input("B.r:"))
v2 = int(input("B.g:"))
v3 = int(input("B.b:"))
v4 = int(input("B.a:"))
pixel1 = (u1, u2, u3, u4) 
pixel2 = (v1, v2, v3, v4) 
r, g, b, a = pixel(pixel1, pixel2)
print("at (0, 0):")
print("r = ", r)
print("g = ", g)
print("b = ", b)
print("a = ", a)






