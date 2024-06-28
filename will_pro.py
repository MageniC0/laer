import json
import os

# 定义JSON文件的路径
RESOURCES_DIR = 'resources'

def get_json_path(filename):
    """获取JSON文件的完整路径"""
    return os.path.join(RESOURCES_DIR, f'{filename}.json')

def load_json(filename):
    """加载JSON文件，如果文件不存在则创建一个空列表"""
    json_path = get_json_path(filename)
    if not os.path.exists(json_path):
        with open(json_path, 'w') as f:
            json.dump([], f)
    with open(json_path, 'r') as f:
        return json.load(f)

def save_json(filename, data):
    """保存数据到JSON文件"""
    json_path = get_json_path(filename)
    with open(json_path, 'w') as f:
        json.dump(data, f, indent=2)

def delete_entry(data, code):
    """删除指定code的条目"""
    for entry in data:
        if entry['code'] == code:
            data.remove(entry)
            print("条目已删除！")
            return
    print("未找到项！")

def create_or_update_entry(data):
    """创建或更新条目"""
    code = input("请输入要创建或更新的code（或输入'create'以创建新条目，输入'delete'以删除条目）: ")
    if code.lower() == 'create':
        # 创建一个新条目
        name = input("请输入新的name: ")
        code = input("请输入新的code: ")
        a = input("请输入新的A值:")
        b = input("请输入新的B值:")
        r1, g1, b1 = a[:2], a[2:4], a[4:]
        # 将十六进制字符串转换为整数，并映射到0-255范围
        r1, g1, b1 = int(r1, 16), int(g1, 16), int(b1, 16)
        r2, g2, b2 = b[:2], b[2:4], b[4:]
        # 将十六进制字符串转换为整数，并映射到0-255范围
        r2, g2, b2 = int(r2, 16), int(g2, 16), int(b2, 16)
        ab = ((r1,g1,b1),(r2,g2,b2))
        new_entry = {
            "name": name,
            "code": int(code),
            "AB": ab
        }
        data.append(new_entry)
    else:
        # 更新一个已存在的条目
        code = int(code)
        for entry in data:
            if entry['code'] == code:
                name = input("请输入新的name（或按回车保留原name）: ") or entry['name']
                a = input("请输入新的A值:")
                b = input("请输入新的B值:")
                r1, g1, b1 = a[:2], a[2:4], a[4:]
                r1, g1, b1 = int(r1, 16), int(g1, 16), int(b1, 16)
                r2, g2, b2 = b[:2], b[2:4], b[4:]
                r2, g2, b2 = int(r2, 16), int(g2, 16), int(b2, 16)
                ab = ((r1,g1,b1),(r2,g2,b2))
                return
        print("未找到指定的code!")

    elif code.lower() == 'delete':
        code_to_delete = input("请输入要删除的code: ")
        try:
            code_to_delete = int(code_to_delete)
            delete_entry(data, code_to_delete)
        except ValueError:
            print("无效的code，请输入一个整数！")
    else:
        # 查找code并更新或显示信息
        code = int(code)
        found = False
        for entry in data:
            if entry['code'] == code:
                found = True
                
                break
        if found:
          code = int(code)
          for entry in data:
              if entry['code'] == code:
                  name = input("请输入新的name（或按回车保留原name）: ") or entry['name']
                  a = input("请输入新的A值:")
                  b = input("请输入新的B值:"
                  r1, g1, b1 = a[:2], a[2:4], a[4:]
                  r1, g1, b1 = int(r1, 16), int(g1, 16), int(b1, 16)
                  r2, g2, b2 = b[:2], b[2:4], b[4:]
                  r2, g2, b2 = int(r2, 16), int(g2, 16), int(b2, 16)
                  ab = ((r1,g1,b1),(r2,g2,b2))
                  entry['name'] = name
                  entry['AB'] = ab_input
                  print("条目已更新！")
                  return
         print("未找到指定的code!")

        else:
            print("已创建code:", code)  # 若找不到则提示已创建
def main():
    while True:
        print("\n操作选项:")
        print("1. 创建条目")
        print("2. 更新条目")
        print("3. 删除条目")
        print("4. 退出")
        choice = input("请输入您的选择（1/2/3/4）: ")
        if choice == '1':
            create_entry(data)
        elif choice == '2':
            code = input("请输入要更新的code: ")
            try:
                code = int(code)
                update_entry(data, code)
            except ValueError:
                print("无效的code，请输入一个整数！")
        elif choice == '3':
            code = input("请输入要删除的code: ")
            try:
                code = int(code)
                delete_entry(data, code)
            except ValueError:
                print("无效的code，请输入一个整数！")
        elif choice == '4':
            save_json(filename, data)
            break
        else:
            print("无效的选择，请重新输入！")
if __name__ == '__main__':
    main()
