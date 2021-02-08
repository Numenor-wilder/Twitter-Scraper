import json

# 去重set
existed = set()


# 写入用户名
def writeName(manifest, js):
    user_id = js['user_id']
    with open(manifest, 'a+', encoding='utf-8') as file:
        if user_id not in existed:
            existed.add(user_id)
            file.writelines(str(user_id))
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
