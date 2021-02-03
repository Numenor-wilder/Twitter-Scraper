import json

# 去重set
existed = set()


# 写入用户名
def writeName(manifest, js):
    username = js['username']
    with open(manifest, 'a+', encoding='utf-8') as file:
        if username not in existed:
            existed.add(username)
            file.writelines(username)
            file.writelines('\n')


# 提取username并生成名单
def makeList(raw, manifest):
    with open(raw, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:  # 到 EOF，返回空字符串，则终止循环
                break
            js = json.loads(line)
            writeName(manifest, js)
