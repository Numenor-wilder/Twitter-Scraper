import os

FILE_ROOT = "./twitter_data/"


# 配置按名爬取
def configUname(conf, user_id, nowTime):
    file_path = FILE_ROOT + nowTime
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    
    output_path = file_path + '/' + user_id + ".json"

    conf.User_id = user_id
    conf.Lang = "zh"
    conf.Store_json = True
    conf.Retweets = True
    conf.Output = output_path
    # 重置Username，避免爬取列表用户数据重复
    conf.Username = None

    # conf.Proxy_type = 'socks5'
    # conf.Proxy_host = '127.0.0.1'
    # conf.Proxy_port = 10808

    return conf


# 配置ALL方法
def configMention(conf, outfile, username):
    conf.Output = outfile
    conf.Store_json = True
    conf.Lang = "zh"
    conf.Min_likes = 20
    conf.All = username

    # conf.Proxy_type = 'socks5'
    # conf.Proxy_host = '127.0.0.1'
    # conf.Proxy_port = 10808

    return conf
