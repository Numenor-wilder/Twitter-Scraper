import os

FILE_ROOT = "./twitter_data/"


# 配置按名爬取
def configUname(conf, username, nowTime):
    file_path = FILE_ROOT + nowTime
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    
    output_path = file_path + '/' + username + ".json"

    conf.Username = username
    conf.Store_json = True
    conf.Retweets = True
    conf.Output = output_path
    # 重置User_id，避免爬取列表用户数据重复
    conf.User_id = None

    # conf.Proxy_host = '127.0.0.1'
    # conf.Proxy_port = 10808
    # conf.Proxy_type = 'socks5'

    return conf


# 配置ALL方法
def configMention(conf, outfile, username):
    conf.Output = outfile
    conf.Store_json = True
    conf.Lang = 'zh'
    conf.Min_likes = 2
    conf.All = username

    # conf.Proxy_host = '127.0.0.1'
    # conf.Proxy_type = 'socks5'
    # conf.Proxy_port = 10808

    return conf
