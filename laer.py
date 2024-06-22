#预处理
from PIL import Image
print("loading...")
basic_image = Image.open("0002.png")#要堆叠的方块
bitmap = Image.new( "RGBA", (49,47))#4*4*4画布
shadow_basic = Image.new('RGBA', (13, 13), (0,0,0,0))#表面渲染空间
cube = basic_image.copy()#直接堆叠物
shadow_image = shadow_basic.copy()#对于直接堆叠物的最终表面渲染

#terraria = [[[0 for _ in range(4)]for _ in range(4)]for _ in range (4)]
#任务表
terraria = [
    #z = 1
    [[1,1,1,1],
     [1,1,0,1],
     [1,1,0,1],
     [1,0,0,0]],
    #z = 2
    [[1,0,0,1],
     [1,0,0,0],
     [0,0,0,0],
     [1,0,0,0]],
    #z = 3
    [[1,0,0,1],
     [1,0,0,0],
     [1,0,0,0],
     [1,0,0,0]],
    #z = 4
    [[0,1,1,1],
     [1,0,0,0],
     [1,0,0,0],
     [0,0,0,0]]
]

trrsz = trrsy = 1
terraria_basic = [[[0,0,0,0,0,0] for _ in range(6)] for _ in range(6)]
for trrz in range(4):
    trrsy = trrz + 1
    for trry in range(4):
        trrsz = trry + 1
        for trrx in range(4):
            terraria_basic[trrsy][trrsz][trrx+1] = terraria[trrz][trry][trrx]

#数据传送
file_name = input("name:" ) + ".png"
print("loading terrain...")
for z_with in range(4):
    for y_with in range(4):
        for x_with in range(4):
            if(terraria[z_with][y_with][x_with]):
                map_x = 18 - 6 * x_with + 6 * y_with
                map_y = 24 + 2 * x_with + 2 * y_with - 8 * z_with
                x = x_with + 1
                y = y_with + 1
                z = z_with + 1
                near = [
                    terraria_basic[z][y][x+1],
                    terraria_basic[z][y][x-1],
                    terraria_basic[z][y+1][x],
                    terraria_basic[z][y-1][x],
                    terraria_basic[z+1][y][x],
                    terraria_basic[z-1][y][x],
                    terraria_basic[z][y-1][x+1],
                    terraria_basic[z][y+1][x-1]]
                shadow1 = near[0] + 2 * near[1] + 4 * near[2] + 8 * near[3]
                shadow1 = format(shadow1, 'x').zfill(1)
                shadow2 = near[4] + 2 * near[5] + 4 * near[6] + 8 * near[7]
                shadow2 = format(shadow2, 'x').zfill(1)
                filename = f"ff{shadow2}{shadow1}.png"
                shadow_image = Image.open(filename)
                cube.alpha_composite(shadow_image)
                bitmap.alpha_composite(cube,(map_x,map_y))
                shadow_image = shadow_basic.copy()
                cube = basic_image.copy()
#完成
bitmap.save(file_name)
bitmap.show()









print(f"saved as {file_name}.")