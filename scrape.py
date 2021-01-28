import twint
import datetime

import config
import extractName

TIMEFORMAT = '%Y%m%d%H%M%S'


# 生成目标名单
def makeList(raw, list):
    extractName.extractUname(raw, list)

# 按username爬取profile
def scraping(list):
    with open(list, 'r', encoding = 'utf-8') as file:
        theTime = datetime.datetime.now().strftime(TIMEFORMAT)
        for name in file:
            config.configUname(name.strip(), theTime)
            twint.run.Profile(config.config)