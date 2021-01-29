import twint

import config


def getMentioned(conf, outfile, username):
    c = config.configMention(conf, outfile, username)
    twint.run.Search(c)
