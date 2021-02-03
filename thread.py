import twint
import datetime

import parameter

TIME_FORMAT = '%Y%m%d%H%M%S'


# 通过username批量爬取Tweets
def getTweetsbylist(roster, conf):
    with open(roster, 'r', encoding='utf-8') as file:
        theTime = datetime.datetime.now().strftime(TIME_FORMAT)
        for name in file:
            c = parameter.configUname(conf, name.strip(), theTime)
            twint.run.Profile(c)


# 爬取单独的username下的Tweets
def getTweetsbyone(username, conf):
    theTime = datetime.datetime.now().strftime(TIME_FORMAT)
    c = parameter.configUname(conf, username, theTime)
    twint.run.Search(c)
