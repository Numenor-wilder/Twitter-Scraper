import json

def writeName(list, json):
    with open(list, 'a+', encoding='utf-8') as file:
        file.writelines(json['username'])
        file.writelines('\n')


def extractUname(raw, list):
    with open(raw, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:  # 到 EOF，返回空字符串，则终止循环
                break
            js = json.loads(line)
            writeName(list, js)