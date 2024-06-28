import os
import json
# 读取.json文件，获取方块名与信息项的映射关系
def read_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data
# 创建一个4x4x4的三维数组，用于存储方块信息
def create_cube(data):
    cube = [[[(0, 0, 0) for _ in range(4)] for _ in range(4)] for _ in range(4)]
    return cube
# 功能1：遍历每一个位置输入方块信息
def input_block_info(cube, data):
    for z in range(4):
        for y in range(4):
            for x in range(4):
                block_name = input(f"请输入({x},{y},{z})位置的方块名：")
                if block_name in data:
                    cube[z][y][x] = data[block_name]
                else:
                    print(f"未找到名为{block_name}的方块信息，将使用默认值((0,0,0),(0,0,0))")
                    cube[z][y][x] = ((0, 0, 0), (0, 0, 0))
# 功能2：查找指定位置的方块名字和信息项
def find_block_info(cube, x, y, z):
    if 0 <= x < 4 and 0 <= y < 4 and 0 <= z < 4:
        return cube[z][y][x]
    else:
        print("坐标超出范围")
        return None
# 功能3：查看.json文件的名字与信息项的一一对应关系
def show_data(data):
    for key, value in data.items():
        print(f"{key}: {value}")
if __name__ == "__main__":
    file_path = os.path.join("resource", "blocks.json")
    data = read_json(file_path)
    cube = create_cube(data)
    input_block_info(cube, data)
    x, y, z = map(int, input("请输入要查找的坐标(x,y,z)：").split(','))
    result = find_block_info(cube, x, y, z)
    if result:
        print(f"({x},{y},{z})位置的方块名字和信息项为：{result}")
    show_data(data)
