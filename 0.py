from PIL import Image

# 读取原始图片
original_image = Image.open('b.png')

# 检查图片大小是否为 47x49
assert original_image.size == (49, 47), "The original image size is not 47x49."

# 使用 resize 方法放大图片，参数是一个二元组，表示新的宽高
# 使用 Image.NEAREST 来保持像素清晰（不进行插值）
enlarged_image = original_image.resize((980, 940), Image.NEAREST)

# 保存放大后的图片
enlarged_image.save('enlarged_940x980.png')