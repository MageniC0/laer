from PIL import Image
image_path = 'c1.png'
image = Image.open(image_path)
image.show()
#from(0,0),↘️
x = 10
y = 10
r,g,b,a = image.getpixel((x, y))
print(f"at ({x}, {y}): ")
print(f"r = ",r)
print(f"g = ",g)
print(f"b = ",b)
print(f"a = ",a)
image.close()
