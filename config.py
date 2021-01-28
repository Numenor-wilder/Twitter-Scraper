import os
import twint

FILE_ROOT = "./twitter_data/"

# 爬虫配置
config = twint.Config()

# 配置按名爬取
def configUname(username, nowTime):
    FILE_PATH = FILE_ROOT + nowTime
    if not os.path.exists(FILE_PATH):
        os.makedirs(FILE_PATH)
    
    OUTPUT_PATH =  FILE_PATH + '/' + username +  ".json"

    # global config
    config.Username = username
    config.Store_json = True
    config.Retweets = True
    config.Output = OUTPUT_PATH
    # 重置User_id，避免爬取列表用户数据重复
    config.User_id = None

    # config.Proxy_host = '127.0.0.1'
    # config.Proxy_port = 10808
    # config.Proxy_type = 'socks5'
