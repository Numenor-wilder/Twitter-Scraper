import twint
import datetime

import parameter

TIME_FORMAT = '%Y%m%d%H%M%S'


# 通过username批量爬取Tweets
def getTweetsbylist(roster, conf):
    with open(roster, 'r', encoding='utf-8') as file:
        theTime = datetime.datetime.now().strftime(TIME_FORMAT)
        for userid in file:
            c = parameter.configUname(conf, userid.strip(), theTime)
            twint.run.Search(c)


# 爬取单独的username下的Tweets
def getTweetsbyone(username, conf):
    theTime = datetime.datetime.now().strftime(TIME_FORMAT)
    c = parameter.configUname(conf, username, theTime)
    twint.run.Search(c)
