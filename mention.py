import os
import twint

config = twint.Config()

config.Output = './mention.json'
config.Store_json =  True
config.Lang = 'zh'
config.Min_likes = 2
config.All = 'iingwen'

# config.Proxy_host = '127.0.0.1'
# config.Proxy_type = 'socks5'
# config.Proxy_port = 10808

# print(config)

twint.run.Search(config)
