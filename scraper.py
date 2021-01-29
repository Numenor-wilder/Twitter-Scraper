import thread
import mention


def mentioned(config, outfile, username):
    mention.getMentioned(config, outfile, username)


def userlistThread(config, raw, roster):
    thread.makeList(raw, roster)
    thread.getTweetsbylist(roster, config)


def userThread(config, username):
    thread.getTweetsbyone(username, config)
