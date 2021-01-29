import twint
import scraper
import requests

LIST_PATH = "./list.txt"
MENTIONED_PATH = "./mentioned.json"


def post():
    url = 'https://sc.ftqq.com/SCU156283Tc80e2a8274b11cf58d9312a0d000fa3b6013fdb531d53.send'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    payload = {'text': '爬虫结束', 'desp': '滚回来干活！！'}
    requests.post(url, params=payload, headers=headers)


# def run():
#     config1 = twint.Config()
#     scraper.mentioned(config1, MENTIONED_PATH, 'iingwen')

def main():
    config = twint.Config()
    scraper.userlistThread(config, MENTIONED_PATH, LIST_PATH)
    post()


if __name__ == '__main__':
    main()
