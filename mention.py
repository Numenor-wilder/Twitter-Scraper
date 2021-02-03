import twint

import parameter


def getMentioned(conf, outfile, username):
    c = parameter.configMention(conf, outfile, username)
    twint.run.Search(c)
