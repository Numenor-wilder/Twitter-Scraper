import twint
import requests

import scraper
import configuration as c


def post():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    payload = {'text': '爬虫结束', 'desp': '滚回来干活！！'}
    requests.post(c.wechatUrl, params=payload, headers=headers)


# 爬取回复中心用户的评论
def replies():
    config = twint.Config()
    scraper.mentioned(config, c.MENTIONED_JSON, c.coreAccount)


# 爬取用户时间线
def thread():
    config = twint.Config()
    scraper.userlistThread(config, c.MENTIONED_JSON, c.LIST_PATH)
