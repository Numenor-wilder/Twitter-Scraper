import json

# 去重list变量
existed = []


# 写入用户名
def writeName(roster, js):
    username = js['username']
    with open(roster, 'a+', encoding='utf-8') as file:
        if username not in existed:
            existed.append(username)
            file.writelines(username)
            file.writelines('\n')


# 提取username并生成名单
def extractUname(raw, roster):
    with open(raw, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:  # 到 EOF，返回空字符串，则终止循环
                break
            js = json.loads(line)
            writeName(roster, js)
